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
typedef pair<lli, lli> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))

#define PI 3.141592653589

int main(void){
	int t; cin >> t;
	rep(c, t){
		int n, k; cin >> n >> k;
		vector<mp> p(n);
		rep(i, n){
			cin >> p[i].sec >> p[i].fir;
			p[i].fir *= 2*p[i].sec;
			p[i].sec *= p[i].sec;
		}
		sort(p.rbegin(), p.rend());
		
		lli ms = 0;
		lli sum = 0;
		rep(i, k-1){
			sum += p[i].fir;
			ms = max(ms, p[i].sec);
		}
		
		lli ans = 0;
		reg(i, k-1, n-1) ans = max(ans, p[i].fir + max(ms, p[i].sec));
		ans += sum;

		printf("Case #%d: %.10f\n", c+1, double(ans)*PI);
	}

	return 0;
}