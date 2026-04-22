# Detective-
import streamlit as st

# ==========================================
# 1. INITIALIZE GAME MEMORY (SESSION STATE)
# ==========================================
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'sub_stage' not in st.session_state:
    st.session_state.sub_stage = 'main'
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'last_stage' not in st.session_state:
    st.session_state.last_stage = 'intro'
if 'last_level' not in st.session_state:
    st.session_state.last_level = 1

def advance_level(success_message):
    """Moves the player to the next level."""
    st.session_state.message = success_message
    st.session_state.level += 1
    st.session_state.sub_stage = 'main'
    st.rerun()

def trigger_plan_b(warning_message):
    """Drops the player into the backup question."""
    st.session_state.message = warning_message
    st.session_state.sub_stage = 'plan_b'
    st.rerun()

def fail_mission(fail_message):
    """Triggers the Game Over screen."""
    st.session_state.last_stage = st.session_state.stage
    st.session_state.last_level = st.session_state.level
    st.session_state.message = fail_message
    st.session_state.stage = 'game_over'
    st.rerun()

def path_complete(completion_message):
    """Triggers the victory screen."""
    st.session_state.message = completion_message
    st.session_state.stage = 'victory'
    st.rerun()

# ==========================================
# 2. MAIN MENU UI
# ==========================================
st.title("👁️ The Mind's Eye")
st.divider()

# Display any incoming messages (successes or warnings)
if st.session_state.message:
    st.info(st.session_state.message)
    st.session_state.message = ""

if st.session_state.stage == 'intro':
    st.write("*Rain beats against the window. The phone rings... You pick it up.*")
    st.write("**Mysterious Voice:** Listen closely. I need to know how your mind works.")
    st.write("**Which of these best describes your approach to solving a crisis?**")
    
    st.write("---")
    if st.button("🕵️‍♂️ The Investigator: Read people, find patterns, uncover the truth."):
        st.session_state.stage = 'investigator'
        st.session_state.level = 1
        st.rerun()
    if st.button("💻 The Tech Architect: Speak to machines, code logic, rebuild networks."):
        st.session_state.stage = 'tech'
        st.session_state.level = 1
        st.rerun()
    if st.button("🩺 The Doctor: Diagnose the unseen, triage under pressure, save lives."):
        st.session_state.stage = 'doctor'
        st.session_state.level = 1
        st.rerun()
    if st.button("🏛️ The Civil Servant: Manage disasters, allocate resources, lead cities."):
        st.session_state.stage = 'civil'
        st.session_state.level = 1
        st.rerun()

