#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define ld long double
#define defmod 1000000007

#define mati64(a,b) vector<vector<i64>>(a, vector<i64>(b, 0));
using namespace std;

void solve1(){
	string s; cin >> s;
	string s2 = s;
	reverse(s2.begin(), s2.end());
	int k; cin >> k;
	int n = s.length();
	int ans = 0;
	for(int i = 0; i+k <= n; ++i){
		if(s[i] == '-'){
			++ans;
			for(int j = i; j < i+k; ++j){
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	int ans2 = 0;
	for(int i = 0; i+k <= n; ++i){
		if(s2[i] == '-'){
			++ans2;
			for(int j = i; j < i+k; ++j){
				if(s2[j] == '-')
					s2[j] = '+';
				else
					s2[j] = '-';
			}
		}
	}
	bool g = true;
	for(int i = 0; i < n; ++i){
		if(s[i] == '-')
			g = false;
	}
	if(g)
		cout << min(ans, ans2) << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	
	int tests; cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		solve1();
	}
	return 0;
}
