from workoutbot.workout import Exercise


# ========================================================================================================
# =============================================== LEGS ===================================================
# ========================================================================================================

legs_core = {
    "exercises": (
        Exercise(
            name="Kettlebell Front Squat",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/wRmiqpizfNM",
            description="""
Hold the kettlebell with your forearm as vertical as possible. Keep the wrist straight and kettlebell \
against the chest.

Squat as low as you can while keeping your head, spine, and pelvis aligned, and pushing your knees apart. \
Keep your torso as vertical as possible - you shouldn’t have to lean forward or work extra hard to hold \
the kettlebell upright. Avoid bending or twisting to either side.

Come back up, extending your hips and knees.
            """,
            difficulty="easy"
        ),  # Kettlebell Front Squat

        Exercise(
            name="Kettlebell Sumo Squat",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/sGNMEtZCkRY",
            description="""
Holding a kettlebell with both hands directly in front of your legs, plant both feet on the floor further than \
shoulder-width apart. Point both feet slightly outward.

Looking straight ahead, bend at both the hips and knees, ensuring that your knees remain in line with your toes. \
Continue bending your knees until your upper legs are parallel with the floor. Ensure that your back remains within \
a 45- and 90-degree angle to your hips.

Push through your heels and extend your legs to return to the starting position.
            """,
            difficulty="easy"
        ),  # Kettlebell Sumo Squat

        Exercise(
            name="Kettlebell Overhead Squat",
            reps=("5 х 8", "4 х 12", "10 min"),
            link="https://youtu.be/2FMyiuKswtA",
            description="""
Hold a kettlebell in your hand and extend your arm so it's directly above your head, with your legs shoulder-width \
apart. Bend your knees and lower yourself into a squat, keeping the kettlebell extended. Use your other arm to \
balance, then return to starting position and repeat.
            """,
            difficulty="medium"),  # Kettlebell Overhead Squat

        Exercise(
            name="Kettlebell Hack Squat",
            reps=("4 х 8", "5 x 5", "3 x 10"),
            link="https://youtu.be/G9r6YEytKTI",
            description="""
Take a position with the feet closer together and toes pointed out at 45 degrees. The kettlebell is held at arm's \
length, behind the back, and shoulders are drawn back. Keep the shoulders down and away from the ears. There should \
be a normal, not exaggerated curve in your lower back. The torso remains vertical. If the need to lean forward \
overcomes you, face a wall so it will be impossible.

The knees move forward, tracking past the toes, the heels come off the ground. Focus hard on keeping your balance. \
Allow the kettlebell to open the chest and maintain tension in the calves.

In the bottom position, smoothly reverse the direction. You should focus on creating a stretch in the area of the \
hamstring/buttocks area. This will improve over time when you access more coordination and skill. Maintain a good \
posture at the top and squeeze your quadriceps and glutes. 
            """,
            difficulty="hard"
        ),  # Kettlebell Hack Squat

        Exercise(
            name="Pistol Squat",
            reps=("5 х 8", "4 х 10", "10 min", "1 х MAX"),
            link="https://youtu.be/R1mxpLzYgxM",
            description="""
Start standing with feet shoulder-width apart. Keep your chest high and eyes forward, pull your shoulders back and \
engage your core.

Extend arms and one leg out in front of you. Then, bend one knee, and hinge at your hips and bend your knee to lower \
into a squat. Continue to lower, keeping your back straight and torso as upright as possible. 

The goal is to bring your butt as close to your heel as you possibly can. Then, squeeze your glutes and drive through \
your heel to stand back up.
            """,
            difficulty="hard"
        ),  # Pistol Squat

        Exercise(
            name="Bronson / Isometric Squat",
            reps=("2 х 10", "3 х 8", "10 min", "1 х MAX"),
            link="https://youtu.be/sUR7EGNDOoc",
            description="""
Isometric squat from Charles Bronson's «Solitary Fitness» book:

Stand with your feet roughly shoulder-width apart, angled out slightly. 

Push your hips back and lower yourself into a full squat position, with your legs at 90 degrees. Hold the bottom \
position for 10 seconds and then go all the way down. 

After that, return to the full squat position in which your legs at 90 degrees. Hold it there for another 10 seconds \
and then go all the way up, pushing your hips through to the full extension.
            """,
            difficulty="hard"
        ),  # Bronson Squat

        Exercise(
            name="Bottoms Up Kettlebell Goblet Squat",
            reps=("5 х 8", "4 х 12", "10 min", "1 x MAX"),
            link="https://youtu.be/4yvHkqU_hBQ",
            description="""
Flip the kettlebell upside down so the heavy portion sits above the handle and the horn sits on the meat of your palm. \
Holding the kettlebell at the chest level, set your feet in a squat stance, so that the heels are at hip-width or \
slightly wider.

To squat, sit the hips down over the heels. As you descend, be sure to support the weight so that it stays above your \
chest line.  

At the bottom of the squat pause, and contract your back muscles to raise your chest high with the weight at that \
level. When standing up, you need to actively lift the chest and the weight so that the kettlebell stays slightly \
higher than chest height. It is imperative that the hips do not shoot backward.
            """,
            difficulty="easy"
        ),  # Bottoms Up Kettlebell Goblet Squat

        Exercise(
            name="Lunges",
            reps=("5 х 8", "4 х 12", "10 min"),
            link="https://youtu.be/3XDriUn0udo",
            description="\nChoose any variation you like.",
            difficulty="medium"
        ),  # Lunges

        Exercise(
            name="Step-Ups",
            reps=("5 х 8", "4 х 12", "10 min"),
            link="https://youtu.be/1hiWQ7pehjQ",
            description="""
Place your entire right foot onto the bench or chair. Press through your right heel as you step onto the bench, \
bringing your left foot to meet your right so you are standing on the bench.

Return to the starting position by stepping down with the right foot, then the left so both feet are on the floor.

Complete the reps leading with the right foot, and then do the same amount leading with your left foot.
            """,
            difficulty="easy"
        )  # Step-Ups
    ),

    "explosive": (
        Exercise(
            name="Star Jumps",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/h6wu4_LOhyU"
        ),  # Star Jumps
        Exercise(
            name="Squat Thrusts",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/fysU2ldlXSY"
        ),  # Squat Thrusts
        Exercise(
            name="Burpee",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/auBLPXO8Fww"
        )  # Burpee
    ),

    "additional": (
        Exercise(
            name="Sit-Ups",
            reps=("100",),
            link="https://youtu.be/jDwoBqPH0jk"
        ),  # Sit-Ups
        Exercise(
            name="Leg Raises",
            reps=("50",),
            link="https://youtu.be/l4kQd9eWclE"
        ),  # Leg Raises
        Exercise(
            name="Plank",
            reps=("1 х MAX", "5 min total"),
            link="https://youtu.be/F-nQ_KJgfCY"
        )  # Plank
    )
}


