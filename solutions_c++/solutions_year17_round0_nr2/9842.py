#include <iostream>
#include <queue>
#include <string>
#include <vector>


/*
Input 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

*/

using namespace std;

int main(int argc, char const *argv[])
{
 	int n;
 	
 	string num;
 	string ans;
 	cin >>  n;
 	for (int i = 0; i < n; ++i)
 	{
 		std::vector<int> num;
 		string num_str;
 		cin >> num_str;
 		int start = 0, ans_begin = 0;
 		int len = num_str.size();
 		int flag = 0;
 		if (len == 1)
 		{
 			cout << "Case #" << i + 1 <<": " << stoi(num_str) << endl;
 			continue;
 		}
 		for (int j = 0; j < len; ++j)
 		{
 			/* code */
 			num.push_back(num_str[j] - '0');
 		}
 		for (int j = 0; j < len - 1; ++j)
 		{
 			if (num[j] <= num[j + 1])
 			{
 				if (num[j] < num[j+1])
 				{
 					start++;
 				}
 				continue;
 			} else {
 				flag = 1;
 				break;
 			}
 		}
 		// cout << flag;
 		if(flag == 1) {
	 		// cout <<" start ";
	 		// cout << start;
	 		if(num[start] == 1 && start == 0) {
	 			ans_begin++;
	 			start++;
	 		} else {
	 			num[start]--;
	 			start++;
	 		}
	 		// cout <<" start ";
	 		// cout << start;
	 		for (int j = start; j < num.size(); ++j)
	 		{
	 			/* code */
	 			num[j] = 9;
	 		}
 		}
 		cout << "Case #" << i + 1 <<": ";
 		for (int j = ans_begin; j < num.size(); ++j)
 		{
 			/* code */
 			cout << num[j];
 		}
 		cout << endl;
 	}
	return 0;
}