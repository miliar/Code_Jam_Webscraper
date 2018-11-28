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
	int N,R,O,Y,G,B,V;
	int s;

	while(T--){
		S(N);
		S(R); S(O); S(Y); S(G); S(B); S(V);

		s = R+Y+B;

		bool flag = true;
		string ans = "";
		if(R > s/2 || Y > s/2 || B > s/2) flag = false;
		else {

			vector<pair<int,char> > c;
			c.pb(mp(R,'R'));
			c.pb(mp(Y,'Y'));
			c.pb(mp(B,'B'));
			sort(c.begin(), c.end());
			reverse(c.begin(), c.end());
			vector<int> cn;
			cn.pb(0);
			cn.pb(0);
			cn.pb(0);

			F(i,0,N){
				ans += 'X';
			}

			F(i,0,N){
				if(i%2 == 0){
					if(cn[0] < c[0].first){
						ans[i] = c[0].second;
						cn[0]++;
					}
				}
			}

			for(int i = N-1; i >= 0; i--){
				if(i == N-1){
					if(cn[1] < c[1].first){
						ans[i] = c[1].second;
						cn[1]++;
						continue;
					}
				}

				else {

					if(ans[i] != 'X') continue;

					if(ans[i+1] != c[1].second){
						if(cn[1] < c[1].first){
							ans[i] = c[1].second;
							cn[1]++;
							continue;
						}
					}

					if(ans[i+1] != c[2].second){
						if(cn[2] < c[2].first){
							ans[i] = c[2].second;
							cn[2]++;
							continue;
						}
					}
				}
			}
		}

		if(!flag) ans = "IMPOSSIBLE";
		cout<<"Case #"<<tst++<<": "<<ans<<endl;
	}
}
