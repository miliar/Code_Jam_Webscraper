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

string solve(string str, int k) {
	int cnt = 0;
	for (int i = 0; i + k  < str.length() + 1;i++) {
		if (str[i] == '-') {
			for (int j = 0; j < k; j++) {
				str[i + j] = (str[i + j] == '+' ? '-' : '+');
			}
			cnt++;
		}
	}
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '-') {
			return "IMPOSSIBLE";
		}
	}
	stringstream ss;
	ss << cnt;
	return ss.str();
}
int main() {
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << test << ": "<<solve(s,k)<<"\n";
	}
	return 0;
}