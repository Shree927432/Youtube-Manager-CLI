import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    
    for index,video in enumerate(videos, start =1):
        print(f"{index}.Name : {video['name']} | Duration : {video['time']}")
    print('*'* 90)

def add_video(videos):
    print('*'* 90)
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print('*'* 90)

def update_video(videos):
    print('*'* 90)
    list_all_videos(videos)
    index = int(input("Enter the video number to update :"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name :")
        time = input("Enter the new video time :")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected") 
    print('*'* 90)

      
def delete_video(videos):
    print('*'* 90)
    list_all_videos(videos)
    index = int(input("Enter the video number to delete :"))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        print(f'No.{index} video has been deleted.')
        save_data_helper(videos)
        
    else:
        print("Invalid video index")
    print('*'* 90)

def main():
    videos = load_data()
    while True:
        print("\n __YOUTUBE VIDEO MANAGER__ | Choose an option")
        print("1.List all Youtube videos.")
        print("2.Add a youtube video.")
        print("3.Update a youtube video.")
        print("4.Delete a youtube video.")
        print("5.Exit the app.")
        choice = input('Enter the choice :')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()