#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int maxn = 110;

typedef long long LL;
struct node {
    node(){}
    node(LL x, LL y) : x(x), y(y){}
    LL x, y;
};
int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        long long n, k;
        cin >> n >> k;
        

        node a, b;
        a = node(n, 1);
        b = node(n-1, 0);
        LL sum = 0;
        LL ans = 0;
        while (sum < k) {
            node c(-1, 0), d(-1, 0);
            if (a.x %2 == 1) {
                c = node(a.x/2, a.y*2+b.y);
                d = node(b.x/2-1, b.y);
                sum += a.y;
                if (sum >= k) {
                    ans = a.x;
                    break;
                }
                
                sum += b.y;
                if (sum >= k) {
                    ans = b.x;
                    break;
                }
            } else {
                c = node(a.x/2, a.y);
                d = node(b.x/2, a.y+b.y*2);
                
                sum += a.y;
                if (sum >= k) {
                    ans = a.x;
                    break;
                }
                
                sum += b.y;
                if (sum >= k) {
                    ans = b.x;
                    break;
                }
                
            }
            a = c;
            b = d;
        }
        
        LL l, r;
        l = ans/2;
        r = ans-1-l;
        if (r > l) swap(l, r);
        printf("Case #%d: ", ++cas);
        cout << l << " " << r << endl;
    }
}