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

int day[1500];
const int m  = 24*60;
const int INF = 1e9;
int totblack, totred;

int dp[m+10][m/2+10][2][2];

int go(int pos, int cblack, int cur, int ini){
    int cred = pos - cblack;
    if(cblack > totblack || cred > totred){
        return INF;
    }
    if(pos == m){
        if(cblack == totblack){
            if(cur == ini) return 0;
            else return 1;
        }else return INF;
    }

    if(dp[pos][cblack][cur][ini] != -1) return dp[pos][cblack][cur][ini];

    int res = INF;
    if(day[pos] != -1){
        int w, nblack;
        if(day[pos] == cur) w = 0;
        else w = 1;
        if(day[pos] == 0) nblack = cblack + 1;
        else nblack = cblack;

        int val = w + go(pos+1,nblack, day[pos], ini);
        res = min(val,res);
    }else{
        int nblack = cblack + 1;
        int w =0;
        if(cur) w++;
        int val1 = w + go(pos+1,nblack,0,ini);

        nblack = cblack;
        w = 0;
        if(!cur) w++;
        int val2 = w + go(pos+1,nblack, 1,ini);

        res = min(res,min(val1,val2));
    }

    return dp[pos][cblack][cur][ini] = res;
}

int main(){
   fastio;
   int tests;
   cin >> tests;
   REP(test,0,tests){
       cerr<<"test "<<test<<endl;
       cout<<"Case #"<<test+1<<": ";
       int ac, aj;
       cin >> ac >> aj;
       REP(i,0,m) day[i] = -1;
       totred = totblack = 720;
       REP(i,0,ac){
           int c,d;
           cin >> c >> d;
           REP(j,c,d) day[j] = 0;
       }
       REP(i,0,aj){
           int c,d;
           cin >> c >> d;
           REP(j,c,d) day[j] = 1;
       }
       REP(i,0,m+10)REP(j,0,m/2+10)REP(k,0,2)REP(ini,0,2) dp[i][j][k][ini] = -1;
       int res;
       if(day[0] == -1){
           int val1 = go(1,1,0,0);
           int val2 = go(1,0,1,1);
           res = min(val1,val2);
       }else{
           int val;
           if(day[0]){
               val = go(1,0,1,1);
           }else{
               val = go(1,1,0,0);
           }
           res = val;
       }

       cout<<res<<endl;

   }
   return 0;
}
