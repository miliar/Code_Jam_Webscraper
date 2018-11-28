#include <bits/stdc++.h>


#define debug(x) cerr<< #x << ": "<< x << endl;
#define print(x) cerr<< x << endl;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define REP(i,x,y) for(int i=x;i<y;i++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define sqr(x) ((x)*(x))

#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define ones(x) __builtin_popcountll(x)
using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAXN = 55;
ll p[MAXN];

const double EPS = 1e-9;

ll pp(string s){
    ll res = 0;
    REP(i,0,s.size()){
        if(s[i] =='.') continue;
        res *= 10;
        res += (s[i]-'0');
    }
    REP(i,0,2) {res *= 10;}
    return res;
}
double ans[MAXN];

double rr(ll r){
    double res = r;
    double s = 1e-6;
    return res*s;
}

int main(){
   fastio;
   int tests;
   cin >> tests;
   REP(test,0,tests){
       cerr<<"test "<<test<<endl;
       cout<<"Case #"<<test+1<<": ";
       int n , k;
       cin >> n >> k;
       string s;
       cin >> s;
       ll u = pp(s);

       REP(i,0,n) {cin >> s; p[i] = pp(s);}
       priority_queue<ll,vector<ll> ,greater<ll> > pq;
       REP(i,0,n) pq.push(p[i]);

       while(u > 0){
           ll val = pq.top();
           pq.pop();
           val += 1;
           u--;
           pq.push(val);
       }
       REP(i,0,n) {p[i] = pq.top(); pq.pop();}
       REP(i,0,n) ans[i] = rr(p[i]);
       double res = 1.0;
       REP(i,0,n) res *= ans[i];
       cout<<setprecision(12)<<fixed<<res<<endl;

   }
   return 0;
}
