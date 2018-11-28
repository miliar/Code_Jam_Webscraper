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

int diff(int start, int endo)
{
    if(endo>start)
        return endo-start;
    else
        return 1440-start + endo;
}
int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);

		int ac, aj;
		cin>>ac>>aj;
		vector<pair<pii, bool> > times(ac+aj);
		fore(i,0,ac)
		{
		    cin>>times[i].ff.ff>>times[i].ff.ss;
		    times[i].ss = true;
		}
		fore(i,0,aj)
		{
		    cin>>times[ac+i].ff.ff>>times[ac+i].ff.ss;
		    times[ac+i].ss = false;
		}
		sort(times.begin(), times.end());
		int n = ac+aj;
		int ans = 0;
		vector<int> prefJ, prefC;
		int j = 720, c = 720;
		fore(i,0,n)
		{
		    if(times[i].ss) {
                c-=times[i].ff.ss-times[i].ff.ff;
		    }
		    else {
                j-=times[i].ff.ss-times[i].ff.ff;
		    }
		}
		fore(i,0,n-1)
		{
		    if(times[i].ss == times[i+1].ss)
            {
                ans+=2;
                if(times[i].ss) {
                    prefC.pb(-1*times[i].ff.ss + times[i+1].ff.ff);
                }
                else {
                    prefJ.pb(-1*times[i].ff.ss + times[i+1].ff.ff);
                }
            }
            else {
                ans++;
            }
		}
		if(n>0) {
            if(times[n-1].ss == times[0].ss)
            {
                ans+=2;
                if(times[n-1].ss) {
                    prefC.pb(1440 - times[n-1].ff.ss + times[0].ff.ff);
                }
                else {
                    prefJ.pb(1440 - times[n-1].ff.ss + times[0].ff.ff);
                }
            }
            else {
                ans++;
            }
		}
		sort(all(prefC));
		sort(all(prefJ));
		fore(i,0,prefC.sz)
		{
		    if(c>=prefC[i]) {
                c-=prefC[i];
                ans-=2;
		    }
		    else {
                break;
		    }
		}
		fore(i,0,prefJ.sz)
		{
		    if(j>=prefJ[i]) {
                j-=prefJ[i];
                ans-=2;
		    }
		    else {
                break;
		    }
		}
		cout<<ans<<endl;
	}
	return 0;
}
