/*
 * This is my code,
 * my code is amazing...
 */
//Template v3.0 alfa 1 
#include <bits/stdc++.h>
#define ll long long
#define lld long double
#define pll pair<ll,ll>
#define pld pair<lld,lld>
#define vll vector<ll>
#define vvll vector<vll>
#define vpll vector<pll>
#define vvpll vector<vpll>
#define INF 1000000000000000047
const char en='\n';
#define prime 47
#define lprime 1000000000000000009
#define lldmin LDBL_MIN
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define FOR(i,a,b) for(ll i=(ll)(a);i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=(ll)(a);i>=(ll)(b);i--)
#define REP(i,b) for(ll i=0;i<(ll)(b);i++)
#define FORE(i,b) for(auto i=(b).begin(); i!=(b).end(); i++)
#define sqr(a) (a)*(a)
#define dst(a,b) sqr((a).ff-(b).ff)+sqr((a).ss-(b).ss)
#define mdst(a,b) abs((a).ff-(b).ff)+abs((a).ss-(b).ss)
//debug
#define debug 1
#define dbg(x) if(debug) cout<<#x<<"="<<(x)<<";"<<endl;
using namespace std;

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>&par) {
  out<<par.ff<<" "<<par.ss<<en;
  return out;
}
template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  REP(i, v.size()){if(i) out<<" ";cout<<v[i];}
  return out;
}







int main(){
	ios::sync_with_stdio(false);
        cin.tie(0);


        int T;
        cin>>T;
        FOR(t,1,T){
            cout<<"Case #"<<t<<": \n";

            int r,c;
            cin>>r>>c;

            vvll  V(r,vll(c,0));

            REP(i,r)
                REP(j,c){
                    char c;
                    cin>>c;
                    V[i][j]=c;

                }

            REP(i,r){
                char last = '?';
                REP(j,c){
                    //najdi prve pismeno
                    if(V[i][j]!='?')
                        last=V[i][j];
                    V[i][j]=last;
                }
                last='?';
                FORD(j,c-1,0){
                    if(V[i][j]=='?')
                        V[i][j]=last;
                    last=V[i][j];                    
                }
            }

            REP(i,c){
                char last='?';
                REP(j,r){
                    if(V[j][i]!='?')
                        last=V[j][i];
                    V[j][i]=last;
                }
            }

            REP(i,c){
                char last='?';
                FORD(j,r-1,0){
                    if(V[j][i]!='?')
                        last=V[j][i];
                    V[j][i]=last;
                }
            }

            REP(i,r){
                REP(j,c){
                    cout<<(char)V[i][j];
                }
                cout<<endl;

            }


        }





}
