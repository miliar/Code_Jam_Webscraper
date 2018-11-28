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





bool da(int pocet, int val, int ing){
    return pocet*ing*9<=val*10 && pocet*ing*11>=val*10;

}

bool male(int pocet, int val, int ing){
    return pocet*ing*9>val*10;
}

bool velke(int pocet, int val, int ing){
    return pocet*ing*11<val*10;
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
            vll V(n);
            REP(i,n)
                cin>>V[i];
            vector<multiset<int>> I;
            I.resize(n+1);

            REP(i,n)
                REP(j,p){
                    int x;
                    cin>>x;
                    I[i].insert(x);
                }
            
            int pocet=1;
            int balikov=0;
            while(true){
                //cout<<"pocet="<<pocet<<endl; 
                int vel=0;
                int koniec=0;
                REP(i,n){
                    while(I[i].size()>0 && male(pocet, *I[i].begin(), V[i])){
                        //cout<<*I[i].begin()<<" je moc male pre "<<pocet<<endl;
                        I[i].erase(I[i].begin());
                    }

                    if(I[i].size()==0){
                        koniec=1;
                        break;
                    }
                    if(velke(pocet, *I[i].begin(), V[i]))
                        vel=1;
                }
                if(koniec){
                    //cout<<"koniec"<<endl;
                    break;
                }

                if(vel){
                    //cout<<"velke"<<endl;
                    pocet++;
                    continue;
                }
                balikov++;
                REP(i,n){
                    I[i].erase(I[i].begin());

                }


            }
            cout<<balikov<<endl;

        }





}
