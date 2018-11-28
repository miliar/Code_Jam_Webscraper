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

vector<double> c;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int test = 0,T;
	cin >> T;
	while(test++<T){
		int n,k;
		cin >> n >> k;
		double tr;
		cin >> tr;
		c.clear();
		for(int i = 0;i < n;i++){
			double a;
			cin >> a;
			c.pb(a);
		}
		sort(ALL(c));
		c.push_back(1);
		for(int i = 1;i <= n;i++){
			double diff = c[i]-c[i-1];
			double each = diff;
			each = min(each,tr/i);
			tr -= each * i;
			for(int j = 0;j < i;j++){
				c[j]+=each;
			}
		}
		double ans = 1;
		for (int i = 0;i < n;i++){
			ans*=c[i];
		}
		printf("Case #%d: %.8f\n",test,ans);
	}


    return 0;
}