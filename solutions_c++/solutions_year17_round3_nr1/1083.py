#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <ext/pb_ds/assoc_container.hpp>
#include <queue>
#include <map>
#include <ctime>
#include <iomanip>
#include <string.h>
#include <stdio.h>
#include <set>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define db puts("*****");
#define mid(x , y) ((x+y)>>1)
#define ff first
#define ss second
#define all(x)	x.begin(),x.end()
#define ll long long
#define sqr(x)	((x)*(x))
#define pii pair <int , int>
#define sz(x) int(x.size())
#define tr(it , c) for(__typeof(c.begin()) it = (c.begin()); it != (c.end()); it++)
#define y1 you_made_my_day

using namespace std;

const int N = 1e3+7;
const int INF = 1e9+7;
//const double PI = 3.1415926535897932384626433832795;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}

int n, m, t;
double a, b, c, d[N], e[N], dp[N][N];
vector <pair<double, double>> v;

int main(){
	freopen("file1.in", "r", stdin);
	freopen("file1.out", "w", stdout);
	
	cout.precision(12);
	scanf("%d", &t);
	
	for(int test=1; test<=t; test++){
		memset(dp, 0.0, sizeof(dp));
		memset(e, 0.0, sizeof(e));
		memset(d, 0.0, sizeof(d));
		
		v.clear();
		
		scanf("%d%d", &n, &m);
		
		for(int i=1; i<=n; i++)	scanf("%lf%lf", &d[i], &e[i]), v.pb(mp(d[i], e[i]));
		sort(all(v));
		for(int i=n-1; i>=0; i--)	d[n-i] = v[i].ff, e[n-i] = v[i].ss;
		
		for(int i=1; i<=n; i++){
			for(int j=0; j<=m; j++)	umax(dp[i][j], dp[i-1][j]);
			
			umax(dp[i][1], (2.0* M_PI *d[i])*e[i] + (M_PI*d[i]*d[i]));
			
			for(int j=1; j<m; j++)
				umax(dp[i][j+1], dp[i-1][j] + (2.0*M_PI*d[i])*e[i]);
		}
		
		cout << "Case #" << test << ": ";
		cout << fixed << dp[n][m] << endl;
	}
	
	return 0;
}

