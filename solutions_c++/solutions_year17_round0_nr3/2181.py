


#include <cstdio>  
#include <cstring>  
#include <algorithm>  
#include <queue>  
#include <iostream>  
#include <string>  
#include <cmath>  
#include <vector>  
#include <set>  
#include <map>  
#include <bitset>  
#include <stack>  
using namespace std;  
  
#define REP(i,n) for ( int i=1; i<=int(n); i++ )    
#define MP make_pair  
#define PB push_back  
#define SZ(x) (int((x).size()))  
#define ALL(x) (x).begin(), (x).end()  
#define X first  
#define Y second  
template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }  
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }  
  
typedef long long LL;  
typedef long double LD;  
const int INF = 0x3f3f3f3f;

map<LL, LL> mp;

int main() {
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++) {
        mp.clear();
        LL n, K;
        cin >> n >> K;
        mp[n] = 1;
        while(true) {
            auto it = mp.rbegin();
            K -= it->Y;
            if(K <= 0) {
                printf("Case #%d: %lld %lld\n", cas, it->X / 2, (it->X - 1) / 2);
                break ;
            }
            if(it->X & 1) {
                mp[it->X / 2] += it->Y * 2;
            } else {
                mp[it->X / 2] += it->Y;
                mp[it->X / 2 - 1] += it->Y;
            }
            mp.erase(it->X);
        }
    } 
}
