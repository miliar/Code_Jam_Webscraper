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


struct s{
    int H,A,h,a,pocet;
};




int main(){
	ios::sync_with_stdio(false);
        cin.tie(0);


        int T;
        cin>>T;
        FOR(t,1,T){
            cout<<"Case #"<<t<<": ";

            
            int H,A,h,a,B,D;
            cin>>H>>A>>h>>a>>B>>D;

            map<pair<pll,pll>,int>M;
            queue<s>Q;
            Q.push({H,A,h,a,0});
            
            int res=-1;

            while(Q.size()>0){
                auto x = Q.front();
                Q.pop();
                //cout<<x.H<<" "<<x.A<<" "<<x.h<<" "<<x.a<<" "<<x.pocet<<endl;
                //cout<<" som tu"<<endl;
                if(M.find(MP(MP(x.H,x.A),MP(x.h,x.a)))!=M.end())
                    continue;
                M[MP(MP(x.H,x.A),MP(x.h,x.a))]=x.pocet;
                //attack
                s y=x;
                y.pocet++;
                y.h-=y.A;
                if(y.h<=0){
                    res=x.pocet+1;
                    break;
                }
                y.H-=y.a;
                if(y.H>0)
                    Q.push(y);
                //else
                    //cout<<"Zabil ma"<<endl;

                //buff
                y=x;
                y.pocet++;
                y.A+=B;
                y.H-=y.a;
                if(y.H>0)
                    Q.push(y);

                //cure
                y=x;
                y.pocet++;
                y.H=H;
                y.H-=y.a;
                if(y.H>0)
                    Q.push(y);

                //debuff
                y=x;
                y.pocet++;
                y.a=max(y.a-D,0);
                
                y.H-=y.a;
                if(y.H>0)
                    Q.push(y);
            }

            if(res==-1){
                cout<<"IMPOSSIBLE"<<endl;
            }
            else cout<<res<<endl;





        }





}
