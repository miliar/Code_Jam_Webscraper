#include <bits/stdc++.h>
using namespace std;
#define int long long
using ll=long long;
using vi=vector<int>;
using vl=vector<long long>;
using pii=pair<int,int>;
using pll=pair<long long,long long>;
#define ITR(i,c) for(auto i=begin(c);i!=end(c);++i)
#define FORE(x,c) for(auto &x:c)
#define REPF(i,a,n) for(int i=a,i##_len=(int)(n);i<i##_len;++i)
#define REP(i,n) REPF(i,0,n)
#define REPR(i,n) for(int i=(int)(n);i>=0;--i)
#define REPW(i,n) for(i=0;i<(int)(n);++i)
#define ALL(c) begin(c),end(c)
#define RALL(c) rbegin(c),rend(c)   // c++14
#define SZ(c) ((int)c.size())
#define EXIST(c,x) (c.find(x)!=end(c))
#define OUTOFRANGE(y,x,h,w) (y<0||x<0||y>=h||x>=w)
#define dump(...)
const int DX[9]={0,1,0,-1,1,1,-1,-1,0},DY[9]={-1,0,1,0,-1,1,1,-1,0};
#define INF (1001001001)
#define INFLL (1001001001001001001ll)
template<class T> ostream& operator << (ostream &os,const vector<T> &v) {
    ITR(i,v) os << *i << (i==end(v)-1 ? "" : " "); return os; }
template<class T> istream& operator >> (istream &is,vector<T> &v) {
    ITR(i,v) is >> * i; return is; }
template<class T> istream& operator >> (istream &is, pair<T,T> &p) {
        is >> p.first >> p.second; return is; }
template<class T>bool chmax(T &a,const T &b){if(a<b){a=b;return 1;}return 0;}
template<class T>bool chmin(T &a,const T &b){if(b<a){a=b;return 1;}return 0;}
//------------------------------------------------------------------------------
struct before_main_function {
    before_main_function() {
        #ifdef int
            #undef INF
            #define INF INFLL
            #define stoi stoll
        #endif
        cin.tie(0);ios::sync_with_stdio(false);
        cout<<setprecision(15)<<fixed;
    }
} before_main_function;
//------------------------------------------------------------------------------

void solve(int t) {
    string s;
    cin>>s;
    int n=SZ(s);
    for(int i=n-1;i>0;i--) {
        if(s[i-1]>s[i]) {
            s[i-1]--;
            REPF(j,i,n) {
                s[j]='9';
            }
        }
    }
    cout<<"Case #"<<t+1<<": "<<stoi(s)<<endl;
}
signed main() {
    int T;
    cin>>T;
    REP(t,T) {
        solve(t);
    }
    return 0;
}

