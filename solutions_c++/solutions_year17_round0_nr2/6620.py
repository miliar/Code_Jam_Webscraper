#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
	string maxNum(string s) {
		string ans = "";
		int flag = 0;    // decreasing flag
		// forward
		ans.append(1, s[0]);
		for (int i = 1; i < s.size(); i++) {
			if (s[i] >= ans[ans.size() - 1]) {
				ans.append(1, s[i]);
			}
			else {
				flag = 1;
				break;
			}
		}
		// backward
		if (flag) {
			while (ans.size() > 1 && ans[ans.size() - 1] == ans[ans.size() - 2]) {
				ans.pop_back();
			}
			ans[ans.size() - 1] -= 1;
		}
		for (int i = ans.size(); i < s.size(); i++)
			ans.append(1, '9');
		if (ans[0] == '0') ans.erase(0, 1);
		return ans;
	}
};

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int T;    //Test Cases
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		Solution solution;
		string input;
		cin >> input;
		cout << "Case #" << kase << ": ";
		string ans = solution.maxNum(input);
		cout << ans << endl;
	}
	return 0;
}