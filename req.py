import requests

customer = { 
 'lead_origin': 'landing_page_submission',
 'lead_source': 'direct_traffic',
 'do_not_email': 'no',
 'do_not_call': 'no',
 'last_activity': 'sms_sent',
 'country': 'india',
 'specialization': 'healthcare_management',
 'how_did_you_hear_about_x_education': 'student_of_someschool',
 'what_is_your_current_occupation': 'student',
 'what_matters_most_to_you_in_choosing_a_course': 'better_career_prospects',
 'search': 'no',
 'magazine': 'no',
 'newspaper_article': 'no',
 'x_education_forums': 'no',
 'newspaper': 'no',
 'digital_advertisement': 'no',
 'through_recommendations': 'no',
 'receive_more_updates_about_our_courses': 'no',
 'tags': 'will_revert_after_reading_the_email',
 'lead_quality': 'might_be',
 'update_me_on_supply_chain_content': 'no',
 'get_updates_on_dm_content': 'no',
 'lead_profile': 'select',
 'city': 'mumbai',
 'asymmetrique_activity_index': '02.medium',
 'asymmetrique_profile_index': '02.medium',
 'i_agree_to_pay_the_amount_through_cheque': 'no',
 'a_free_copy_of_mastering_the_interview': 'no',
 'last_notable_activity': 'sms_sent',
 'totalvisits': 4.0,
 'total_time_spent_on_website': 1503,
 'page_views_per_visit': 2.0,
 'asymmetrique_activity_score': 14.0,
 'asymmetrique_profile_score': 15.0}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)

if response.status_code == 200:
    print('✅ Prediction:', response.json())
else:
    print('❌ Error:', response.status_code, response.text)

#print(response.status_code)
#print(response.json())