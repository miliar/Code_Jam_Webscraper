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

struct node{
    ll L,R,diff;
    node(){};
    node(ll l,ll r) : L(l),R(r),diff(r-l-1){}
    bool operator < (const node & no) const {
        if(diff != no.diff) return diff < no.diff;
        else return L < no.L;
    }
    bool operator == (const node & no) const{
        return (L==no.L and R==no.R and diff==no.diff);
    }
};

void solve(){
    ll N,K;
    cin >> N >> K;
    priority_queue<node> que;
    que.push(node(0,N+1));
    rep(loop,K){
        auto p = que.top();
        que.pop();
        ll l = p.L, r = p.R, d = p.diff;

        ll x,y;
        if(d%2==0){
            x = l + (d/2)-1;
            y = l + (d/2)+1;
        }else{
            x = l + (d/2);
            y = l + (d/2)+2;
        }
        que.push(node(l,x+1));
        que.push(node(y-1,r));
        if(loop==K-1){
            if(d%2==0) cout << (d/2) << " " << (d/2)-1 << endl;
            else cout << d/2 << " " << d/2 << endl;
            return;
        }
    }
}

int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
