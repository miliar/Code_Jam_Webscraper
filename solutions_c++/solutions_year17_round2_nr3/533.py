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

const int N = 101;
Int d[N+1][N+1];
Int e[N+1], s[N+1];
double ans[N+1];

int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    FOR(tt,1,t) {
        int n,q;
        cin>>n>>q;
        FOR(i,1,n) cin>>e[i]>>s[i];
        FOR(i,1,n) FOR(j,1,n) cin>>d[i][j];
        FOR(i,1,n) d[i][i]=0;
        FOR(w,1,n) FOR(i,1,n) FOR(j,1,n) if(d[i][w]!=-1 && d[w][j]!=-1) {
            if(d[i][j]==-1) d[i][j]=2000000001;
            d[i][j]=min(d[i][j], d[i][w]+d[w][j]);
        }

        FOR(i,1,n) {
            //FOR(j,1,n) cerr<<d[i][j]<<" ";cerr<<endl;
        }

        cout<<"Case #"<<tt<<":";
        
        while(q--) {
            int A,B;
            cin>>A>>B;
            FOR(i,1,n) ans[i]=1e+15;
            ans[A]=0;
            set<pair<double, int> >q;
            q.insert(mp(ans[A], A));
            while(!q.empty()) {
                int v = q.begin()->second;
                q.erase(q.begin());
                FOR(to,1,n) if(to!=v) if(d[v][to]!=-1 && e[v]>=d[v][to]) {
                    double tm = ans[v]+d[v][to]/double(s[v]);
                   //cerr<<v<<" "<<to<<" "<<tm<<" "<<d[v][to]<<" "<<s[v]<<endl;
                    if(tm<ans[to]) {
                        q.erase(mp(ans[to], to));
                        ans[to]=tm;
                        q.insert(mp(ans[to], to));
                    }
                }
            }
            printf(" %.8lf", (double)ans[B]);
        }
        cout<<endl;
    }
}