# ========================================================================================================
# ============================================== CHEST ===================================================
# ========================================================================================================

chest_core = {
    "exercises": (
        Exercise(
            name="Push-Ups",
            reps=("10 min", "1 х MAX"),
            link="https://youtu.be/IODxDxX7oi4",
            description="""
Get on the floor on all fours, positioning your hands slightly wider than your shoulders. Extend your legs back so \
that you are balanced on your hands and toes. Keep your body in a straight line from head to toe without sagging in \
the middle or arching your back. Position your feet to be close together.

Contract your abs and tighten your core by pulling your belly button toward your spine. Keep a tight core throughout \
the entire pushup. Inhale as you slowly bend your elbows and lower yourself until your chest touches the ground.

Exhale as you begin contracting your chest muscles and pushing back up through your hands to the start position. \
Don't lock out the elbows - keep them slightly bent.
            """,
            difficulty="easy"
        ),  # Push-Ups

        Exercise(
            name="Dips",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/2z8JmcrW-As",
            description="""
Grasp the parallel bars and hop up so your arms are straight. Lean forward at about a 45-degree angle. Pull your \
shoulders down and back. Maintain this body position throughout the exercise.

Slowly bend your elbows to lower your body into the Dip until your upper arms are about parallel to the ground. Keep \
your elbows tight to your body.

Straighten your arms to drive your body up to the starting position.
            """,
            difficulty="medium"
        ),  # Dips

        Exercise(
            name="Kettlebell Press",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/WTmR-Qr32dg",
            description="""
Start with the kettlebell in the rack position (the end position of a clean).

Make sure your elbow is tucked into your chest, then press the weight directly up overhead.

Lower the weight by reversing the bell path and repeat the move.
            """,
            difficulty="easy"
        ),  # Kettlebell Press

        Exercise(
            name="Kettlebell Seesaw Press",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/55-ngw6hplo",
            description="""
Using the clean motion, bring two kettlebells to shoulder level.

One of the kettlebells should then be moved overhead by extending your arm through the elbow. Make sure to turn your \
wrist so that your palm is in a forward-facing position. The other kettlebell should be held in place on your shoulder.

The kettlebell that has been pressed should be returned to shoulder level but, upon the way down, the other \
kettlebell should be pressed.
            """,
            difficulty="medium"
        ),  # Kettlebell Seesaw Press

        Exercise(
            name="Kettlebell Clean & Press",
            reps=("5 х 8", "4 х 12", "10 min", "1 х MAX"),
            link="https://youtu.be/sAtZ4yAsQnI",
            description="""
In a standing position with feet hip/shoulder-width apart, position the kettlebell between the feet. Engage the core \
and set the shoulders and bend down to grab the kettlebell. 

Straighten the legs as you lift the kettlebell upwards. When the kettlebell is just above knee level, drive the hips \
quickly forwards and upwards. Simultaneously pull the shoulders back and clean the kettlebell to the rack position \
(front of shoulder). Regain your balance/foot position before pressing the kettlebell overhead. Return the kettlebell \
to the rack position (under control) and gently lower it to the ground.

Repeat for reps or time before switching sides.
            """,
            difficulty="medium"
        )  # Kettlebell Clean & Press
    ),

    "explosive": (
        Exercise(
            name="Jumping Push-Ups",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/VzqjWuarzZQ"
        ),  # Jumping Push-Ups
        Exercise(
            name="Clapping Push-Ups",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/EYwWCgM198U"
        ),  # Clapping Push-Ups
        Exercise(
            name="Kettlebell Push Press",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/CCqru4q9RK0"
        )  # Kettlebell Push Press
    ),

    "additional": None
}


