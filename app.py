from flask import Flask, render_template, request
import random

app = Flask(__name__)

pairs = {
    "Security sector reform (SSR)": "Providing security and maintaining public order to protect people, property and State institutions.",
    "Provision of a security umbrella": "Actions to gather information on whether an agreement to stop fighting is being respected.",
    "Mine action": "Helping end conflict or maintain peace through negotiations, dialogue, reconciliation and institution‑building.",
    "DDR (Disarmament, Demobilization, Reintegration)": "Removing weapons, disbanding armed groups and helping ex‑combatants return to civilian life.",
    "Monitoring and verification": "Ensuring that parties comply with ceasefires, peace agreements or political commitments.",
    "Political processes": "Supporting political dialogue, elections, constitutional processes and inclusive governance.",
    "Protection of civilians": "Preventing, deterring and responding to threats of physical violence against civilians.",
    "Human rights promotion": "Monitoring, reporting and supporting accountability for human rights violations.",
    "Rule of law support": "Strengthening justice institutions, police, courts and corrections.",
    "Ceasefire support": "Assisting parties in implementing and maintaining a cessation of hostilities.",
    "Electoral assistance": "Supporting credible, inclusive and transparent elections.",
    "Community engagement": "Building trust with local populations and supporting dialogue.",
    "Conflict prevention": "Identifying risks and taking action to prevent escalation.",
    "Early warning": "Collecting and analyzing information to anticipate threats.",
    "Capacity building": "Training and supporting national institutions to improve performance.",
    "Stabilization support": "Helping restore basic security and functioning governance after conflict."
}

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = list(pairs.keys())
    definitions = list(pairs.values())

    random.shuffle(tasks)
    random.shuffle(definitions)

    if request.method == "POST":
        user_matches = request.form.to_dict()
        score = sum(1 for t, d in user_matches.items() if pairs.get(t) == d)

        return render_template(
            "index.html",
            tasks=tasks,
            definitions=definitions,
            score=score,
            total=len(pairs),
            submitted=True,
            pairs=pairs,
            user_matches=user_matches
        )

    # GET request
    return render_template(
        "index.html",
        tasks=tasks,
        definitions=definitions,
        score=None,
        submitted=False,
        pairs=pairs,
        user_matches={}
    )

if __name__ == "__main__":
    app.run(debug=True)
