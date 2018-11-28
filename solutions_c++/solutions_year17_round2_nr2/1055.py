#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef long double ld;

#define rep(i,a,b) for(ll i=a;i<=b;++i)
#define rev(i,a,b) for(ll i=a;i>=b;i--)
#define pll pair<ll,ll>
#define vll vector<ll>
#define sll set<ll>
#define vpll vector<pll>
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ln length()
#define M 1000000007
ll t,n,r,o,y,g,b,v;

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("B-small-attempt0 (3).in");
    ofstream fout;fout.open("samll.txt");

    fin>>t;
    rep(tt,1,t){

        fin>>n>>r>>o>>y>>g>>b>>v;
        string ans="";
        if(b<2*o || r < 2*g || y < 2*v) {
            ans="IMPOSSIBLE";
            fout<<"Case #"<<tt<<": "<<ans<<'\n';
            continue;
        }
        b-=o;r-=g;y-=v;
        pair<ll,char> x[5];x[1]=mp(b,'B');x[2]=mp(r,'R');x[3]=mp(y,'Y');
        sort(x+1,x+4);

        if(b==r && b==y){
            rep(i,1,b) ans+="BRY";
        }

        else{
            while(x[2].F > x[1].F){
                ans.pb(x[3].S);
                ans.pb(x[2].S);
                x[3].F--;x[2].F--;
            }
            while(x[3].F > x[2].F && x[2].F>0){
                ans.pb(x[3].S);
                ans.pb(x[2].S);
                ans.pb(x[3].S);
                ans.pb(x[1].S);
                x[3].F-=2;x[2].F--;x[1].F--;
            }
            if(x[3].F>x[2].F){
                ans="IMPOSSIBLE";
            }
            else{
                if(x[3].F<x[2].F){
                    ans.pb(x[2].S);
                    ans.pb(x[1].S);
                    x[2].F--;x[1].F--;
                }
                while(x[1].F--){
                    ans.pb(x[3].S);
                    ans.pb(x[2].S);
                    ans.pb(x[1].S);
                }
            }
        }

        if(ans=="IMPOSSIBLE") fout<<"Case #"<<tt<<": "<<ans<<'\n';
        else{
            fout<<"Case #"<<tt<<": ";
            rep(i,0,ans.ln-1){
                if(ans[i]=='B' && o>0){
                    fout<<"BOB";
                    o--;
                }
                else if(ans[i]=='B') fout<<"B";

                else if(ans[i]=='R' && g>0){
                    fout<<"RGR";
                    g--;
                }
                else if(ans[i]=='R') fout<<"R";

                else if(ans[i]=='Y' && v>0){
                    fout<<"YVY";
                    v--;
                }
                else if(ans[i]=='Y') fout<<"Y";
            }
            fout<<'\n';
        }
    }
}
