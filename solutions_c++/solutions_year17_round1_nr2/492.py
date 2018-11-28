#include<bits/stdc++.h>
using namespace std;
#define inc(i,x) for(int i=0;i<x;i++)
#define onc(i,x) for(int i=1;i<=x;i++)
int n,p;
int r[55];
int q[55][55];
typedef pair<int,int> pii;
#define f first
#define s second
#define pb push_back
#define sz(x) ((int)x.size())
vector<pii> al[55];
int pt[55];
int solve()
{
    ///[lb,ub]
    inc(i,n) if(pt[i]==sz(al[i])) return 0;
    int line=al[0][pt[0]].f;
    inc(i,n) line=max(line,al[i][pt[i]].f);
    bool f=0;
    inc(i,n){
        if(al[i][pt[i]].f<=line&&line<=al[i][pt[i]].s){
            ///good;
        }
        else{
            f=1;
            pt[i]++;
        }
    }
    if(f) return solve();

    inc(i,n) pt[i]++;
    return solve()+1;
}
main()
{
    int t;
    cin>>t;
    onc(kase,t){
        cin>>n>>p;

        inc(i,n) cin>>r[i];
        inc(i,n){
            inc(j,p){
                cin>>q[i][j];
            }
        }

        inc(i,n){
            al[i].clear();
            inc(j,p){
                int lb=ceil((double)q[i][j]/r[i]/1.1)+0.5;
                int ub=floor((double)q[i][j]/r[i]/0.9)+0.5;
                if(lb<=ub)
                    al[i].pb({lb,ub});///[lb,ub]
                //printf("{%d,%d}\n",lb,ub);
            }
            sort(al[i].begin(),al[i].end());
        }

        cout<<"Case #"<<kase<<": ";
        memset(pt,0,sizeof(pt));
        cout<<solve()<<"\n";
    }
}

