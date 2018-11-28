#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"


using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
string find_maximum(string num, int valuable_digit_maximum, bool decreased, int &min_used) {
	if (num.length() == 1) {
		min_used = num[0] - '0';
		
		if (decreased) {
			min_used = 9;
		}else if (min_used < valuable_digit_maximum) {
			return "";
		}
		return string(1, '0' + min_used);
	}
	
	int start_from = (num[0] - '0');
	if (decreased) {
		start_from = 9;
	}
	for (int it = start_from; it >= valuable_digit_maximum; it--) {
		int mu = 9;
		string ret = find_maximum(num.substr(1), it,decreased,mu);
		if (ret != "" && it <= mu) {
			return string(1,'0'+it)+ret;
		}
		decreased = true;
	}
	return "";
}
string solve(string num) {
	int m = 0;
	string ret = find_maximum(num, 1,false,m);
	if (ret == "") {
		ret = string(num.length() - 1, '9');
	}
	return ret;
}
/*

I've used these two function to test my solution if you wonder :)

*/
int is_tidy(int num) {
	stringstream ss;
	ss << num;
	string snum = ss.str();
	for (int i = 1; i < snum.length(); i++) {
		if (snum[i] < snum[i - 1]) {
			return 0;
		}
	}
	return 1;
}
string bfsolve(string num) {
	stringstream ss;
	ss.str(num);
	int numval;
	ss >> numval;
	while (1) {
		if (is_tidy(numval)) {
			ss.clear();
			ss << numval;
			return ss.str();
		}
		numval--;
	}
	return "";
}
int main() {
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		string num;
		cin >> num;
		cout << "Case #" << test << ": "<< solve(num)<<"\n";
	}
	return 0;
}