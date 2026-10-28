import streamlit as st
from datetime import date

st.set_page_config(
    page_title="FlatMate Food",
    page_icon="🥕",
    layout="wide"
)

st.title("🥕 FlatMate Food")
st.subheader("Your shared kitchen, less food waste!")
st.write(
    "Track shared ingredients, discover affordable student recipes, "
    "and make the most of the food you already have."
)

# -------------------------
# SHARED KITCHEN STOCK
# -------------------------

st.divider()
st.header("🧊 Shared Kitchen Stock")
st.write("Add ingredients currently available in your shared kitchen.")

if "ingredients" not in st.session_state:
    st.session_state.ingredients = []

with st.form("ingredient_form", clear_on_submit=True):
    ingredient = st.text_input(
        "Ingredient name",
        placeholder="e.g. Tomatoes"
    )

    location = st.selectbox(
        "Storage location",
        ["Fridge", "Pantry", "Freezer"]
    )

    quantity = st.text_input(
        "Quantity (optional)",
        placeholder="e.g. 4 pieces, 500 g"
    )

    use_by = st.date_input(
        "Use-by date (optional)",
        value=None
    )

    submitted = st.form_submit_button("Add ingredient")

if submitted:
    if ingredient.strip():
        st.session_state.ingredients.append({
            "name": ingredient.strip(),
            "location": location,
            "quantity": quantity.strip(),
            "use_by": use_by
        })
        st.success(f"{ingredient.strip()} added to your kitchen stock!")
    else:
        st.warning("Please enter an ingredient name.")

st.subheader("Current Stock")

if st.session_state.ingredients:
    for i, item in enumerate(st.session_state.ingredients):
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(f"**{item['name']}**")
                st.caption(
                    f"{item['location']} · "
                    f"{item['quantity'] or 'Quantity not specified'}"
                )

                if item["use_by"] is not None:
                    st.caption(f"Use-by date: {item['use_by']}")

            with col2:
                if st.button("Remove", key=f"remove_{i}"):
                    st.session_state.ingredients.pop(i)
                    st.rerun()
else:
    st.info("Your kitchen stock is empty. Add your first ingredient above.")

# -------------------------
# RECIPES
# -------------------------

