#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstring>
#include<sstream>
#include<climits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define S(x) scanf("%d",&x)
#define SD(x) scanf("%lf",&x)
#define SL(x) scanf("%lld",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x, i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

ll getMx(ll N, ll K, int x){
	return ((N - K + pow(2,x-1))/(pow(2,x)));
}

ll getMn(ll N, ll K, int x){
	return (N-K)/(pow(2,x));
}

int main() {
	
	int T,tst=1; S(T);
	ll N,K,J,mx,mn;
	int x;
	
	while(T--){
		
		SL(N); SL(K);

		x = 0;
		J = K;
		while(J){
			x++;
			J>>=1;
		}

		mx = getMx(N,K,x);
		mn = getMn(N,K,x);

		printf("Case #%d: %lld %lld\n", tst++, mx, mn);
	}
}
