import json
from datetime import datetime

def create_note():
    note_id = str(datetime.now().timestamp())
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "date": date
    }
    return note


def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write('\n')
    print("Заметка успешно сохранена")


def read_notes():
    with open("notes.json", "r") as file:
        notes = file.readlines()
        if notes:
            for note in notes:
                note_data = json.loads(note)
                print("ID:", note_data["id"])
                print("Заголовок:", note_data["title"])
                print("Тело:", note_data["body"])
                print("Дата создания:", note_data["date"])
                print("=====================================")
        else:
            print("Список заметок пуст")


def view_all_notes():
    read_notes()


def edit_note():
    read_notes()
    notes = read_notes_file()
    if not notes:
        return
    note_id = input("Введите ID заметки для редактирования: ")
    note = find_note_by_id(note_id, notes)
    if note is None:
        print("Заметка с указанным ID не найдена")
        return
    updated_note = create_note()
    updated_note["id"] = note["id"]
    index = notes.index(note)
    notes[index] = updated_note
    save_notes_file(notes)
    print("Заметка успешно отредактирована")


def delete_note():
    read_notes()
    notes = read_notes_file()
    if not notes:
        return
    note_id = input("Введите ID заметки для удаления: ")
    note = find_note_by_id(note_id, notes)
    if note is None:
        print("Заметка с указанным ID не найдена")
        return
    notes.remove(note)
    save_notes_file(notes)
    print("Заметка успешно удалена")


def save_notes_file(notes):
    with open("notes.json", "w") as file:
        for note in notes:
            json.dump(note, file)
            file.write('\n')


def read_notes_file():
    with open("notes.json", "r") as file:
        notes = file.readlines()
        if not notes:
            print("Список заметок пуст")
            return []
        return [json.loads(note) for note in notes]


def find_note_by_id(note_id, notes):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def filter_notes_by_date(date):
    read_notes()
    notes = read_notes_file()
    if not notes:
        return
    filtered_notes = [note for note in notes if note["date"].startswith(date)]
    if not filtered_notes:
        print("Нет заметок, соответствующих заданной дате")
        return
    for note in filtered_notes:
        print("ID:", note["id"])
        print("Заголовок:", note["title"])
        print("Тело:", note["body"])
        print("Дата создания:", note["date"])
        print("=====================================")


def main():
    while True:
        command = input("Введите команду (add, view, edit, delete, filter, exit): ")
        if command == "add":
            note = create_note()
            save_note(note)
        elif command == "view":
            view_all_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "filter":
            date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            filter_notes_by_date(date)
        elif command == "exit":

            break
        else:
            print("Неверная команда. Попробуйте еще раз.")
        print()


if __name__ == "__main__":
    main()