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

const double PI = acos(-1.0);
const double INF = 1e16;
int n;
vector<pair<double,double> > data;

double dp[1020][1020];

int solved[1020][1020];
double go(int pos, int cant){
    if(cant < 0) return -INF;
    if(pos == n){
        if(cant == 0) return 0;
        else return -INF;
    }
    if(solved[pos][cant] ) return dp[pos][cant];
    double val1 = data[pos].fst * data[pos].snd + go(pos+1,cant-1);
    double val2 = go(pos+1, cant);

    solved[pos][cant] = 1;
    return dp[pos][cant]=max(val1,val2);
}

int main(){
   fastio;
   int tests;
   cin >> tests;
   REP(test,0,tests){
       cerr<<"test "<<test<<endl;
       cout<<"Case #"<<test+1<<": ";
       int K;
       cin >> n >> K;
       data.clear();
       REP(i,0,n){
           int a, b;
           cin >> a >> b;
           data.pb(mp(a,b));
       }
       sort(rall(data));
       double res = 0.0;
       REP(i,0,n+10) REP(j,0,K + 10) solved[i][j] = 0;
       REP(i,0,n){
           double val = PI*sqr(data[i].fst) + 2*PI*(data[i].fst*data[i].snd + go(i+1,K-1));
           res = max(res,val);
       }
       cout<<setprecision(12)<<fixed<<res<<endl;


   }
   return 0;
}
