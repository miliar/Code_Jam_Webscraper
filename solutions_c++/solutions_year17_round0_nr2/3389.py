#include <bits/stdc++.h>
#define endl '\n'
#define lli long long int
#define forn(i, n) for(int i=0;i<n;i++)

using namespace std;

const int MAXN = 20;

string num;
string ans;
lli memo[MAXN][2][10];

lli DP(int id,int f,int last) {
	if(memo[id][f][last] != -1) return memo[id][f][last];
	if(id == num.size()) return memo[id][f][last] = 1;
	lli r = 0;

	if(f) {
		forn(i, 10)
			if(i >= last)
				r += DP(id + 1, f, i);
	} else {
		forn(i,10)
			if(i >= last && i <= (num[id] - 48))
				r += DP(id + 1, i < (num[id] - 48), i);
	}

	return memo[id][f][last] = r;
}

void DP2(int id,int f,int last) {
	if(id == num.size()) return;
	if(f) {
		for(int i=9;i>=0;i--)
			if(i >= last && memo[id + 1][f][i]) {
				ans += char(i + 48);
				DP2(id + 1, f, i);
				return;
			}
	} else {
		for(int i=num[id]-48;i>=0;i--)
			if(i >= last && memo[id + 1][i < (num[id] - 48)][i]) {
				ans += char(i + 48);
				DP2(id + 1, i < (num[id] - 48), i);
				return;
			}			
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t, u = 1;
	cin>>t;
	while(t--) {
		cin>>num;
		forn(i, num.size() + 1)
		forn(j, 2)
		forn(h, 10)
			memo[i][j][h] = -1;
		DP(0, 0, 0);

		ans = "";
		DP2(0, 0, 0);
		cout<<"Case #"<<u++<<": ";
		int i = 0;
		while(i < ans.size() && ans[i] == '0') i++;
		while(i < ans.size()) cout<<ans[i++];
		cout<<endl;
	}
	return 0;
}
