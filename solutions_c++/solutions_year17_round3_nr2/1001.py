// #pragma comment(linker,"/STACK:102400000,102400000")
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

typedef long long ll;

struct foo{
        int col;
        int l, r;
        friend bool operator<(const foo &x, const foo &y){
            return x.l < y.l;
            }
        };

foo p[10007];
int res;

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    int n, m;
    for(int cas = 0; cas < t; cas++){
        cin >> n >> m;
        res = 2;
        cout << "Case #" << cas + 1 << ": ";
        if(n+m <= 2){
            for (int i = 0; i < n; i ++ ) {
                cin >> p[i].l >> p[i].r;
                p[i].col = -1;
            }
            for (int i = 0; i < m; i ++) {
                cin >> p[i+n].l >> p[i+n].r;
                p[i].col = 1;
            }
            sort(p, p + n + m);
            if(n + m == 1 || n == 1 || m == 1) res=2;
            else if(n == 0 || m == 0){
                if(p[2].r-p[1].l <= 720 || 1440 - p[2].l + p[1].r <= 720) {
                    res = 2;
                } 
                else {
                    res = 4;
                } 
            }
        }
        printf("%d\n", res);
    }
    return 0;;
}

