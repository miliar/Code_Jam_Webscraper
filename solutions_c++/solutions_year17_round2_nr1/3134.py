// author: ash.code
 
#include <bits/stdc++.h>
 
#define FOR(i, a, b) for(int i = a; i <= b; i++)
#define ROF(i, a, b) for(int i = a; i >= b; i--)
#define REP(i, n) for(int i = 0; i < n; i++)

#define FILL(X, A) memset(X, A, sizeof(X))
#define fast ios_base::sync_with_stdio(false)
#define MOD 1000000007
#define inf INT_MAX
#define pll pair<long long,long long>
#define pii pair<int,int>
typedef long long ll;

using namespace std;

int main() {
    // #ifndef ONLINE_JUDGE
    // 	freopen("ip.txt", "r", stdin);
    // 	freopen("op.txt", "w", stdout);
    // #endif
	
	//fast;
    int t;
    scanf("%d", &t);
    int d, n, k[1005], s[1005], x[1005];
    REP(tt, t) {
		scanf("%d%d", &d, &n);
		double max=INT_MIN;
		REP(i, n) {
			cin >> k[i] >> s[i];
			double xx=(double)(d-k[i])/(double)s[i];
			if(xx > max) max=xx; 
		}
		double res = (double)d/max;
		//cout << "Case #" << tt+1 << ": " << res << endl;
    	printf("Case #%d: %lf\n", tt+1, res);
    }    
    
    return 0;
}

