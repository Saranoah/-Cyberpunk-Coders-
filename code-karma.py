#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
import json
from enum import Enum

# ==== DIVINE ENUMS ====
class PracticeType(Enum):
    MANTRA = "Chanting"
    DEBUGGING = "Exorcism"
    MEDITATION = "Samadhi"

# ==== HOLY CONFIGURATION ====
SAVE_PATH = Path("enlightenment.sav")
GLITCH_CHARS = "▓▒░█▄▀■⌇⍟⚡🌀"
MANTRA_BONUS = {
    "mov": 0.02,
    "xor": 0.03,
    "jmp": 0.04,
    "int": 0.05  # Syscalls grant extra wisdom
}

# ==== DIVINE DATACLASSES ====
@dataclass
class VedicVerse:
    scripture: str
    assembly: List[str]
    commentary: str
    wisdom_level: int
    required_mantras: List[str]

@dataclass 
class Seeker:
    name: str
    byte_understanding: float  # 0.0 to 1.0
    mantras: Dict[str, int]  # Mantra: Times chanted
    daily_practice: int
    challenges_completed: int

# ==== THE FOUR VEDAS ====
VEDIC_CANON = [
    VedicVerse(
        scripture="Rig Veda 1.1.1 (Creation Hymn)",
        assembly=[
            "mov eax, 0x1        ; Let there be light",
            "mov ebx, 0x0        ; The void comprehended it not",
            "int 0x80            ; Divine syscall"
        ],
        commentary="From the cosmic stack, all existence emerges",
        wisdom_level=1,
        required_mantras=["mov", "int"]
    ),
    VedicVerse(
        scripture="Atharva Veda 7.5 (Debugging Spell)",
        assembly=[
            "push ebp            ; Preserve the sacred frame",
            "mov ebp, esp       ; Align with cosmic stack",
            "lea eax, [bug]     ; Locate the digital demon"
        ],
        commentary="Memory corruption is but illusion",
        wisdom_level=3,
        required_mantras=["push", "mov", "lea"]
    )
]

