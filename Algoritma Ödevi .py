class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"'{task}' görevi eklendi.")

    def list_tasks(self):
        if not self.tasks:
            print("Görev listeniz boş.")
        else:
            print("Görevleriniz:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"'{removed_task}' görevi silindi.")
        else:
            print("Geçersiz görev numarası.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nYapılacaklar Listesi Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Sil")
        print("4. Çıkış")

        choice = input("Seçiminiz (1-4): ")

        if choice == '1':
            task = input("Eklemek istediğiniz görevi yazın: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            todo_list.list_tasks()
            task_number = int(input("Silmek istediğiniz görevin numarasını yazın: "))
            todo_list.remove_task(task_number)
        elif choice == '4':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()