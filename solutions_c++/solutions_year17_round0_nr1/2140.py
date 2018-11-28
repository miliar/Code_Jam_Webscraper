

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

const int N = 1e3 + 100;
char str[N];
int cas;
int main() {
    int T;
    cin >> T;
    while(T --) {
        int K, n;
        scanf("%s%d", str, &K);        
        n = strlen(str);
        bool flag = 0;
        int ans = 0;
        for(int i = 0; i < n; i ++) 
            if(str[i] == '-') {
                ans ++;
                if(i + K > n) flag = 1;
                else {
                    for(int j = 0; j < K; j ++)
                        str[i + j] = str[i + j] == '+' ? '-' : '+';
                }
            } 
        if(flag) printf("Case #%d: IMPOSSIBLE\n", ++ cas);
        else printf("Case #%d: %d\n", ++ cas, ans);
    }
}
