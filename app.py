
import streamlit as st
import random

st.set_page_config(page_title="InterviewPrep AI v1.0", page_icon="🎤", layout="wide")

QUESTIONS={
"Developer":[
"What is OOP?",
"Explain REST API.",
"What is the difference between list and tuple in Python?"
],
"Data Scientist":[
"What is overfitting?",
"Explain bias vs variance.",
"What is feature engineering?"
]}

ROADMAP={
"Beginner":["Python Basics","Loops & Functions","Easy Problem Solving"],
"Intermediate":["OOP","REST APIs","Mini Projects"],
"Advanced":["System Design","Scalability","Distributed Systems"]
}

st.title("🚀 InterviewPrep AI v1.0")

page=st.sidebar.radio("Navigation",["Home","Mock Interview","Dashboard"])

if "questions" not in st.session_state:
    st.session_state.questions=[]
    st.session_state.answers=[]
    st.session_state.scores=[]
    st.session_state.feedback=[]

if page=="Home":
    st.markdown("""
### AI-powered mock interview simulator

- Generate interview questions
- Mock AI evaluation
- Skill gap analysis
- Learning roadmap
- Performance dashboard
""")

elif page=="Mock Interview":
    role=st.selectbox("Role",list(QUESTIONS.keys()))
    level=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])

    if st.button("Generate Questions"):
        st.session_state.questions=QUESTIONS[role]
        st.session_state.answers=[""]*3
        st.session_state.scores=[]
        st.session_state.feedback=[]

    if st.session_state.questions:
        st.subheader("Interview")
        ans=[]
        for i,q in enumerate(st.session_state.questions):
            ans.append(st.text_area(f"Q{i+1}. {q}",value=st.session_state.answers[i],key=f"a{i}"))
        if st.button("Submit Answers"):
            st.session_state.answers=ans
            scores=[]
            feedback=[]
            for a in ans:
                score=random.randint(50,95)
                scores.append(score)
                feedback.append("✅ Good explanation." if score>=80 else "⚠ Needs improvement.")
            st.session_state.scores=scores
            st.session_state.feedback=feedback

        if st.session_state.scores:
            st.subheader("Evaluation")
            for i,s in enumerate(st.session_state.scores):
                st.metric(f"Question {i+1}",f"{s}/100")
                st.write(st.session_state.feedback[i])

            avg=sum(st.session_state.scores)/len(st.session_state.scores)
            st.subheader("Skill Gap Analysis")
            if avg>80:
                st.success("Strong skills")
            elif avg>=60:
                st.warning("Moderate skills")
            else:
                st.error("Weak foundation")

            st.subheader("Learning Roadmap")
            for item in ROADMAP[level]:
                st.write("•",item)

elif page=="Dashboard":
    st.header("Performance Dashboard")
    if st.session_state.scores:
        avg=sum(st.session_state.scores)/len(st.session_state.scores)
        c1,c2,c3=st.columns(3)
        c1.metric("Average Score",f"{avg:.1f}")
        c2.metric("Questions",len(st.session_state.questions))
        c3.metric("Answers",len([a for a in st.session_state.answers if a.strip()]))
        st.progress(min(int(avg),100))
        st.bar_chart(st.session_state.scores)
    else:
        st.info("Complete an interview first.")
