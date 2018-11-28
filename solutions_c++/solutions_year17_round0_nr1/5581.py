#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

#define INF 99999999

map<string, int> memo;
int n;
map<char, char> inv;

void swap(string &s, int l, int r){
	for (int i = l; i <= r; i++){
		s[i] = inv[s[i]];
	}
}

int get(string s){
	if (memo.find(s) == memo.end()){
		memo[s] = INF;
		int ans = INF;
		for (int i = 0; i < s.size()-n+1; i++){
			string tmp = s;
			swap(tmp, i, i+n-1);
			ans = min(ans, 1+get(tmp));		
		}
		memo[s] = ans;
	}
	return memo[s];
}

int main(){ _
	inv['+'] = '-';
	inv['-'] = '+';
	int k;
	cin >> k;
	string s;
	for (int q = 1; q <= k; q++){
		cin >> s;
		cin >> n;
		memo.clear();
		string ans = s;
		for (int i = 0; i < ans.size(); i++)
			if (s[i] == '-')
				s[i] = '+';
		memo[ans] = 0;
		int value = get(s);
		cout << "Case #" << q << ": ";
		if (value == INF)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << value << endl;
	}	
	return 0;
}
