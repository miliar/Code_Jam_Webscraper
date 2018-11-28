#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007
#define PI 3.141592653589793238462643383279
int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		int n,k;
		cin>>n>>k;
		vector<ll> r(n),h(n);
		fore(i,0,n)
		{
		    cin>>r[i]>>h[i];
		}
		vector<pair<double, int> > sa(n);
		fore(i,0,n)
		{
		    sa[i].ff = (double)2*PI*r[i]*h[i];
		    sa[i].ss = i;
		}
		double fa = 0;
		fore(i,0,n)
		{
		    vector<double> best;
		    fore(j,0,n)
		    {
		        if(j == i) {
                    continue;
		        }
		        if(r[j]>r[i]) {
                    continue;
		        }
		        best.pb(sa[j].ff);
		    }
		    if(best.sz<k-1) {
                continue;
		    }
		    sort(best.rbegin(), best.rend());
		    double ans = sa[i].ff + PI*(double)r[i]*r[i];
		    fore(j,0,k-1)
		    {
		        ans+=best[j];
		    }
		    fa = max(fa, ans);
		}
		cout<<std::fixed<<setprecision(9)<<fa<<endl;
	}
	return 0;
}
