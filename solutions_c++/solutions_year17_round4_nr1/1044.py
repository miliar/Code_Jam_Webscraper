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
            cout<<"Case #"<<t<<": ";

            int n,p;
            cin>>n>>p;

            vll V(4,0);

            
            REP(i,n){
                int x;
                cin>>x;
                V[x%p]++;
            }
            
            
            if(p==1){
                cout<<V[0]<<endl;
            }
            else if(p==2){
                cout<<V[0]+V[1]/2+V[1]%2<<endl;;
            }
            else if(p==3){
                int pocet=V[0];

                int komb=min(V[1],V[2]);
                V[1]-=komb;
                V[2]-=komb;
                pocet+=komb;
                
                pocet+=V[1]/3+(V[1]%3!=0);
                pocet+=V[2]/3+(V[2]%3!=0);
                cout<<pocet<<endl;
            }
            else if(p==4){
                int pocet=V[0];

                int komb=min(V[1],V[3]);
                V[1]-=komb;
                V[3]-=komb;
                pocet+=komb;

                if(V[1]>0){
                    komb=min(V[1]/2,V[2]);
                    V[1]-=2*komb;
                    V[2]-=komb;
                    pocet+=komb;
                }
                if(V[3]>0){
                    komb=min(V[3]/2,V[2]);
                    V[3]-=2*komb;
                    V[2]-=komb;
                    pocet+=komb;
                }

                komb=V[2]/2;
                V[2]-=komb*2;
                pocet+=komb;

                komb=V[1]/4;
                V[1]-=komb*4;
                pocet+=komb;

                komb=V[3]/4;
                V[3]-=komb*4;
                pocet+=komb;

                pocet+=(V[1]+V[2]+V[3]>0);

                cout<<pocet<<endl;

            }
        


	}
}
