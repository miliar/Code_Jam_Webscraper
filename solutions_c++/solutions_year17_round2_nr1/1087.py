#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<unordered_set>
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
#define SL(x) scanf("%lld",&x)
#define SD(x) scanf("%lf",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x, i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

int main() {
	int T; S(T);	
	int  tst = 1;
	int D,N,temp;
	vi K,S;
	double time;

	while(T--){
		
		S(D);
		S(N);
		K.clear(); S.clear();
		time = 0.0;

		F(i,0,N){
			S(temp);
			K.pb(temp);
			S(temp);
			S.pb(temp);
		}

		F(i,0,N){
			time = max(time, ((D - K[i])*1.0)/(S[i]*1.0));
		}

		printf("Case #%d: %.9lf\n", tst++, (D*1.0)/time);
	}
}
