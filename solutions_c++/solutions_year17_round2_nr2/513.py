#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<set>
#include<map>
#include<string.h>
#include<cstdio>
#include<queue>
using namespace std;
const int inf = 1000000001;
const int MOD = 1000000007;
typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())

//const int N = 100000;
//double s[N+1];
//int k[N+1];

int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    FOR(tt,1,t) {
        int n;
        int r,y,b,hz;
        cin>>n>>r>>hz>>y>>hz>>b>>hz;
        //N, R, O, Y, G, B, and V.
        vector<pair<int,char> > a;
        a.pb(mp(r, 'R'));
        a.pb(mp(b, 'B'));
        a.pb(mp(y, 'Y'));
        sort(a.begin(), a.end(), greater<pair<int,char> >());
        vector<int> pos;
        for(int i=0; i<n; i+=2) pos.pb(i);
        for(int i=1; i<n; i+=2) pos.pb(i);

        string ans="";FOR(i,1,n) ans+=" ";
        int inx=0;
        FOR(i,0,sz(a)-1)
        FOR(j,0,a[i].first-1) {
            ans[pos[inx]]=a[i].second;
            inx++;
        }

        bool ok=true;
        FOR(i,0,sz(ans)-1) if(ans[i]==ans[(i+1)%sz(ans)]) ok=false;

        cerr<<ans<<endl;

        if(!ok) ans="IMPOSSIBLE";
        cout<<"Case #"<<tt<<": ";
        
        cout<<ans<<endl;
        
    }
}