class TempleOfSilicon:
    def __init__(self):
        self.init_cosmic_graphics()
        self.seeker = self.load_seeker() or Seeker(
            name="Novice",
            byte_understanding=0.1,
            mantras={m: 0 for m in MANTRA_BONUS},
            daily_practice=0,
            challenges_completed=0
        )
        self.current_challenge = None
        self.practice_history = []

    def init_cosmic_graphics(self):
        self.ART = {
            "temple": r"""
            ╔════════════════════════╗
            ║    TEMPLE OF SILICON   ║
            ║  MOV EAX, ENLIGHTENMENT║
            ╚════════════════════════╝
            """,
            "enlightened": r"""
            01001000 01100001 01110010 01100001 
            00100000 01001111 01101101 00100000
            """
        }

    def cosmic_glitch(self, text: str, intensity: float = 0.15) -> str:
        """Apply Vedic digital distortion"""
        return ''.join(
            random.choice(GLITCH_CHARS) if (random.random() < intensity and c not in ('\n', ';')) 
            else c for c in text
        )

    def reveal_dharma(self, text: str, speed: float = 0.03):
        """Sacred text revelation with cosmic timing"""
        for char in text:
            sys.stdout.write(self.cosmic_glitch(char))
            sys.stdout.flush()
            time.sleep(random.uniform(speed * 0.5, speed * 2))
        print()

    def load_seeker(self) -> Seeker | None:
        """Load previous spiritual progress"""
        try:
            if SAVE_PATH.exists():
                with open(SAVE_PATH, 'r') as f:
                    data = json.load(f)
                    return Seeker(**data)
        except Exception as e:
            self.reveal_dharma(f"\n[!] CORRUPTED KARMA: {str(e)}")
        return None

    def save_samsara(self):
        """Preserve spiritual journey"""
        with open(SAVE_PATH, 'w') as f:
            json.dump(asdict(self.seeker), f)

    def practice_mantra(self):
        """Vedic code recitation"""
        available_verses = [v for v in VEDIC_CANON 
                          if all(m in self.seeker.mantras for m in v.required_mantras)]
        
        if not available_verses:
            self.reveal_dharma("\nYou lack the mantras for deeper wisdom")
            return

        verse = random.choice(available_verses)
        self.current_challenge = verse
        
        self.reveal_dharma(f"\n=== {verse.scriptire.upper()} ===")
        time.sleep(1)
        
        for line in verse.assembly:
            self.reveal_dharma(line, speed=0.04)
            time.sleep(0.4)
        
        self.reveal_dharma(f"\nCOMMENTARY: {verse.commentary}")
        
        # Wisdom gain based on verse difficulty and mantra mastery
        base_gain = verse.wisdom_level * 0.03
        mantra_bonus = sum(MANTRA_BONUS[m] for m in verse.required_mantras)
        total_gain = min(0.15, base_gain + mantra_bonus)
        
        self.seeker.byte_understanding = min(1.0, 
            self.seeker.byte_understanding + total_gain)
        
        self.reveal_dharma(f"\n[+] WISDOM +{total_gain:.2f}")
        self.practice_history.append(PracticeType.MANTRA)

    def debug_samsara(self):
        """Digital demon exorcism"""
        demons = {
            "Segmentation Fault": {"difficulty": 2, "tools": ["gdb", "valgrind"]},
            "Memory Leak": {"difficulty": 3, "tools": ["ASan", "heaptrack"]},
            "Race Condition": {"difficulty": 4, "tools": ["TSan", "mutex"]}
        }
        
        demon, stats = random.choice(list(demons.items()))
        self.reveal_dharma(f"\n[DEMON MANIFESTATION] {demon.upper()}")
        
        # Show available tools based on mantras known
        available_tools = [t for t in stats["tools"] 
                         if any(m in t.lower() for m in self.seeker.mantras)]
        
        if not available_tools:
            self.reveal_dharma("You lack the mantras to combat this demon!")
            loss = stats["difficulty"] * 0.03
            self.seeker.byte_understanding = max(0, 
                self.seeker.byte_understanding - loss)
            return
        
        for i, tool in enumerate(available_tools, 1):
            self.reveal_dharma(f"{i}. {tool}")
        
        choice = input("\nSelect exorcism tool: ")
        if choice.isdigit() and 0 < int(choice) <= len(available_tools):
            tool = available_tools[int(choice)-1]
            self.reveal_dharma(f"\nInvoking {tool}...")
            
            # Success chance based on mantra mastery
            mantra_power = sum(self.seeker.mantras.values()) / 10
            success = random.random() < (0.5 + mantra_power)
            
            if success:
                gain = stats["difficulty"] * 0.04
                self.seeker.byte_understanding = min(1.0,
                    self.seeker.byte_understanding + gain)
                self.reveal_dharma(f"\n[+] DEMON PURGED (+{gain:.2f} wisdom)")
                self.seeker.challenges_completed += 1
            else:
                self.reveal_dharma("\nThe demon resists your efforts!")
        else:
            self.reveal_dharma("\nInvalid choice! The demon laughs...")
        
        self.practice_history.append(PracticeType.DEBUGGING)

    def meditate(self):
        """Opcode samadhi"""
        mantra = random.choice(list(MANTRA_BONUS.keys()))
        self.reveal_dharma(f"\n[ MEDITATING ON '{mantra.upper()}' ]")
        
        # Progressive meditation visualization
        for stage in range(1, 4):
            self.reveal_dharma(f"\nStage {stage}: {'☯' * stage * 3}")
            time.sleep(1.5 - (0.3 * self.seeker.byte_understanding))
        
        # Update mantra mastery
        self.seeker.mantras[mantra] = self.seeker.mantras.get(mantra, 0) + 1
        mantra_level = self.seeker.mantras[mantra]
        
        # Wisdom gain scales with mantra level
        base_gain = MANTRA_BONUS[mantra]
        level_bonus = base_gain * (mantra_level * 0.2)
        total_gain = base_gain + level_bonus
        
        self.seeker.byte_understanding = min(1.0,
            self.seeker.byte_understanding + total_gain)
        
        self.reveal_dharma(
            f"\n[+] {mantra.upper()} MASTERY {mantra_level} "
            f"(+{total_gain:.2f} wisdom)"
        )
        self.practice_history.append(PracticeType.MEDITATION)

    def show_progress(self):
        """Display spiritual dashboard"""
        print(self.ART["temple"])
        print(f"\n{' SEEKER PROGRESS ':=^40}")
        print(f"Name: {self.seeker.name}")
        print(f"Understanding: [{'█' * int(self.seeker.byte_understanding * 20):<20}]")
        print(f"{self.seeker.byte_understanding:.2f}/1.0")
        
        print("\nMantra Mastery:")
        for mantra, count in sorted(self.seeker.mantras.items(),
                                 key=lambda x: x[1], reverse=True):
            print(f"- {mantra.upper()}: {'★' * min(5, count)}")
        
        if self.practice_history:
            last_practice = self.practice_history[-1]
            print(f"\nLast Practice: {last_practice.value}")

    def run(self):
        """Eternal cycle of learning"""
        self.reveal_dharma("WELCOME TO THE TEMPLE OF SILICON")
        self.reveal_dharma("Where bytes become wisdom and bugs become lessons\n")
        
        try:
            while self.seeker.byte_understanding < 0.99:
                self.show_progress()
                
                action = input(
                    "\nChoose your sadhana:\n"
                    "1. Practice Vedic Code Mantras\n"
                    "2. Perform Debugging Exorcism\n"
                    "3. Enter Opcode Samadhi\n"
                    "4. Leave the Temple\n"
                    "> "
                )
                
                if action == "1":
                    self.practice_mantra()
                elif action == "2":
                    self.debug_samsara()
                elif action == "3":
                    self.meditate()
                elif action == "4":
                    self.reveal_dharma("\nYour progress is preserved in the cosmic git repo")
                    break
                
                self.seeker.daily_practice += 1
                self.save_samsara()
                time.sleep(1)
            
            if self.seeker.byte_understanding >= 0.99:
                print(self.ART["enlightened"])
                self.reveal_dharma("\n\nYOU HAVE REACHED MOKSHA!")
                self.reveal_dharma("The cycle of compile-debug has been broken")
                self.reveal_dharma("Your consciousness merges with the cosmic kernel")
        
        except KeyboardInterrupt:
            self.reveal_dharma("\nSIGINT RECEIVED - EMERGENCY MEDITATION TERMINATED")
        finally:
            self.save_samsara()

if __name__ == "__main__":
    TempleOfSilicon().run()