# ==========================================
# 3. PATH 1: THE INVESTIGATOR
# ==========================================
elif st.session_state.stage == 'investigator':
    st.subheader(f"Level {st.session_state.level}")
    
    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** Someone cleaned out the evidence locker.")
            st.write("- Alice: 'I didn't open that locker.'\n- Bob: 'Charlie opened it.'\n- Charlie: 'Bob is a liar.'")
            st.write("**Exactly ONE of them is telling the truth. Who did it?**")
            ans = st.text_input("Name the culprit (Alice, Bob, Charlie):").strip().lower()
            if st.button("Submit"):
                if ans == 'alice': advance_level("Detective Vance: She did it. Let's move.")
                else: trigger_plan_b("Detective Vance: Wait, she's making a run for it! Three cars speed out: Red, Blue, and Black. Red left before Blue. Black left before Red.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Which car left FIRST? (Red, Blue, Black):").strip().lower()
            if st.button("Submit"):
                if ans == 'black': advance_level("Detective Vance: The Black car! We boxed her in.")
                else: fail_mission("Detective Vance: We lost her.")

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** She's running a betting ring. Payouts: Match 1: 2k. Match 2: 4k. Match 3: 8k. Match 4: 16k.")
            ans = st.text_input("What is the payout for Match 5? (number only):").strip()
            if st.button("Submit"):
                if ans == '32': advance_level("Detective Vance: 32 grand. We intercepted the drop!")
                else: trigger_plan_b("Detective Vance: We missed it! The courier dropped an anagram for the backup spot: R D P O.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Unscramble the letters:").strip().upper()
            if st.button("Submit"):
                if ans == 'DROP': advance_level("Detective Vance: The DROP zone! We grabbed him.")
                else: fail_mission("Detective Vance: The trail went cold.")

    elif st.session_state.level == 3:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** Alice bought extreme thermal gear, snow chains, and a sub-zero sleeping bag.")
            ans = st.text_input("Where is she heading? (docks / city / mountains):").strip().lower()
            if 'mountain' in ans: advance_level("Detective Vance: The mountains. Brilliant deduction.")
            elif st.button("Submit"): trigger_plan_b("Detective Vance: Wrong! Train A goes to blizzards. Train B goes to the desert.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Which train do we board? (A or B):").strip().upper()
            if st.button("Submit"):
                if ans == 'A': advance_level("Detective Vance: We boarded Train A. We're close.")
                else: fail_mission("Detective Vance: Wrong train. She's gone.")

    elif st.session_state.level == 4:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** It's a trap! The room is flooding 1 foot per hour. There's a rope ladder hanging from a floating raft. 10 rungs, 1 foot apart.")
            ans = st.text_input("How many hours until the water covers the top rung? (number or 'never'):").strip().lower()
            if st.button("Submit"):
                if ans in ['never', '0']: advance_level("Detective Vance: Right! The raft floats. We climb it now!")
                else: trigger_plan_b("Detective Vance: The ladder floated up! Quick, bypass the door: A bat and a ball cost $1.10. The bat costs $1.00 MORE than the ball.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("How much does the ball cost? (Enter cents, e.g., 5 or 10):").strip()
            if st.button("Submit"):
                if ans == '5': advance_level("Detective Vance: 5 cents! The door opened!")
                else: fail_mission("Detective Vance: Wrong code! We're locked in.")

    elif st.session_state.level == 5:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** She's escaping in a jeep at 80 km/h with a 2-hour head start. Our chopper flies at 120 km/h.")
            ans = st.text_input("How many hours will it take to catch her? (number only):").strip()
            if st.button("Submit"):
                if ans == '4': path_complete("Detective Vance: 4 hours. We close the gap. We got her. Masterful work.")
                else: trigger_plan_b("Detective Vance: Math was off! My sniper scope needs a 3-digit code. They multiply to 36 and add to 13. Highest digit first.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("What is the code?").strip()
            if st.button("Submit"):
                if ans == '922': path_complete("Detective Vance: Code 922. Target disabled! You saved the case.")
                else: fail_mission("Detective Vance: Invalid code. She got away.")

# ==========================================
# 4. PATH 2: THE TECH ARCHITECT
# ==========================================
elif st.session_state.stage == 'tech':
    st.subheader(f"Level {st.session_state.level}")
    
    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Malware tripped the breaker.")
            st.write("- Alpha MUST boot before Gamma.\n- Do NOT boot Beta first.\n- Gamma MUST boot before Beta.")
            ans = st.text_input("Type the first letter of each server in order (e.g., A B G):").strip().upper().replace(" ", "")
            if st.button("Submit"):
                if ans == 'AGB': advance_level("Sarah: Alpha, Gamma, Beta. It worked!")
                else: trigger_plan_b("Sarah: Sequence shorted! Generator outputs exactly 150W. Load 1 is 50W. Load 2 is 100W.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Plug in Load 1, Load 2, or BOTH?").strip().upper()
            if st.button("Submit"):
                if ans == 'BOTH': advance_level("Sarah: Balanced! Generator humming.")
                else: fail_mission("Sarah: Generator caught fire!")

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Malware jumped to Port: 10, then 13, then 16, then 19.")
            ans = st.text_input("What port will it jump to next? (number):").strip()
            if st.button("Submit"):
                if ans == '22': advance_level("Sarah: Port 22! Firewall deployed.")
                else: trigger_plan_b("Sarah: Missed it! Override needed: 5, 10, 15, ?")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the missing number:").strip()
            if st.button("Submit"):
                if ans == '20': advance_level("Sarah: Override accepted!")
                else: fail_mission("Sarah: Drive corrupted.")

    elif st.session_state.level == 3:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Input A is active (True). Input B is dead (False). We need the output to be TRUE.")
            ans = st.text_input("Type AND or OR:").strip().upper()
            if st.button("Submit"):
                if ans == 'OR': advance_level("Sarah: OR gate bypassed the dead server!")
                else: trigger_plan_b("Sarah: AND gate failed! Manual override: 'Press RED, then press the color of the ocean.'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the two colors:").strip().upper()
            if st.button("Submit"):
                if ans == 'RED BLUE': advance_level("Sarah: Switch engaged.")
                else: fail_mission("Sarah: Wrong sequence! System dark.")

    elif st.session_state.level == 4:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Downloading a 1200 MB packet. 1st sec: 512 MB. 2nd: 256 MB. 3rd: 128 MB. It keeps halving infinitely.")
            ans = st.text_input("Will it EVER finish downloading the full 1200 MB? (Yes or No):").strip().lower()
            if st.button("Submit"):
                if ans == 'no': advance_level("Sarah: Right! It converges at 1024 MB. It will never reach 1200.")
                else: trigger_plan_b("Sarah: Logic bomb triggered! 5 servers take 5 minutes to wipe 5 caches.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("How many minutes for 100 servers to wipe 100 caches?").strip()
            if st.button("Submit"):
                if ans == '5': advance_level("Sarah: Right, 5 minutes! Parallel processing.")
                else: fail_mission("Sarah: Wrong calculation! OS deleted.")

    elif st.session_state.level == 5:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Total blackout. You have one match, a kerosene lamp, an oil heater, and a wax candle.")
            ans = st.text_input("What do you light FIRST? (match / lamp / heater / candle):").strip().lower()
            if st.button("Submit"):
                if ans == 'match': path_complete("Sarah: Yes! You have to light the match first. System secured!")
                else: trigger_plan_b("Sarah: You fumbled! Voice failsafe activated: 'I am an odd number. Take away a letter and I become even. What am I?'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Spell out the number:").strip().lower()
            if st.button("Submit"):
                if ans == 'seven': path_complete("Sarah: 'Seven'. Meltdown aborted. System secured!")
                else: fail_mission("Sarah: Core critical. Goodbye.")
                # ==========================================
# 5. PATH 3: THE DOCTOR
# ==========================================
elif st.session_state.stage == 'doctor':
    st.subheader(f"Level {st.session_state.level}")

    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Head Nurse:** Three patients!")
            st.write("- A: Screaming, broken arm.\n- B: Coughing violently.\n- C: Completely silent, breathing rapidly.")
            ans = st.text_input("Who goes to surgery first? (A, B, or C):").strip().upper()
            if st.button("Submit"):
                if ans == 'C': advance_level("Head Nurse: Good call. Silence in trauma means shock. Let's operate.")
                else: trigger_plan_b("Head Nurse: Patient C crashed! Mix a dopamine drip. 'Mix 2 parts saline to 1 part medicine.' You need 30ml total.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("How many ml of MEDICINE do you add? (number only):").strip()
            if st.button("Submit"):
                if ans == '10': advance_level("Head Nurse: 10ml medicine, 20ml saline. We got a pulse.")
                else: fail_mission("Head Nurse: Wrong dosage! The patient flatlined!")

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Head Nurse:** Titration schedule: Hour 1: 3 mg. Hour 2: 9 mg. Hour 3: 27 mg.")
            ans = st.text_input("Based on this multiplier, how many mg for Hour 4? (number only):").strip()
            if st.button("Submit"):
                if ans == '81': advance_level("Head Nurse: 81 mg. The fever is breaking.")
                else: trigger_plan_b("Head Nurse: Rejecting medication! Riddle for the antidote lockbox: 'What has a head, a tail, is brown, and has no legs?'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the word:").strip().lower()
            if st.button("Submit"):
                if ans in ['penny', 'coin']: advance_level("Head Nurse: A penny! The box opened.")
                else: fail_mission("Head Nurse: The box stays locked. Cardiac arrest.")

    elif st.session_state.level == 3:
        if st.session_state.sub_stage == 'main':
            st.write("**Head Nurse:** Family found unconscious. Skin is flushed 'cherry red'. Gas heater was running.")
            ans = st.text_input("What invisible gas poisoned them? (Type the name):").strip().lower()
            if st.button("Submit"):
                if 'carbon monoxide' in ans or ans == 'co': advance_level("Head Nurse: Carbon monoxide. Get them on 100% oxygen!")
                else: trigger_plan_b("Head Nurse: Wrong! Wait, one has a medical bracelet: 'ALLERGIC TO P C N L N I I I'.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Unscramble the antibiotic:").strip().lower()
            if st.button("Submit"):
                if ans == 'penicillin': advance_level("Head Nurse: Penicillin! Changing meds now.")
                else: fail_mission("Head Nurse: Wrong meds given. Anaphylactic shock!")

    elif st.session_state.level == 4:
        if st.session_state.sub_stage == 'main':
            st.write("**Head Nurse:** A boy and father in an accident. Father is in ICU. Surgeon looks at the boy and says, 'I cannot operate, he is my son.'")
            ans = st.text_input("If the father is in the ICU, who is the surgeon?").strip().lower()
            if st.button("Submit"):
                if 'mother' in ans or 'mom' in ans: advance_level("Head Nurse: The mother. Good focus.")
                else: trigger_plan_b("Head Nurse: You hesitated! Quick, some months have 31 days. Some have 30. How many have 28 days?")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the number:").strip()
            if st.button("Submit"):
                if ans == '12': advance_level("Head Nurse: All 12 of them! Defibrillator charging!")
                else: fail_mission("Head Nurse: Too slow. We lost him.")

    elif st.session_state.level == 5:
        if st.session_state.sub_stage == 'main':
            st.write("**Head Nurse:** Power failed! Ventilator dead. You have a flashlight, a manual Ambu bag, and a defibrillator.")
            ans = st.text_input("What do you reach for FIRST? (flashlight / bag / defibrillator):").strip().lower()
            if st.button("Submit"):
                if 'bag' in ans or 'ambu' in ans: path_complete("Head Nurse: Yes! Grab the bag and pump oxygen. You saved them!")
                else: trigger_plan_b("Head Nurse: Wrong item! CPR needed! 100 to 120 bpm. Which song rhythm?\n[A] Slow waltz\n[B] Disco (Stayin' Alive)\n[C] Heavy metal")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type A, B, or C:").strip().upper()
            if st.button("Submit"):
                if ans == 'B': path_complete("Head Nurse: Stayin' Alive! The perfect rhythm! Power is back!")
                else: fail_mission("Head Nurse: Rhythm was wrong. Heart stopped.")

# ==========================================
# 6. PATH 4: THE CIVIL SERVANT
# ==========================================
elif st.session_state.stage == 'civil':
    st.subheader(f"Level {st.session_state.level}")

    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Chief of Staff:** Cyclone hitting in 4 hours. Highway A is flooded. Highway B is blocked. Highway C is clear but leads to the eye of the storm.")
            ans = st.text_input("Which highway do you order buses through? (A, B, C, or None):").strip().upper()
            if st.button("Submit"):
                if ans == 'NONE': advance_level("Chief of Staff: Exactly. Shelter in Place order issued.")
                else: trigger_plan_b("Chief of Staff: Buses trapped! A relief truck is stuck under a bridge, 1 inch too tall.")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("What do you do to the truck? (1 word):").strip().lower()
            if st.button("Submit"):
                if 'tire' in ans or 'tyre' in ans or 'air' in ans: advance_level("Chief of Staff: Let the air out of the tires! It drove out.")
                else: fail_mission("Chief of Staff: Storm surge hit the convoy.")

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Chief of Staff:** Village flooded 40 km upstream. Boat travels 20 km/h upstream and 40 km/h downstream.")
            ans = st.text_input("How many hours for one full round trip? (number only):").strip()
            if st.button("Submit"):
                if ans == '3': advance_level("Chief of Staff: 3 hours. (2 up, 1 down).")
                else: trigger_plan_b("Chief of Staff: Timeline wrong! Scrambled text for what they need: R W T A E")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Unscramble the word:").strip().upper()
            if st.button("Submit"):
                if ans == 'WATER': advance_level("Chief of Staff: WATER! Dropping crates now.")
                else: fail_mission("Chief of Staff: Wrong supplies sent.")

    elif st.session_state.level == 3:
        if st.session_state.sub_stage == 'main':
            st.write("**Chief of Staff:** North village has hospital. East has food silo. West has heavy construction machinery.")
            ans = st.text_input("Which village do you clear a path to FIRST? (North, East, West):").strip().lower()
            if st.button("Submit"):
                if ans == 'west': advance_level("Chief of Staff: West! Secure machinery first to clear the rest.")
                else: trigger_plan_b("Chief of Staff: Protestors rioting. De-escalate with this riddle: 'What is as light as a feather, but even the strongest person can't hold it for 5 minutes?'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the word:").strip().lower()
            if st.button("Submit"):
                if 'breath' in ans: advance_level("Chief of Staff: Breath. The crowd calmed down.")
                else: fail_mission("Chief of Staff: Riot overran the center.")

    elif st.session_state.level == 4:
        if st.session_state.sub_stage == 'main':
            st.write("**Reporter:** 'A man builds a house. All four walls face South. A bear walks past. What color is the bear?'")
            ans = st.text_input("What color is the bear?").strip().lower()
            if st.button("Submit"):
                if 'white' in ans: advance_level("Chief of Staff: White! Because it's at the North Pole.")
                else: trigger_plan_b("Chief of Staff: Press laughed! Quick, follow-up math: 'If you divide 30 by half and add 10, what do you get?'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the number:").strip()
            if st.button("Submit"):
                if ans == '70': advance_level("Chief of Staff: 70! (30 / 0.5 + 10). Authority reclaimed.")
                else: fail_mission("Chief of Staff: PR disaster.")

    elif st.session_state.level == 5:
        if st.session_state.sub_stage == 'main':
            st.write("**Chief of Staff:** Dam is cracking! Digital lock needs the next Fibonacci number: 1, 1, 2, 3, 5, 8, ?")
            ans = st.text_input("What is the next number? (number only):").strip()
            if st.button("Submit"):
                if ans == '13': path_complete("Chief of Staff: Code 13 accepted! Spillways open! City saved!")
                else: trigger_plan_b("Chief of Staff: Wrong code! Biometric riddle: 'What belongs to you, but other people use it more than you do?'")
        elif st.session_state.sub_stage == 'plan_b':
            ans = st.text_input("Type the word:").strip().lower()
            if st.button("Submit"):
                if 'name' in ans: path_complete("Chief of Staff: Your name! Override accepted. You are a hero.")
                else: fail_mission("Chief of Staff: Override failed. The dam broke.")

# ==========================================
# 7. GAME OVER & VICTORY SCREENS
# ==========================================
elif st.session_state.stage == 'game_over':
    st.error("❌ CRITICAL FAILURE")
    st.write(st.session_state.message)
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏪ Rewind Timeline (Retry Level)"):
            st.session_state.stage = st.session_state.last_stage
            st.session_state.level = st.session_state.last_level
            st.session_state.sub_stage = 'main'
            st.session_state.message = "Timeline rewound. Try again."
            st.rerun()
    with col2:
        if st.button("🏠 Main Menu"):
            st.session_state.stage = 'intro'
            st.rerun()

elif st.session_state.stage == 'victory':
    st.success("🏆 PATH COMPLETE")
    st.write(st.session_state.message)
    st.balloons()
    if st.button("🏠 Play Another Path"):
        st.session_state.stage = 'intro'
        st.rerun()
        
