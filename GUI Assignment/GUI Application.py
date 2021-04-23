from tkinter import *
from tkinter.messagebox import *
from tkinter.font import Font


def load_images():
    global food_image_list

    crepes_photo = PhotoImage(file="crepes.png")
    chicken_photo = PhotoImage(file="chicken.png")
    salmon_photo = PhotoImage(file="salmon.png")
    frenchtoast_photo = PhotoImage(file="frenchtoast.png")

    food_image_list = [crepes_photo, chicken_photo, salmon_photo, frenchtoast_photo]


def create_profile_and_grid():
    create_profile()
    grid_rest_of_widgets()


def create_profile():
    global max_calories
    global max_protein
    global max_carbs
    global max_fat


    gender = genderVar.get()
    height = heightVar.get()
    weight = weightVar.get()
    fitnessGoal = goalVar.get()

    max_calories = 0
    max_protein = 0
    max_carbs = 0
    max_fat = 0

    if gender == 1:
        max_calories = int((-25.178 + (13.397 * weight) + (4.799 * height)) * 1.4)
    elif gender == 2:
        max_calories = int((360.993 + (9.247 * weight) + (3.098 * height)) * 1.4)
    else:
        max_calories = int((360.993 + (9.247 * weight) + (3.098 * height)) * 1.4) + 100

    if fitnessGoal == "Lose Weight":
        max_calories -= 300
    elif fitnessGoal == "Gain Weight":
        max_calories += 300
    else:
        max_protein = 30

    max_protein += max_calories//16
    max_carbs = max_calories//8
    max_fat = max_calories//36


def grid_rest_of_widgets():
    macroScale.config(from_=max_calories, tickinterval=max_calories)

    createProfileButton.config(state=DISABLED)

    foodOptionsListbox.grid(row=5, rowspan=8, column=1, )
    foodOptionsLabel.grid(row=4, column=1)

    addFoodOptionButton.grid(row=13, column=1, pady=15, ipadx=15, ipady=5)

    calorieLabel.grid(row=5, column=2)
    calorieEntry.grid(row=6, column=2, pady=(0, 5))
    proteinLabel.grid(row=7, column=2)
    proteinEntry.grid(row=8, column=2, pady=(0, 5))
    carbsLabel.grid(row=9, column=2)
    carbsEntry.grid(row=10, column=2, pady=(0, 5))
    fatLabel.grid(row=11, column=2)
    fatEntry.grid(row=12, column=2)

    userFoodLabel.grid(row=4, column=3)
    userFoodListbox.grid(row=5, rowspan=8, column=3)

    removeFoodOptionButton.grid(row=13, column=3, pady=15, ipadx=10, ipady=5)

    macroScale.grid(row=5, rowspan=9, column=4, columnspan=2, pady=15)

    macroSpinbox.grid(row=4, column=4)

    macroChangeButton.grid(row=4, column=5, padx=5, ipadx=2)

    resetButton.grid(row=9, rowspan=2, column=6, columnspan=2, padx=20, pady=15, ipadx=30, ipady=5)
    resetAllButton.grid(row=11, rowspan=2, column=6, columnspan=2, padx=20, pady=15, ipadx=10, ipady=5)

    recipeTitleLabel.grid(row=1, column=6, columnspan=2, sticky=S)
    recipeFrame.grid(row=2, rowspan=5, column=6, columnspan=2, padx=20, pady=5, sticky=N)
    recipeLabel.grid(row=1, column=1, ipadx=6, ipady=5)
    recipeImageLabel.grid(row=2, column=1)

    recipeSwitchButton.grid(row=2, rowspan=2, column=4, columnspan=2, sticky=E)

    titleLabel.grid(row=1, column=3)


def add_user_food_and_change_scale():
    add_user_food()
    change_macro_scale()


def add_user_food():
    global userFoodList
    
    index = foodOptionsListbox.curselection()[0]
    food = foodOptionsList[index]
    calories = foodMacrosList[index][0]
    protein = foodMacrosList[index][1]
    carbs = foodMacrosList[index][2]
    fat = foodMacrosList[index][3]

    calorieVar.set(calories)
    proteinVar.set(protein)
    carbsVar.set(carbs)
    fatVar.set(fat)

    userFoodList.append(food)
    userFoodVar.set(userFoodList)

    totalCaloriesVar.set(totalCaloriesVar.get() + calories)
    totalProteinVar.set(totalProteinVar.get() + protein)
    totalCarbsVar.set(totalCarbsVar.get() + carbs)
    totalFatVar.set(totalFatVar.get() + fat)


