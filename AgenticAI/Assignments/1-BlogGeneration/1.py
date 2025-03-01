



if topic:
    with st.spinner("Generating your blog... ⏳"):
        result = app.invoke({"topic": topic})
        st.success("✅ Blog Generated!")
        st.subheader("📌 Generated Blog:")
        st.write(result["final_blog"])

    # Collect human feedback
    feedback = st.text_area("Provide feedback on the blog (optional):", "")

    if feedback:
        with st.spinner("Incorporating your feedback... ⏳"):
            result_with_feedback = app.invoke({"topic": topic, "feedback": feedback, "final_blog": result["final_blog"]})
            st.success("✅ Feedback Incorporated!")
            st.subheader("📌 Updated Blog:")
            st.write(result_with_feedback["final_blog"])
else:
    st.warning("⚠️ Please enter a topic first.")