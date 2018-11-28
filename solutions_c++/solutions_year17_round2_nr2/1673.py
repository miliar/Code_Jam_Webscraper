#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <time.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define sz(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a) {
    if(a<0)
        return a*(-1);
    else
        return a;
}

vector<pair<int,char>> p;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 0;
	
	while(test++<T){
		int r,d,y,b;
		int n;
		cin >> n;
		cin >> r >> d >> y >> d >> b >> d;
		p.clear();
		p.pb(mp(r,'R'));
		p.pb(mp(y,'Y'));
		p.pb(mp(b,'B'));
		sort(ALL(p));
		reverse(ALL(p));
		string ans;
		bool c = true;
		while(true){
			sort(ALL(p));
			reverse(ALL(p));
			if(p[0].X+p[1].X+p[2].X==3 && p[0].X==1){
				if(L(ans)==0){
					ans = "RYB";
					break;
				}
				char l = ans[0];
				char p = ans[L(ans)-1];
				if(l=='R' && p == 'G'){
					ans+="RYB";
					break;
				}
				if(l=='R' && p == 'B'){
					ans+="RBY";
					break;
				}
				if(l=='B' && p == 'Y'){
					ans+="RBY";
					break;
				}
				if(l=='B' && p == 'R'){
					ans+="BRY";
					break;
				}
				if(l=='Y' && p == 'B'){
					ans+="RYB";
					break;
				}
				if(l=='Y' && p == 'R'){
					ans+="YBR";
					break;
				}
				if(l == 'Y' && p == 'Y'){
					ans+="RYB";
					break;
				}
				if(l == 'B' && p == 'B'){
					ans+="RBY";
					break;
				}
				if(l == 'R' && p == 'R'){
					ans+="BRY";
					break;
				}

				break;
			}
			if(p[0].X==0)
				break;
			if(L(ans)<=0){
				ans+=p[0].Y;
				p[0].X--;
			}else{
				char l = ans[L(ans)-1];
				if(l == p[0].Y){
					if(p[1].X==0){
						c = false;
						break;
					}
					ans+=p[1].Y;
					p[1].X--;
				}else{
					ans+=p[0].Y;
					p[0].X--;
				}
			}
		}
		if(ans[0]==ans[L(ans)-1])
			c = false;
		printf("Case #%d: ",test);
		if(c){
			cout << ans << endl;
		}else{
			cout << "IMPOSSIBLE" << endl;
		}
	}


    return 0;
}