def change_macro_scale():
    global max_calories
    global max_protein
    global max_carbs
    global max_fat

    macro = macroOptionVar.get()

    if macro == "Calories":
        macroScale.config(from_=max_calories, tickinterval=max_calories, variable=totalCaloriesVar, label="Calories",
                          troughcolor="#ffde5b")
        macroSpinbox.config(bg="#ffde5b")

    elif macro == "Protein":
        macroScale.config(from_=max_protein, tickinterval=max_protein, variable=totalProteinVar, label="Protein (g)",
                          troughcolor="#f1948a")
        macroSpinbox.config(bg="#f1948a")

    elif macro == "Carbohydrates":
        macroScale.config(from_=max_carbs, tickinterval=max_carbs, variable=totalCarbsVar, label="Carbohydrates (g)",
                          troughcolor="#f8c471")
        macroSpinbox.config(bg="#f8c471")

    else:
        macroScale.config(from_=max_fat, tickinterval=max_fat, variable=totalFatVar, label="Fat (g)",
                          troughcolor="#af601a")
        macroSpinbox.config(bg="#af601a")


def remove_food_and_reset_macro_entries():
    remove_user_food()
    reset_macro_entries()


def remove_user_food():
    global userFoodList
    
    index = userFoodListbox.curselection()[0]

    food_index = foodOptionsList.index(userFoodList[index])
    
    totalCaloriesVar.set(totalCaloriesVar.get() - foodMacrosList[food_index][0])
    totalProteinVar.set(totalProteinVar.get() - foodMacrosList[food_index][1])
    totalCarbsVar.set(totalCarbsVar.get() - foodMacrosList[food_index][2])
    totalFatVar.set(totalFatVar.get() - foodMacrosList[food_index][3])
    
    userFoodList.pop(index)
    userFoodVar.set(userFoodList)


def reset_macro_entries():
    calorieVar.set(0)
    proteinVar.set(0)
    carbsVar.set(0)
    fatVar.set(0)


def reset():
    global userFoodList

    check = askquestion("Reset", "Are you sure you want to reset your foods list and your macro scale? Your profile will not be changed.")
    if check == "yes":
        userFoodList = []
        userFoodVar.set(userFoodList)
    
        totalCaloriesVar.set(0)
        totalProteinVar.set(0)
        totalCarbsVar.set(0)
        totalFatVar.set(0)
    
        calorieVar.set(0)
        proteinVar.set(0)
        carbsVar.set(0)
        fatVar.set(0)
    
    else:
        pass
    

def reset_all():
    global max_calories
    global max_protein
    global max_carbs
    global max_fat
    global userFoodList
    
    check = askquestion("Reset All", "Are you sure you want to reset everything, including your profile?")
    if check == "yes":

        userFoodList = []
        userFoodVar.set(userFoodList)

        totalCaloriesVar.set(0)
        totalProteinVar.set(0)
        totalCarbsVar.set(0)
        totalFatVar.set(0)

        calorieVar.set(0)
        proteinVar.set(0)
        carbsVar.set(0)
        fatVar.set(0)
        
        genderVar.set(None)
        heightVar.set(0)
        weightVar.set(0)
        goalVar.set("Select Your Fitness Goal")
    
        max_calories = 0
        max_protein = 0
        max_carbs = 0
        max_fat = 0

        change_macro_scale()
        ungrid_widgets()
        
    else:
        pass
    

def ungrid_widgets():
    
    createProfileButton.config(state=NORMAL)

    foodOptionsListbox.grid_remove()
    foodOptionsLabel.grid_remove()

    addFoodOptionButton.grid_remove()

    calorieLabel.grid_remove()
    calorieEntry.grid_remove()
    proteinLabel.grid_remove()
    proteinEntry.grid_remove()
    carbsLabel.grid_remove()
    carbsEntry.grid_remove()
    fatLabel.grid_remove()
    fatEntry.grid_remove()

    userFoodLabel.grid_remove()
    userFoodListbox.grid_remove()

    removeFoodOptionButton.grid_remove()

    macroScale.grid_remove()

    macroSpinbox.grid_remove()

    macroChangeButton.grid_remove()

    resetButton.grid_remove()
    resetAllButton.grid_remove()

    recipeTitleLabel.grid_remove()
    recipeFrame.grid_remove()
    recipeLabel.grid_remove()
    recipeImageLabel.grid_remove()

    recipeSwitchButton.grid_remove()
    
    titleLabel.grid(row=1, column=2)


def change_recipe():
    recipe_number = recipeVar.get()
    recipe_number += 1
    
    if recipe_number == 4:
        recipe_number = 0
    
    recipeTitleVar.set(recipeTitles[recipe_number])
    recipesVar.set(recipes[recipe_number])

    recipeImageLabel.config(image=food_image_list[recipe_number])
    
    recipeVar.set(recipe_number)


