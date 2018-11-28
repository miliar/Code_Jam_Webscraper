#include<cmath>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#define int long long
#define P(x) cout << x << endl
#define D(x) P(#x << ": " << x)
#define F(i,n) for(int i=0; i<(int)(n); ++i)
#define DEC(i,n) for(int i=(int)(n); --i>=0;)
using namespace std;

int T;

signed main() {
	cin >> T;
	F(sc,T){
		int D,N; cin >> D >> N;
		int K,S;
		double ans = 0.0;
		F(i,N){
			cin >> K >> S;
			ans = max(ans,double(D-K)/double(S));
		}
		ans = D/ans;

		printf("Case #%d: %.7lf\n",sc+1,ans);
	}
	
}
