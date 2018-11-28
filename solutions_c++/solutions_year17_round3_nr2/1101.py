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
#define ireg(i,a,b) for(int i = ((int)(b));i>=((int)(a));i--)
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
	int T; cin >> T;
	rep(C, T){
		int am, bm, re = 720, ans; cin >> am >> bm; ans = bm;
		vector<mp> a(am+bm+1, mp(IINF, IINF));
		rep(i, am) cin >> a[i].fir >> a[i].sec;
		reg(i, am, am+bm-1){
			cin >> a[i].fir >> a[i].sec;
			re -= a[i].sec - a[i].fir;
			a[i].sec = -a[i].sec;
		}
		sort(a.begin(), a.end());
		a.back() = mp(a[0].fir+1440, a[0].sec+(a[0].sec>0?1440:-1440));
		
		vector<mp> b[2]; vector<int> sb(3, 0);
		rep(i, a.size()-1){
			bool ff = (a[i].sec > 0); 
			bool fb = (a[i+1].sec > 0);
			if(!(ff||fb)){
				b[0].push_back(mp(a[i+1].fir + a[i].sec, i));
				sb[0] += b[0].back().fir;
			}else if(ff&&fb){
				b[1].push_back(mp(a[i+1].fir - a[i].sec, i));
				sb[1] += b[1].back().fir;
			}else{
				sb[2] += a[i+1].fir - abs(a[i].sec);
			}
		}
		sort(b[0].begin(), b[0].end());
		sort(b[1].rbegin(), b[1].rend());
		
		if(re == 0){
			ans -= upper_bound(b[0].begin(), b[0].end(), mp(0, IINF)) - lower_bound(b[0].begin(), b[0].end(), mp(0, 0));
		}else{
			if(re < sb[0]){
				for(int i = 0; re > 0; i++){
					re -= b[0][i].fir;
					ans--;
				}
				if(re != 0) ans++;
			}else if(re <= sb[0] + sb[2]){
				ans -= b[0].size();
			}else{
				re -= sb[0] + sb[2];
				for(int i = 0; re > 0; i++){
					re -= b[1][i].fir;
					ans++;
				}
			}
		}
		
		cout << "Case #" << C+1 << ": " << ans*2 << endl;
	}

	return 0;
}