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

int who[1550];
vector<pii> a1,a2;
vector<pair<pii,int> > per;
int ans = 1000;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int test = 0,T;
	cin >> T;
	while(test++<T){
		int n,m;
		cin >> n >> m;
		a1.clear();
		a2.clear();
		ans = 1000;
		int n1 = 100000,n2 = -10000;
		for(int i = 0;i < n;i++){
			int a,b;
			cin >> a >> b;
			n1 = min(a,n1);
			n2 = max(b,n2);
			a1.pb(mp(a,b));
		}
		sort(ALL(a1));
		int m1 = 100000,m2 = -100000;
		for(int i = 0;i < m;i++){
			int a,b;
			cin >> a >> b;
			m1 = min(a,m1);
			m2 = max(b,m2);
			a2.pb(mp(a,b));
		}
		sort(ALL(a2));
		ans = 4;
		if(n == 1 || m == 1){
			ans = 2;
		}else{
			if(n==2){
				if(a1[1].Y - a1[0].X<=720){
					ans = 2;
				}else{
					if(a1[0].Y+1440 - a1[1].X <=720){
						ans = 2;
					}
				}
			}else{
				if(a2[1].Y - a2[0].X<=720){
					ans = 2;
				}else{
					if(a2[0].Y+1440 - a2[1].X <=720){
						ans = 2;
					}
				}
			}
		}
		printf("Case #%d: %d\n",test,ans);
	}


    return 0;
}