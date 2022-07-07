import os
import pickle

# Python 3.8.12
# A CLI todo app

# Functions
def display_title_bar():
  # Clears the terminal screen, displays a title bar that
  #  includes the amount of notes saved
  os.system('clear')
  print("----------------------------------")
  print("- Notes and Todos (%d)" % len(note_titles))
  print("----------------------------------")

def get_choice(invalid_input):
    print("\nMenu:")
    print("1 - New Note")
    print("2 - Edit title")
    print("3 - Edit content")
    print("4 - Delete note")
    print("Q - Quit app")

    # Check for invalid user input
    if invalid_input:
        choice = input("Invalid option. Please try again [1-4, Q]:\n> ")
        invalid_input = False
    else:
        choice = input("Choose an option [1-4, Q]:\n> ")
    return choice

def get_note_title():
    note_title = input("Create a note title:\n> ")
    return note_title

def get_note_content():
    note_content = input("Take a note:\n> ")
    return note_content

def save_note():
    # Try to save notes to a file
    try:
        # Save note title
        file_note_titles = open('titles.pydata', 'wb')
        pickle.dump(note_titles, file_note_titles)
        file_note_titles.close()

        # Save note content
        file_note_contents = open('contents.pydata', 'wb')
        pickle.dump(note_contents, file_note_contents)
        file_note_contents.close()
    except Exception as e:
        print(e)

def load_note_titles():
    # Load note titles. If the file is not found, it returns an
    #  empty array
    try:
        file_note_titles = open('titles.pydata', 'rb')
        note_titles = pickle.load(file_note_titles)
        file_note_titles.close()
        return note_titles
    except Exception as e:
        print(e)
        return []

def load_note_contents():
    # Load note contents. If the file is not found, it an
    #  empty array
    try:
        file_note_contents = open('contents.pydata', 'rb')
        note_contents = pickle.load(file_note_contents)
        file_note_contents.close()
        return note_contents
    except Exception as e:
        print(e)
        return []

def new_note():
    # Creates a new notes, and saves it to a file
    display_title_bar()
    note_titles.append(get_note_title())
    note_contents.append(get_note_content())
    save_note()

# 2
def edit_note_title():
    display_title_bar()
    display_note_titles()
    note_index = input("Enter note ID to edit (1-%d):\n> #" % len(note_titles))
    note_index = int(note_index)
    new_note_title = input("Edit the title:\n> ")
    note_titles[note_index-1] = new_note_title
# 3
def edit_note_content():
    display_title_bar()
    display_note_titles()
    note_index = input("Enter note ID (1-%d):\n> #" % len(note_titles))
    note_index = int(note_index)
    new_note_content = input("Edit the note:\n> ")
    note_contents[note_index-1] = new_note_content

# 4
def delete_note():
    display_title_bar()
    note_index = input("Enter note ID to delete:\n> ")
    note_index = int(note_index)
    note_index -= 1
    return note_index

def display_notes(display_content):
    for index, note_title in enumerate(note_titles):
        note_id = index + 1
        print("[#%d / %s]\n" % (note_id, note_title), end="")
        note_id -= 1
        if display_content:
            print(note_contents[note_id])

def display_note_titles():
    display_content = False
    display_notes(display_content)
    display_content = True

# Main app
# Initialize variables

choice = " "
invalid_input = False
display_content = True
note_titles = load_note_titles()
note_contents = load_note_contents()
while choice != "Q":
    display_title_bar()

    # Display notes
    display_notes(display_content)
    
    # Get user choice
    choice = get_choice(invalid_input)

    # Respond to user choice
    if choice == "1":
        new_note()
    elif choice == "2":
        edit_note_title()
    elif choice == "3":
        edit_note_content()
    elif choice == "4":
        
        # Delete a note
        note_id = delete_note()
        note_titles.pop(note_id)
        note_contents.pop(note_id)
    else:
        invalid_input = True
    
    # Save all changes to a file
    save_note()