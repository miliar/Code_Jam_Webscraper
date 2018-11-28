#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
using namespace std;

int P;
int cashe[101][101][101][4];
int back(int n1, int n2, int n3, int s) {
    int& ret = cashe[n1][n2][n3][s];
    if(ret != -1) return ret;
    ret = 0;
    
    if(n1 >0) ret = max(ret, back(n1-1, n2, n3, (s+1)%P));
    if(n2 >0) ret = max(ret, back(n1, n2-1, n3, (s+2)%P));
    if(n3 >0) ret = max(ret, back(n1, n2, n3-1, (s+3)%P));
    
    if((n1 >0 || n2 >0 || n3 >0) && s==0) ret += 1;
    return ret;
}

int main () {
    freopen("/Users/bowbowbow/Downloads/A-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/A-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        memset(cashe, -1, sizeof(cashe));
        cout << "Case #" << t << ": ";
        
        int N;
        cin >> N >> P;
        
        int ans = 0;
        vector<int> cnt (4, 0);
        for(int i=1, t;i<=N;i++) {
            cin >> t;
            if(t%P == 0) ans++;
            else cnt[t%P]++;
        }
        ans += back(cnt[1], cnt[2], cnt[3], 0);
        cout << ans << endl;
    }
    return 0;
}
