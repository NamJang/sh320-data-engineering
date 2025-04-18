def main():
    subjects = ['physics','calculus','poetry','history']
    grades = [98, 97, 85, 88]
    gradebook = []
    for subject, grade in zip(subjects, grades):
        gradebook.append([subject, grade])
    print(gradebook)
    subjects.append('computer science')
    grades.append(100)
    gradebook.append([subjects[-1], grades[-1]])
    subjects.append('visual arts')
    grades.append(93)
    gradebook.append([subjects[-1], grades[-1]])
    print(gradebook)

    grades[subjects.index('visual arts')] += 5
    gradebook[subjects.index('visual arts')] = ['visual arts', grades[subjects.index('visual arts')]]

    gradebook.remove(['poetry',85])
    gradebook.insert(subjects.index('poetry'), ['poetry', 'Pass'])
    print(gradebook)

    last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

    full_gradebook = last_semester_gradebook + gradebook
    print(full_gradebook)





if __name__ == '__main__':
    main()