# MAIN
root = Tk()
root.title("Fit Learn")
root.config(bg="#add8e6")
mainframe = Frame(root)
mainframe.config(bg="#add8e6")

OswaldFont = Font(family="Oswald", size=12)
FredokaFontSuperSmall = Font(family="Fredoka One", size=12)
FredokaFontSmall = Font(family="Fredoka One", size=15)
FredokaFontBig = Font(family="Fredoka One", size=40)


# WIDGETS

# TITLE
titleVar = StringVar()
titleVar.set("Fit Learn")
titleLabel = Label(mainframe, textvariable=titleVar, font=FredokaFontBig, bg="#add8e6")


# GENDER RADIO BUTTONS
gendersFrame = LabelFrame(mainframe, text="Select your gender", font=OswaldFont, bg="#add8e6")
genderVar = IntVar()
maleRadio = Radiobutton(gendersFrame, text="Male", variable=genderVar, value=1, bg="#add8e6")
femaleRadio = Radiobutton(gendersFrame, text="Female", variable=genderVar, value=2, bg="#add8e6")
otherRadio = Radiobutton(gendersFrame, text="Other", variable=genderVar, value=3, bg="#add8e6")


# HEIGHT & WEIGHT SCALES
heightVar = IntVar()
heightScale = Scale(mainframe, from_=0, to_=250, variable=heightVar, width=15, length=150, orient=HORIZONTAL, label="Height (cm)", bg="#add8e6")
weightVar = IntVar()
weightScale = Scale(mainframe, from_=0, to_=250, variable=weightVar, width=15, length=150, orient=HORIZONTAL, label="Weight (kg)", bg="#add8e6")


# FITNESS GOAL OPTION MENU
goals = ["Lose Weight", "Gain Weight", "Build Muscle"]
goalVar = StringVar()
goalVar.set("Select Your Fitness Goal")
goalOption = OptionMenu(mainframe, goalVar, *goals,)
goalOption.config(bg="#add8e6", font=OswaldFont)


# CREATE PROFILE BUTTON
createProfileButton = Button(mainframe, command=create_profile_and_grid, text="Create Profile", font=FredokaFontSmall, bg="#add8e6")


# FOOD OPTIONS LISTBOX
foodOptionsList = ["Banana", "5% Yogurt - 1 Cup", "Avocado", "Whole Egg", "Chicken Breast 100g", "Salmon 100g", "White Rice 100g", "Spinach 100g", "2% Milk - 1 Cup", "White Bread - 1 slice"]
foodMacrosList = [[110, 1, 28, 0], [210, 20, 7, 11], [240, 3, 12, 21], [71, 6, 0, 4], [123, 25, 0, 2], [100, 19, 0, 2], [157, 3, 34, 0], [23, 3, 4, 0], [120, 8, 11, 5], [50, 1, 9, 0]]
foodOptionsVar = StringVar()
foodOptionsVar.set(foodOptionsList)
foodOptionsListbox = Listbox(mainframe, listvariable=foodOptionsVar, selectmode=SINGLE, font=OswaldFont, bg="#add8e6")
foodOptionsLabelVar = StringVar()
foodOptionsLabelVar.set("Food Options")
foodOptionsLabel = Label(mainframe, textvariable=foodOptionsLabelVar, font=FredokaFontSmall, bg="#add8e6")


# FOOD OPTION ADD BUTTON
addFoodOptionButton = Button(mainframe, command=add_user_food_and_change_scale, text="Add", font=FredokaFontSmall, bg="#add8e6")


# CALORIES, PROTEIN, FAT & CARB ENTRIES
calorieLabelVar = StringVar()
calorieLabelVar.set("Calories")
calorieLabel = Label(mainframe, textvariable=calorieLabelVar, font=OswaldFont, bg="#add8e6")
calorieVar = IntVar()
calorieEntry = Entry(mainframe, text=f"{calorieVar}", font=OswaldFont, bg="#add8e6", state=DISABLED, width=10)

proteinLabelVar = StringVar()
proteinLabelVar.set("Protein (g)")
proteinLabel = Label(mainframe, textvariable=proteinLabelVar, font=OswaldFont, bg="#add8e6")
proteinVar = IntVar()
proteinEntry = Entry(mainframe, text=f"{proteinVar}", font=OswaldFont, bg="#add8e6", state=DISABLED, width=10)

carbsLabelVar = StringVar()
carbsLabelVar.set("Carbohydrates (g)")
carbsLabel = Label(mainframe, textvariable=carbsLabelVar, font=OswaldFont, bg="#add8e6")
carbsVar = IntVar()
carbsEntry = Entry(mainframe, text=f"{carbsVar}", font=OswaldFont, bg="#add8e6", state=DISABLED, width=10)

