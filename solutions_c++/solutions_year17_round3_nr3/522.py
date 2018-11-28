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
		double u;
		cin>>u;
		vector<double> p(n);
        double can = 0;
		fore(i,0,n)
		{
		    cin>>p[i];
		    can+=1-p[i];
		}
		//cout<<u<<" "<<can<<endl;
		sort(all(p));
		p.pb(1.0);
		vector<double> diff(n);
		fore(i,0,n)
		{
		    diff[i] = p[i+1]-p[i];
		}
		fore(i,0,n)
		{
		    if(u>=diff[i]*(i+1)) {
                u-=diff[i]*(i+1);
                fore(j,0,i+1)
                {
                    p[j] = p[i+1];
                }
		    }
		    else {
                double each = u/(i+1);
                u = 0;
                fore(j,0,i+1)
                {
                    p[j]+=each;
                }
                break;
		    }
		    /*fore(j,0,n)
		    {
		        cout<<p[j]<<" ";
		    }
		    cout<<endl;*/
		}
		double fa = 1;
		fore(i,0,n)
		{
		    fa*=p[i];
		}
		cout<<std::fixed<<setprecision(9)<<fa<<endl;
	}
	return 0;
}
