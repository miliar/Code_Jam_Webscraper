#include <bits/stdc++.h>
using namespace std;
/*{{{*/  //template
#define REP(i,n) for(int i=0;i<n;i++)
#define rep(i,n) for(int i=0;i<n;i++)
#define INF 1<<29
#define LINF LLONG_MAX/3
#define MP make_pair
#define PB push_back
#define pb push_back
#define EB emplace_back
#define ALL(v) (v).begin(),(v).end()
#define all(v) ALL(v)
#define sz(x) (int)(x).size()
#define debug(x) cerr<<#x<<":"<<x<<endl
#define debug2(x,y) cerr<<#x<<","<<#y":"<<x<<","<<y<<endl
//struct fin{ fin(){ cin.tie(0); ios::sync_with_stdio(false); } } fin_;
struct Double{ double d; explicit Double(double x) : d(x){} };
ostream& operator<<(ostream& os,const Double x){ os << fixed << setprecision(20) << x.d; return os; }
template<typename T> ostream& operator<<(ostream& os,const vector<T>& vec){ os << "["; for(const auto& v : vec){ os << v << ","; } os << "]"; return os; }
template<typename T,typename U> ostream& operator<<(ostream& os,const pair<T,U>& p){ os << "(" << p.first << ","<< p.second <<")"; return os; }
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
ll gcd(ll a,ll b){ if(b==0) return a; else return gcd(b,a%b); }
constexpr double eps = 1e-14; 
constexpr ll mod = 1e9+7;
const int dx[]={1,0,-1,0} ,dy[] = {0,1,0,-1};
/*}}}*/



int R,C;

bool complete(const vector<string> & tbl){
    rep(i,R) rep(j,C) if(tbl[i][j]=='?') return false;
    return true;
}

void solve(){
    cin >> R >> C;
    vector<string> tbl(R);
    rep(i,R) cin>>tbl[i];

    map<char,bool> mp;
    rep(i,R) rep(j,C) if(tbl[i][j]!='?') mp[tbl[i][j]] = false;

    auto inp(tbl);

    rep(x,R) rep(y,C) if(tbl[x][y]!='?'){
        if(mp[tbl[x][y]]) continue;
        int lx=x,rx=x;
        int ly=y,ry=y;
        while(lx>=0){
            bool f=true;
            for(int i=lx;i<=rx;i++){
                for(int j=ly;j<=ry;j++){
                    if(i==x and j==y) continue;
                    if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                        f=false;
                        break;
                    }
                }
                if(!f) break;
            }
            if(!f) break;
            lx--;
        }
        lx++;
        while(rx<R){
            bool f=true;
            for(int i=lx;i<=rx;i++){
                for(int j=ly;j<=ry;j++){
                    if(i==x and j==y) continue;
                    if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                        f=false;
                        break;
                    }
                }
                if(!f) break;
            }
            if(!f) break;
            rx++;
        }
        rx--;
        while(ly>=0){
            bool f=true;
            for(int i=lx;i<=rx;i++){
                for(int j=ly;j<=ry;j++){
                    if(i==x and j==y) continue;
                    if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                        f=false;
                        break;
                    }
                }
                if(!f) break;
            }
            if(!f) break;
            ly--;
        }
        ly++;
        while(ry<=C){
            bool f=true;
            for(int i=lx;i<=rx;i++){
                for(int j=ly;j<=ry;j++){
                    if(i==x and j==y) continue;
                    if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                        f=false;
                        break;
                    }
                }
                if(!f) break;
            }
            if(!f) break;
            ry++;
        }
        ry--;
        for(int i=lx;i<=rx;i++) for(int j=ly;j<=ry;j++) tbl[i][j]=tbl[x][y];
        mp[tbl[x][y]] =true; 
    }

    if(!complete(tbl)){
        //cout << "ERROR" << endl;
        //rep(i,R) cout << inp[i] << endl;
        //exit(1);
        //return;

        tbl = inp;
        mp.clear();

        rep(i,R) rep(j,C) if(tbl[i][j]!='?') mp[tbl[i][j]] = false;

        rep(x,R) rep(y,C) if(tbl[x][y]!='?'){
            if(mp[tbl[x][y]]) continue;
            int lx=x,rx=x;
            int ly=y,ry=y;
            while(ly>=0){
                bool f=true;
                for(int i=lx;i<=rx;i++){
                    for(int j=ly;j<=ry;j++){
                        if(i==x and j==y) continue;
                        if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                            f=false;
                            break;
                        }
                    }
                    if(!f) break;
                }
                if(!f) break;
                ly--;
            }
            ly++;
            while(ry<=C){
                bool f=true;
                for(int i=lx;i<=rx;i++){
                    for(int j=ly;j<=ry;j++){
                        if(i==x and j==y) continue;
                        if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                            f=false;
                            break;
                        }
                    }
                    if(!f) break;
                }
                if(!f) break;
                ry++;
            }
            ry--;
            while(lx>=0){
                bool f=true;
                for(int i=lx;i<=rx;i++){
                    for(int j=ly;j<=ry;j++){
                        if(i==x and j==y) continue;
                        if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                            f=false;
                            break;
                        }
                    }
                    if(!f) break;
                }
                if(!f) break;
                lx--;
            }
            lx++;
            while(rx<R){
                bool f=true;
                for(int i=lx;i<=rx;i++){
                    for(int j=ly;j<=ry;j++){
                        if(i==x and j==y) continue;
                        if(tbl[i][j]!='?' and tbl[i][j]!=tbl[x][y]){
                            f=false;
                            break;
                        }
                    }
                    if(!f) break;
                }
                if(!f) break;
                rx++;
            }
            rx--;
            for(int i=lx;i<=rx;i++) for(int j=ly;j<=ry;j++) tbl[i][j]=tbl[x][y];
            mp[tbl[x][y]] =true; 
        }
    }

    for(int i=0;i<R;i++){
        cout << tbl[i] << endl;
    }
}

int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        printf("Case #%d:\n",i);
        solve();
    }
}
