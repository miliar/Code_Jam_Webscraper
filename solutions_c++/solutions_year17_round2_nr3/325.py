#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iterator>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <utility>
#include <memory>
#include <functional>
#include <deque>
#include <cctype>
#include <ctime>
#include <numeric>
#include <list>
#include <iomanip>

#if __cplusplus >= 201103L
#include <array>
#include <tuple>
#include <initializer_list>
#include <forward_list>

#define cauto const auto&
#else

#endif

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
    v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
    stringstream ss;
    ss << f;
    ss >> t;
}

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define reep(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n) reep((i),0,(n))
#define ALL(v) (v).begin(),(v).end()
#define PB push_back
#define F first
#define S second
#define mkp make_pair
#define RALL(v) (v).rbegin(),(v).rend()
#define DEBUG
#ifdef DEBUG
#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#else
#define dump(x) 
#define debug(x) 
#endif

#define MOD 1000000007LL
#define EPS 1e-8
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define maxs(x,y) x=max(x,y)
#define mins(x,y) x=min(x,y)

void mainmain(){
    int T;
    cin>>T;
    rep(turn, T){
        cout<<"Case #"<<turn+1<<": ";
        int n;
        cin>>n;
        int Q;
        cin>>Q;
        vector<pll> uma(n);
        rep(i,n) cin>>uma[i].F>>uma[i].S;
        vvll vv;
        initvv(vv, n, n);
        rep(i,n){
            rep(j,n){
                cin>>vv[i][j];
                if(vv[i][j] == -1) vv[i][j] = INFL;
            }
        }
        rep(i,n) vv[i][i] = 0;
        rep(k,n) rep(i,n) rep(j,n){
            mins(vv[i][j], vv[i][k]+vv[k][j]);
        }
        VV(double) ww;
        initvv(ww, n, n, 1e20);
        rep(i,n){
            rep(j,n){
                if(vv[i][j] <= uma[i].F){
                    mins(ww[i][j], 1.*vv[i][j]/uma[i].S);
                }
            }
        }
        rep(_,n){
            rep(i,n){
                rep(j,n){
                    rep(k,n){
                        if(vv[i][k] <= uma[i].F){
                            mins(ww[i][j], 1.*vv[i][k]/uma[i].S + ww[k][j]);
                        }
                    }
                }
            }
        }
        rep(_, Q){
            int a,b;
            cin>>a>>b;
            a--,b--;
            if(_) cout<<" ";
            cout<<ww[a][b];
        }
        cout<<endl;
    }
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<fixed<<setprecision(20);
    mainmain();
}