RECIPES = [
    {
        "name": "Tomato Pasta",
        "description": "A simple, filling pasta dish.",
        "equipment": "Stovetop",
        "ingredients": ["pasta", "tomato", "onion", "oil"],
        "instructions": [
            "Boil the pasta in a pot of water.",
            "Meanwhile, chop the onion and tomato.",
            "Cook the onion in a little oil in a pan.",
            "Add the tomato and cook until softened.",
            "Mix with the drained pasta and serve."
        ],
        "time": 20,
        "vegetarian": True
    },
    {
        "name": "Egg Fried Rice",
        "description": "A great way to use leftover rice and vegetables.",
        "equipment": "Stovetop",
        "ingredients": ["rice", "egg", "onion", "oil"],
        "instructions": [
            "Cook the rice if you do not already have cooked rice.",
            "Beat the eggs in a bowl.",
            "Cook the onion in a little oil in a frying pan.",
            "Add the eggs and stir until cooked.",
            "Add the rice and stir-fry everything together."
        ],
        "time": 20,
        "vegetarian": True
    },
    {
        "name": "Chickpea Curry",
        "description": "An inexpensive, filling meal using pantry staples.",
        "equipment": "Stovetop",
        "ingredients": ["chickpeas", "tomato", "onion", "curry powder", "oil"],
        "instructions": [
            "Chop the onion.",
            "Cook it in a little oil in a pot or deep pan.",
            "Add the tomato, chickpeas and curry powder.",
            "Simmer for 10–15 minutes, adding a little water if needed.",
            "Serve on its own or with rice if available."
        ],
        "time": 25,
        "vegetarian": True
    },
    {
        "name": "Cheese Omelette",
        "description": "A quick meal with just a few ingredients.",
        "equipment": "Stovetop",
        "ingredients": ["egg", "cheese", "oil"],
        "instructions": [
            "Beat the eggs in a bowl.",
            "Heat a little oil in a frying pan.",
            "Pour in the eggs and cook over medium-low heat.",
            "Add the cheese, fold the omelette and cook until set."
        ],
        "time": 10,
        "vegetarian": True
    },
    {
        "name": "Roasted Vegetable Tray",
        "description": "A flexible recipe for vegetables that need using up.",
        "equipment": "Oven",
        "ingredients": ["potato", "carrot", "onion", "oil"],
        "instructions": [
            "Preheat the oven to 200°C.",
            "Chop the vegetables into similar-sized pieces.",
            "Toss with oil and seasonings.",
            "Roast for 30–40 minutes, until tender and cooked through."
        ],
        "time": 45,
        "vegetarian": True
    },
    {
        "name": "Lentil Tomato Soup",
        "description": "A budget-friendly, hearty soup.",
        "equipment": "Stovetop",
        "ingredients": ["lentils", "tomato", "onion", "carrot", "oil"],
        "instructions": [
            "Chop the onion and carrot.",
            "Cook them in a little oil in a pot.",
            "Add lentils, tomato and water according to the lentil package.",
            "Simmer until the lentils are tender, adding water if needed.",
            "Check seasoning and serve."
        ],
        "time": 35,
        "vegetarian": True
    },
    {
        "name": "Greek Salad",
        "description": "A fresh, quick salad with crisp veggies and cheese.",
        "equipment": "No-cook",
        "ingredients": ["tomato", "cucumber", "onion", "cheese", "oil"],
        "instructions": [
            "Dice the tomato and cucumber.",
            "Thinly slice the onion.",
            "Crumble or cube the cheese.",
            "Toss everything in a bowl with oil, salt, and pepper."
        ],
        "time": 10,
        "vegetarian": True
    },
    {
        "name": "Chickpea & Tuna Salad",
        "description": "A high-protein, budget-friendly pantry salad.",
        "equipment": "No-cook",
        "ingredients": ["chickpeas", "tuna", "onion", "oil"],
        "instructions": [
            "Drain and rinse the chickpeas.",
            "Drain the canned tuna.",
            "Finely chop the onion.",
            "Mix all ingredients in a bowl with oil, salt, and pepper."
        ],
        "time": 5,
        "vegetarian": False
    },
    {
        "name": "Microwave Mug Mac & Cheese",
        "description": "Single-serve comfort food cooked directly in a mug.",
        "equipment": "Microwave",
        "ingredients": ["pasta", "water", "milk", "cheese"],
        "instructions": [
            "In a large microwave-safe mug, combine pasta and water.",
            "Microwave for 3–4 minutes, stirring halfway, until pasta is tender.",
            "Splash in a little milk and stir in grated cheese until melted."
        ],
        "time": 5,
        "vegetarian": True
    },
    {
        "name": "Microwave Jacket Potato",
        "description": "A quick cooked potato topped with melted cheese.",
        "equipment": "Microwave",
        "ingredients": ["potato", "cheese", "butter"],
        "instructions": [
            "Prick the potato several times with a fork.",
            "Microwave on high for 7–10 minutes until soft, flipping halfway.",
            "Cut open, add butter, and top with grated cheese."
        ],
        "time": 10,
        "vegetarian": True
    }
]

st.divider()
st.header("🍳 Recipe Finder")
st.write(
    "Find affordable student meals that match your ingredients "
    "and available cooking equipment."
)


equipment_options = [
    "Stovetop",
    "Oven",
    "Microwave",
    "No-cook"
]

available_equipment = st.multiselect(
    "Which cooking equipment do you have?",
    options=equipment_options,
    default=["Stovetop"]
)

if not available_equipment:
    st.info("No equipment selected: showing no-cook recipes by default.")
    matching_recipes = [
        recipe for recipe in RECIPES
        if recipe["equipment"] == "No-cook"
    ]
else:
    matching_recipes = [
        recipe for recipe in RECIPES
        if recipe["equipment"] in available_equipment
    ]


stock_names = {
    item["name"].strip().lower()
    for item in st.session_state.ingredients
}


