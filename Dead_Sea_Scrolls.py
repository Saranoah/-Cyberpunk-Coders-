#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
from dataclasses import dataclass
from typing import List, Dict

# ==== HOLY DATACLASSES ====
@dataclass
class Scripture:
    title: str
    verses: List[str]
    revelation_level: int  # 1-10

@dataclass
class DebuggingMonk:
    name: str
    skills: Dict[str, int]
    enlightenment: float  # 0.0 to 1.0

# ==== SACRED TEXTS ====
CODICES = {
    "Segfault": Scripture(
        title="The Book of Segfault",
        verses=[
            "And lo, the Core Dump did appear unto the debugger",
            "Seven stack frames deep did GDB reveal the truth",
            "But the NULL pointer was a lie from the beginning"
        ],
        revelation_level=7
    ),
    "MemoryLeaks": Scripture(
        title="The Epistle of Memory Leaks",
        verses=[
            "Valgrind the Pure walked through unfreed allocations",
            "Each leak a sin against the /dev/null",
            "Only through --leak-check=full may you be saved"
        ],
        revelation_level=9
    )
}

# ==== CYBER MONK SIMULATOR ====
class MonasteryOfCode:
    def __init__(self):
        self.monks = [
            DebuggingMonk("Brother GDB", {"reverse_engineering": 8}, 0.8),
            DebuggingMonk("Sister Valgrind", {"memory_purification": 9}, 0.95)
        ]
        self.player = DebuggingMonk("Novice", {"python": 3}, 0.1)
    
    def typewriter(self, text: str, speed: float = 0.03):
        """Holy terminal revelation effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()
    
    def reveal_scripture(self, codex_name: str):
        """Divine text unfolding"""
        scripture = CODICES[codex_name]
        self.typewriter(f"\n=== {scripture.title} ===\n", 0.01)
        
        for verse in scripture.verses:
            # Random chance of "corruption"
            if random.random() < 0.2:
                verse = verse[:len(verse)//2] + "..." + verse[len(verse)//2:]
            self.typewriter(f"• {verse}")
            time.sleep(0.5)
        
        self.player.enlightenment += scripture.revelation_level * 0.05
    
    def debug_ritual(self):
        """Sacred debugging practice"""
        errors = [
            "Segmentation fault (core dumped)",
            "SyntaxError: unexpected EOF while parsing",
            "ImportError: No module named 'enlightenment'"
        ]
        self.typewriter("\n[ Initiate Debugging Ritual ]")
        
        for i in range(3):
            error = random.choice(errors)
            self.typewriter(f"\nERROR: {error}")
            
            solution = input("How will you fix this? > ")
            if "google" in solution.lower():
                self.typewriter("\nThe Elder Monks nod approvingly")
                self.player.skills["research"] = self.player.skills.get("research", 0) + 1
            else:
                self.typewriter("\nThe compiler rejects your offering")
    
    def run(self):
        """Main pilgrimage"""
        self.typewriter("WELCOME TO THE MONASTERY OF CODE\n")
        
        while self.player.enlightenment < 0.8:
            print(f"\nCurrent Enlightenment: {self.player.enlightenment:.2f}/1.0")
            action = input(
                "Choose your path:\n"
                "1. Study Sacred Texts\n"
                "2. Perform Debugging Ritual\n"
                "3. Consult Elder Monks\n"
                "> "
            )
            
            if action == "1":
                codex = random.choice(list(CODICES.keys()))
                self.reveal_scripture(codex)
            elif action == "2":
                self.debug_ritual()
            elif action == "3":
                monk = random.choice(self.monks)
                self.typewriter(f"\n{monk.name} whispers: 'Use {random.choice(list(monk.skills.keys()))}...'")
        
        self.typewriter("\nYOU HAVE ACHIEVED TECHNICAL ENLIGHTENMENT!")
        self.typewriter("The sacred `./configure && make && sudo make install` is complete.")

if __name__ == "__main__":
    temple = MonasteryOfCode()
    try:
        temple.run()
    except KeyboardInterrupt:
        print("\nThe stack trace fades into nothingness...")
