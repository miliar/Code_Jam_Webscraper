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

int main() {
	
	int T,K; S(T);
	string s;
	int tst = 1;
	bool flag;
	int n,ans;

	while(T--){
		
		flag = true;
		ans = 0;

		cin>>s;
		S(K);
		n = s.length();

		F(i,0,n-K+1){
			
			if(s[i] == '+') continue;
			F(j,i,i+K){
				s[j] = (s[j] == '-') ? '+' : '-';	
			}

			ans++;
		}

		F(i,n-K+1,n){
			if(s[i] == '-') {
				flag = false;
				break;
			}	
		}

		printf("Case #%d: ", tst++);
		flag ? printf("%d\n", ans) : printf("IMPOSSIBLE\n");
	}	
}