if matching_recipes:
    st.subheader("Choose recipes for your shopping list")

    if "selected_recipes" not in st.session_state:
        st.session_state.selected_recipes = []

    stock_names = [
        item["name"].strip().lower()
        for item in st.session_state.ingredients
    ]

    shopping_items = set()

    for recipe in matching_recipes:
        recipe_ingredients = recipe["ingredients"]

        available = [
            name for name in recipe_ingredients
            if name.lower() in stock_names
            or any(
                name.lower() in stock_name
                or stock_name in name.lower()
                for stock_name in stock_names
            )
        ]

        missing = [
            name for name in recipe_ingredients
            if name not in available
        ]

        with st.container(border=True):
            st.subheader(recipe["name"])
            st.write(recipe["description"])

            st.caption(
                f"⏱️ About {recipe['time']} minutes · "
                f"Equipment: {recipe['equipment']}"
            )

            st.write(
                "**Ingredients:** "
                + ", ".join(recipe_ingredients)
            )

            if available:
                st.write(
                    "**Already in your stock:** "
                    + ", ".join(available)
                )

            if missing:
                st.write(
                    "**You may need to buy:** "
                    + ", ".join(missing)
                )
            else:
                st.success(
                    "You appear to have all listed ingredients!"
                )

            selected = st.checkbox(
                "Add to shopping list",
                key=f"select_{recipe['name']}"
            )

            if selected:
                st.session_state.selected_recipes.append(
                    recipe["name"]
                )

            with st.expander("View cooking instructions"):
                for step, instruction in enumerate(
                    recipe["instructions"], start=1
                ):
                    st.write(f"{step}. {instruction}")

    st.divider()
    st.header("🛒 Shopping List")

    selected_recipe_names = {
        recipe["name"]
        for recipe in matching_recipes
        if st.session_state.get(f"select_{recipe['name']}", False)
    }

    for recipe in matching_recipes:
        if recipe["name"] not in selected_recipe_names:
            continue

        for ingredient in recipe["ingredients"]:
            in_stock = (
                ingredient.lower() in stock_names
                or any(
                    ingredient.lower() in stock_name
                    or stock_name in ingredient.lower()
                    for stock_name in stock_names
                )
            )

            if not in_stock:
                shopping_items.add(ingredient)

    if shopping_items:
        for ingredient in sorted(shopping_items):
            st.checkbox(
                ingredient.capitalize(),
                key=f"shopping_{ingredient}"
            )
    elif selected_recipe_names:
        st.success("You already have all ingredients for your selected recipes!")
    else:
        st.info("Select one or more recipes to generate your shopping list.")

else:
    st.info("No recipes match the equipment selected. Try another option.")

# --- AI Recipe Suggestions ---
import os
from openai import OpenAI

st.divider()
st.header("🤖 AI Recipe Suggestions")

st.write(
    "Discover recipe ideas based on your kitchen stock "
    "and selected cooking equipment."
)

if st.button("Generate AI recipe suggestions"):
    api_key = os.getenv("GROQ_API_KEY")

try:
    api_key = st.secrets.get("GROQ_API_KEY", api_key)
except Exception:
    pass

    api_key = os.getenv("GROQ_API_KEY")
    try:
            api_key = st.secrets.get("GROQ_API_KEY", api_key)
    except Exception:
            pass

    if not api_key:
            st.error("Groq API key not found. Please check your app secrets.")
    elif not st.session_state.ingredients:
            st.warning("Add some ingredients to your kitchen stock first.")
    else:
            stock_list = [
                item["name"] for item in st.session_state.ingredients
            ]
            equipment_list = (
                available_equipment if available_equipment
                else ["No-cook"]
            )

    prompt = f"""
You are the recipe assistant for FlatMate Food,
an app designed to reduce food waste in shared kitchens.

Suggest 3 practical, student-friendly recipes.

Available ingredients in the kitchen:
{stock_list}

Available cooking equipment:
{equipment_list}

Rules:
- Prefer ingredients already available in the kitchen.
- You may list a few additional ingredients if needed.
- Only suggest recipes compatible with the available equipment.
- If the equipment list is No-cook, suggest recipes requiring no cooking.
- Give each recipe a name, ingredients, preparation time,
  equipment required, and clear step-by-step instructions.
- Do not include prices or cost estimates.
- Do not claim ingredients are available unless they are in the stock list.
- Keep the answer clear and concise.
"""

    try:
            with st.spinner("Generating recipe ideas..."):
                client = OpenAI(
                    api_key=api_key,
                    base_url="https://api.groq.com/openai/v1"
                )

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are the AI recipe assistant for FlatMate Food. "
                                "Help users reduce food waste with practical recipes."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                st.markdown(response.choices[0].message.content)

    except Exception as e:
            st.error(f"AI API error: {type(e).__name__}")
            st.code(str(e))
            print(f"Groq API error: {type(e).__name__}: {e}")