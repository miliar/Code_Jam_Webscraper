#include <iostream>
#include <string>
using namespace std;

string ans;
void dfs(const string& origin, string done, string remain) {
	if (ans != "") return;
	if (remain == "") {
		ans = done;
		return;
	}
	int max_num = remain.at(0) - '0';
	if (done < origin.substr(0, done.size())) max_num = 9;
	int pre_num = 0;
	if(done.size()) pre_num = done.back() - '0';
	for (int i = max_num; i >= 0; --i) {
		if (pre_num <= i) {
			char c = '0' + i;
			dfs(origin, done + c, remain.substr(1));
		}
	}
}

int main() {
	int t;
	cin >> t;
	string num;
	for (int tloop = 1; tloop <= t; ++tloop) {
		cin >> num;
		ans = "";
		dfs(num, "", num);
		int i = 0;
		for (; i < ans.size(); ++i) {
			if (ans.at(i) != '0') break;
		}
		string ret = ans.substr(i);
		if (ret == "") ret = "0";
		cout << "Case #" << tloop << ": " << ret << endl;
	}
}