# ========================================================================================================
# =============================================== BACK ===================================================
# ========================================================================================================

back_core = {
    "exercises": (
        Exercise(
            name="Pull-Ups",
            reps=("5 х 8", "4 х 12", "10 min"),
            link="https://youtu.be/XB_7En-zf_M",
            description="""
Reach up and grab the bar with each hand. Your grip should be wider than your shoulders.

When positioned correctly, your arms and torso should form a 'Y' - each arm should be 30 to 45 degrees from your \
body, but no more than a 45-degree angle.

Look straight ahead and pull your body upwards towards the bar. The movement is done mostly with your back. To ensure \
that, try to focus on bringing your elbows towards your sides when pulling.
            """,
            difficulty="medium"
        ),  # Pull ups

        Exercise(
            name="Kettlebell Swing",
            reps=("10 min", "1 х MAX"),
            link="https://youtu.be/YSxHifyI6s8",
            description="""
Start with the kettlebell on the floor slightly in front of you and between your feet, which should be shoulder-width \
apart. 

Bending slightly at the knees but hingeing mainly at the hips, grasp the kettlebell and pull it back between your legs \
to create momentum. Drive your hips forwards and straighten your back to send the kettlebell up to shoulder height. 

Let the bell return back between your legs and repeat the move.
            """,
            difficulty="easy"
        ),  # Kettlebell Swing

        Exercise(
            name="Kettlebell Row",
            reps=("5 х 8", "4 х 12", "10 min"),
            link="https://youtu.be/3scGFjVtftw",
            description="\nChoose any variation you like.",
            difficulty="easy"
        ),  # Kettlebell Row

        Exercise(
            name="Kettlebell Clean",
            reps=("10 min", "1 х MAX"),
            link="https://youtu.be/C0B1SrcGAIA",
            description="""
Start as if you were going to perform a one-arm kettlebell swing. All the points that apply to the swing also apply to \
the clean, minus the straight-arm requirement. The arms must stay loose, and the hips must do all the work of driving \
the kettlebell upward. Avoid the tendency to curl the KB.

The kettlebell should travel the shortest distance possible, following a vertical path, rather than an arc. Pull the \
kettlebell into the body at shoulder height, allowing it to “roll” over onto the forearm on both the negative and on \
the positive. Do not allow the kettlebell to flip up and “crash” on your forearm. The KB, the elbow, and the torso \
must become one solid unit at the top of the clean. The shoulder must be pressed down, armpit squeezed tightly, \
triceps resting on the ribcage, and kettlebell resting between the forearm and the biceps, almost in the crook of \
the elbow.

Upon lockout, as the kettlebell lands on your forearm and upper arm, immediately tighten the abs and let out a little \
bit of air. Keep the wrists straight and neutral; no flexion!
            """,
            difficulty="easy"
        ),  # Kettlebell Clean

        Exercise(
            name="Turkish Get-Ups",
            reps=("10 min", "1 х MAX"),
            link="https://youtu.be/0bWRPC49-KI",
            description="""
A complex, full-body exercise that emphasizes balance, coordination, core strength, and stability, as well as overall \
body tension. 

Review the technique carefully before performing. Start with small weights.
            """,
            difficulty="hard")  # Turkish Get-Ups
    ),

    "explosive": (
        Exercise(
            name="Kettlebell Snatch",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/6l2Iu26oWW8"
        ),  # Kettlebell Snatch
        Exercise(
            name="Kettlebell Dead Snatch",
            reps=("2 х 15", "3 х 10", "1 min"),
            link="https://youtu.be/QuJ3mncWV1M"
        ),  # Kettlebell Dead Snatch
        Exercise(
            name="Explosive Pull-Ups",
            reps=("2 х 5", "3 х 4", "1 min")
        )  # Explosive Pull-Ups
    ),

    "additional": (

        Exercise(
            name="Floor Hyperextension",
            reps=("100",),
            link="https://youtu.be/AOaj0rAZ8iA"
        ),  # Floor Hyperextension
        Exercise(
            name="Quadraped",
            reps=("100",),
            link="https://youtu.be/fjztCWxOYZw"
        )  # Quadraped
    )
}


cardio_core = (
    "Running in Place",
    "Jump Rope",
    "Jumping Jacks",
    "Shadow Boxing"
)
