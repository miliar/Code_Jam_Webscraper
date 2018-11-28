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

vector<pair<int,int> > pp;
vector<double> pl;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int test = 0,T;
	cin >> T;
	while(test++<T){
		int n,k;
		cin >> n >> k;
		pp.clear();
		for(int i = 0;i < n;i++){
			int a,b;
			cin >> a >> b;
			pp.pb(mp(a,b));
		}
		double ans = 0;
		for(int i = 0;i < n;i++){
			int base = pp[i].X;
			pl.clear();
			for(int j = 0;j < n;j++){
				if(i!=j){
					if(pp[j].X <= base){
						double r = pp[j].X;
						double h = pp[j].Y;
						double p = h * 2 * PI * r;
						pl.pb(p);
					}
				}
			}
			sort(ALL(pl));
			reverse(ALL(pl));
			double r = pp[i].X;
			double h = pp[i].Y;
			double a1 = r * r * PI;
			a1 += h * 2 * PI * r;
			for(int j = 0;j < k-1 && j < L(pl);j++){
				a1 += pl[j];
			}
			ans = max(ans,a1);
		}
		//for(int i = 0;i < k;i++){
		//	double r = pp[i].X;
		//	double h = pp[i].Y;
		//	if(i==0){
		//		ans+= r * r * PI;
		//	}
		//	ans+=h * 2 * PI * r;
		//}

		printf("Case #%d: %.8f\n",test,ans);
	}


    return 0;
}