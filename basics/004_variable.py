tester_name = "Nishat"
tester_role = "SQA Engineer"
experience_year = 2
project_name = "Billing System"
city = "Dhaka"

print(tester_name, tester_role, experience_year, city)
print(project_name)

'''✅ Assignment:
Simulate a QA test case execution using variables and print the test summary.'''

#🚀 Try it yourself first before scrolling down to see the solution!

test_case_id = "TC_101"
test_case_title = "Verify login with valid credentials"         #Test cse details
module_name = "Authentication"
priority = "High"

tester_name = "Nishat"
browser = "Chrome"
is_passed = True            #Test execusition details
execution_time_sec = 3.45

print("Test Case ID:", test_case_id)
print("Title:", test_case_title)
print("Module:", module_name)
print("Priority:", priority)                 #Print test execution summary
print("Executed By:", tester_name)
print("Browser:", browser)
print("Test Passed:", is_passed)
print("Execution Time (sec):", execution_time_sec)