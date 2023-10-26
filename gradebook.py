import pandas as pd
import os
import glob

# reading the roster.csv file
rosterDF = pd.read_csv(
    "data/roster.csv",
    converters={
        'Email Address': str.lower,
        'NetID': str.lower
    },
)

hwAndExamsDF = pd.read_csv(
    "data/hw_exam_grades.csv",
    converters={
        'SID': str.lower,
    },
    usecols= lambda x: "Submission" not in x
)

quizDF = pd.DataFrame()
for file_path in glob.glob(os.getcwd() + "/data/quiz_*_grades.csv"):
    quizName = "Quiz" + file_path.split("_")[1]
    quiz = pd.read_csv(
        file_path,
        converters={
            "Email": str.lower
        },
        index_col=["Email"],
        usecols=["Email", "Grade"]
    ).rename(columns={"Grade": quizName})
    quizDF = pd.concat([quizDF, quiz], axis=1)
    print(quizDF)
    

# print(quizDF)