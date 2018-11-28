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

ll dp[20][2][10];

void mainmain(){
	int T;
	cin>>T;
	rep(turn,T){
		cout<<"Case #"<<turn+1<<": ";
		string s;
        cin>>s;
        int n = s.size();
        bool ok = true;
        rep(i,n-1){
            if(s[i] > s[i+1]) ok = false;
        }
        if(ok){
            cout<<s<<endl;
            continue;
        }
        ll ans = 1;
        rep(i,n){
            string t = s;
            if(s[i] == '0'){
                t[i] = '9';
                reep(j,i+1,n) t[j] = '9';
                bool ok = false;
                char num = '9';
                for(int j = i-1; j >= 0; j--){
                    if(ok){
                        mins(num, s[j]);
                        t[j] = num;
                    }
                    else{
                        if(s[j] != '0'){
                            mins(num, char(s[j]-1));
                            t[j] = num;
                            ok = true;
                        }
                        else{
                            t[j] = num;
                        }
                    }
                }
            }
            else{
                t[i] = s[i] - 1;
                char tt = t[i];
                for(int j = i-1; j >= 0; j--){
                    mins(tt, s[j]);
                    t[j] = tt;
                }
                reep(j,i+1,n) t[j] = '9';
            }
            ll tans;
            convert(t, tans);
            maxs(ans, tans);
        }
        cout<<ans<<endl;
        // dp[0][0][0] = 1;
        // rep(i,n){
        //     rep(j,10){
        //         dp[i+1][1][j] += dp[i][1][j];
        //         rep(k,j+1){
        //             dp[i+1][0][j] += dp[i][0][k];
        //             if(j<s[i]-'0') dp[i+1][0][j] += dp[i][1][k];
        //         }
        //     }
        //     // dp[i+1][0] += dp[i][0]*10;
        //     // dp[i+1][0] += dp[i][1]*(s[i]-'0');
        //     // dp[i+1][1] += dp[i][1];
        // }
	}
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<fixed<<setprecision(20);
    mainmain();
}