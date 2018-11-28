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

vector<pii> pp;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int test = 0;
	while(test++<T){
		double d;
		int n;
		cin >> d >> n;
		pp.clear();
		for(int i = 0;i < n;i++){
			int a,b;
			cin >> a >> b;
			pp.pb(mp(a,b));
		}
		double l = 0,r = 10000000000001;
		int itt = 0;
		while(itt++<=2000){
			double m = l + (r-l)/2;
			bool c = true;
			for(int i = 0;i < n;i++){
				double tm = d / m;
				double p = (double)pp[i].X + (double)pp[i].Y * tm;
				if(p<=d){
					c = false;
				}
			}
			if(c){
				l = m;
			}else{
				r = m;
			}
		}
		printf("Case #%d: ",test);
		printf("%0.8f\n",r);
	}


    return 0;
}