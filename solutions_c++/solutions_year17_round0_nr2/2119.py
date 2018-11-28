

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



int main() {
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++) {
        string s;
        cin >> s;
        int p = 0;
        for(int i = 1; i < SZ(s); i ++) {
            if(s[i] > s[i - 1]) p = i;
            if(s[i] < s[i - 1]) {
                s[p] --;
                for(int j = p + 1; j < SZ(s); j ++)
                    s[j] = '9';
                break;
            }
        }

        LL ans = 0;
        for(int i = 0; i < SZ(s); i ++) {
            ans = ans * 10 + s[i] - '0';
        }
        printf("Case #%d: %lld\n", cas, ans);
    }
}
