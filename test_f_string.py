interview_round = 'Technical'
llm = {'name': 'John', 'years_experience': 5, 'current_role': 'Dev', 'skills_found': ['Python', 'Java'], 'strengths': ['Fast'], 'interview_focus': ['Testing']}
jd_text = 'Software Engineer'

prompt = f"""Generate 8-10 targeted interview questions for a {interview_round} round.

**Candidate Background**:
- Name: {llm.get('name')}
- Experience: {llm.get('years_experience')} years
- Current Role: {llm.get('current_role')}
- Key Skills: {', '.join(llm.get('skills_found', [])[:5])}
- Strengths: {', '.join(llm.get('strengths', [])[:3])}
- Areas to probe: {', '.join(llm.get('interview_focus', []))}

**Job Description**:
{str(jd_text)[:1000]}

Generate questions that:
1. Assess technical depth in required skills
2. Probe experience claims
3. Evaluate culture fit
4. Address any gaps or concerns
5. Are specific to this candidate's background

Return ONLY valid JSON with this exact key:
{{
  "questions": [list of strings]
}}"""
print("Success")
