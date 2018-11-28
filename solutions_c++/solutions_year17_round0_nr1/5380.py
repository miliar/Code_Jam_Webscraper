#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i = 0;i<((int)(n));i++)
#define reg(i,a,b) for(int i = ((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i = ((int)(n)-1);i>=0;i--)
#define ireg(i,a,b) for(int i = ((int)(b)-1);i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int, int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))

int main(void){
	int t; cin >> t;
	rep(c, t){
		string s; cin >> s;
		int k; cin >> k;
		int ans = 0;
		rep(i, s.size()-k+1){
			if(s[i] == '-'){
				ans++;
				rep(j, k) s[i+j] = (s[i+j]=='-')?'+':'-';
			}
		}
		bool f = true;
		reg(i, s.size()-k, s.size()-1) if(s[i] == '-'){
			f = false; break;
		}
		
		if(f) cout << "CASE #" << c+1 << ": " << ans << endl;
		else  cout << "CASE #" << c+1 << ": IMPOSSIBLE" << endl;
	}

	return 0;
}