/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

const int N = 1005;

vpii vp;
double dp[N][N];
int n,k;

ld a(int r)
{
    return (ld)r*(ld)r*PI;
}

ld b(int r,int h)
{
    return (ld)r*(ld)h*2.0*PI;
}
 
ld f(int ii,int m)
{
    if(!m) return 0;
    if(ii>=n) return -eps;
    if(dp[ii][m] != -1.0) return dp[ii][m];
    
    ld ret(0);
    int r = vp[ii].first;
    int h = vp[ii].second;

    if(m == 1) return dp[ii][m] = b(r,h);

    rep2(i, ii+1, n) {
        ld sur = b(r,h);
        ret = max(ret,sur + f(i,m-1));
    }

    return dp[ii][m] = ret;
}

int main(int argc, char *args[]) {
	
	int T;    
    int A, B;

    cin >> T;

    rep2(t,1,T+1) {
        cin>>n>>k;
        
        vp.clear();

        rep(i, n) {
            int r,h;
            cin>>r>>h;
            vp.push_back(mp(r,h));
        }
        sort(vp.rbegin(), vp.rend());

        rep(i, n) {
            for(int j=0;j<=n;++j) dp[i][j] = -1.0;
        }

        ld res = 0.0;
        rep(i, n-k+1) {
            res = max(res, a(vp[i].first) + f(i,k));
        }

        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(9) << res << endl;
    }
	
    return 0;
}