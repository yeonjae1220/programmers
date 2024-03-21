# 제한시간 내 해결x
#https://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
def solution(m, musicinfos):
    answer = '(None)'

    for infos in musicinfos:
        info_list = infos.split(',')
        
        cal_start_min = info_list[0].split(':')
        cal_end_min = info_list[1].split(':')
        playtime = (int(cal_end_min[0]) * 60 + int(cal_end_min[1])) - \
            (int(cal_start_min[0]) * 60 + int(cal_start_min[1]))
        

        title = info_list[2]
        music_note = info_list[3]

        print('music_note : ', music_note)

        changed_music_note = []
        for i in range(len(music_note)):
            if music_note[i] == '#':
                changed_music_note[-1] = changed_music_note[-1].lower()
                continue
            
            changed_music_note.append(music_note[i])
        
        changed_music_note = ''.join(changed_music_note)
        print('changed_music_note : ', changed_music_note)        


        changed_m = []
        for i in range(len(m)):
            if m[i] == '#':
                changed_m[-1] = changed_m[-1].lower()
                continue

            changed_m.append(m[i])
        
        changed_m = ''.join(changed_m)
        print('chaged_m : ', changed_m)



        if len(changed_music_note) > playtime:
            changed_music_note = changed_music_note[:playtime]

        

        changed_music_note += changed_music_note
        
        if len(changed_m) > len(changed_music_note):
            if changed_music_note in changed_m:
                return title

        else:
            if changed_m in changed_music_note:
                return title
       

    return answer

m = "ABC"#"ABCDEFG"#"CC#BCC#BCC#BCC#B"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]#["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]#["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))