fatLabelVar = StringVar()
fatLabelVar.set("Fat (g)")
fatLabel = Label(mainframe, textvariable=fatLabelVar, font=OswaldFont, bg="#add8e6")
fatVar = IntVar()
fatEntry = Entry(mainframe, text=f"{fatVar}", font=OswaldFont, bg="#add8e6", state=DISABLED, width=10)


# USER FOOD LISTBOX
userFoodList = []
userFoodVar = StringVar()
userFoodListbox = Listbox(mainframe, listvariable=userFoodVar, selectmode=SINGLE, font=OswaldFont, bg="#add8e6")
userFoodLabelVar = StringVar()
userFoodLabelVar.set("My Food")
userFoodLabel = Label(mainframe, textvariable=userFoodLabelVar, font=FredokaFontSmall, bg="#add8e6")


# USER FOOD REMOVE BUTTON
removeFoodOptionButton = Button(mainframe, command=remove_food_and_reset_macro_entries, text="Remove", font=FredokaFontSmall, bg="#add8e6")


# MACRO SCALE
amountVar = IntVar()
totalCaloriesVar = IntVar()
totalProteinVar = IntVar()
totalCarbsVar = IntVar()
totalFatVar = IntVar()
amountVar.set(0)
macroScale = Scale(mainframe, from_=1000, to_=0, variable=amountVar, width=50, length=350, state=DISABLED, label="Calories", font=OswaldFont, bg="#add8e6", troughcolor="#ffde5b")


# MACRO SPINBOX
macros = ["Calories", "Protein", "Carbohydrates", "Fat"]
macroOptionVar = StringVar()
macroOptionVar.set("Calories")
macroSpinbox = Spinbox(mainframe, textvariable=macroOptionVar, values=macros)
macroSpinbox.config(bg="#ffde5b", font=OswaldFont, width=15)


# MACRO CHANGE BUTTON
macroChangeButton = Button(mainframe, command=change_macro_scale, text="Change", font=FredokaFontSuperSmall, bg="#add8e6")


# RESET & RESET ALL BUTTONS
resetButton = Button(mainframe, command=reset, text="RESET", font=FredokaFontSmall, bg="#add8e6")
resetAllButton = Button(mainframe, command=reset_all, text="RESET ALL", font=FredokaFontSmall, bg="#add8e6")


# RECIPE ENTRIES
recipeTitles = ["2 INGREDIENT CREPES", "CHICKEN AVOCADO RICE BOWL", "YOGURT BAKED SALMON", "FLUFFY FRENCH TOAST"]
recipeTitleVar = StringVar()
recipeTitleVar.set(recipeTitles[0])
recipeTitleLabel = Label(mainframe, textvariable=recipeTitleVar, font=FredokaFontSmall, bg="#add8e6")

recipeFrame = LabelFrame(mainframe, bg="#add8e6")

recipes = ["Make these delicious crepes by blending together\n4 eggs with 2 bananas and cooking in a pan.\nTop them off with some spinach\nand more bananas!", "Season both your chicken and rice to your\nliking and bake the chicken while cooking the rice\nin a rice cooker. Once done, plate them\nwith some sliced avocado and enjoy!", "Bake your salmon until golden brown and drizzle\nwith yogurt. Serve with spinach \nand a squeeze of lemon!", "Dip your bread in egg and milk on both sides\nand place in a pan until golden brown on both sides.\nServe with a fried egg on top!"]
recipesVar = StringVar()
recipesVar.set(recipes[0])
recipeLabel = Label(recipeFrame, textvariable=recipesVar, font=OswaldFont, bg="#add8e6")

load_images()
recipeVar = IntVar()
recipeVar.set(0)
recipeImageLabel = Label(recipeFrame, image=food_image_list[0], bg="#add8e6")


# RECIPE SWITCH BUTTON
recipeSwitchButton = Button(mainframe, command=change_recipe, text="\u23F4", font=("Arial", 40), bg="#add8e6")


# GRIDING WIDGETS (REST OF WIDGETS ARE GRID AFTER AN EVENT)

root.minsize(width=500, height=350)
root.maxsize(width=1225, height=750)
mainframe.grid(padx=30, pady=20)

titleLabel.grid(row=1, column=2)

gendersFrame.grid(row=2, rowspan=2, column=1, ipadx=10, ipady=5, padx=30, pady=20)
maleRadio.grid(row=1, column=1, sticky=W, ipady=10)
femaleRadio.grid(row=2, column=1, sticky=W)
otherRadio.grid(row=3, column=1, sticky=W, ipady=10)

heightScale.grid(row=2, column=2)
weightScale.grid(row=3, column=2)

goalOption.grid(row=2, column=3)

createProfileButton.grid(row=3, column=3, ipadx=20, ipady=5)


