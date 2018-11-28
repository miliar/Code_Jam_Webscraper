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
vector<uint64_t> all;
bool tidy(uint64_t n){
	uint64_t la = 9;
	while(n){
		if(n%10 > la)
			return false;
		la = n%10;
		n/=10;
	}
	return true;
}

uint64_t toint(string s){
	stringstream ss;
	ss << s;
	uint64_t re;
	ss >> re;
	return re;
}

void solve1(uint64_t n){
	int ind = lower_bound(all.begin(), all.end(), n)-all.begin();
	if(all[ind] == n)
		cout << n << endl;
	else
		cout << all[ind-1] << endl;
}

void brute1(uint64_t n){
	while(n >= 1){
		if(tidy(n)){
			cout << n << endl;
			return;
		}
		--n;
	}
}



void gen1(string s){
	if(s.length() > 19)
		return;
	all.push_back(toint(s));
	for(char c = '1'; c <= '9' && c <= s[0]; ++c){
		gen1(c+s);
	}
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	string dkaslkdlsa = "3";
	for(char c = '1'; c <= '9'; ++c){
		dkaslkdlsa[0] = c;
		gen1(dkaslkdlsa);
	}
	sort(all.begin(), all.end());
	int tests; cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		uint64_t n;
		cin >> n;
		solve1(n);
	}
	return 0;
}
