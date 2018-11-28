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

i64 k[1010], s[1010];
void solve1(){
	i64 d, n; cin >> d >> n;
	ld mt = 0;
	for(int i = 0; i < n; ++i){
		cin >> k[i] >> s[i];
		ld kt = k[i], st = s[i];
		mt = max(mt, (d-kt)/st);
	}
	ld ans = d/mt;
	cout << setprecision(20);
	cout << ans << endl;
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	
	int tests;
	cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		solve1();
	}
	return 0;
}
