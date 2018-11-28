#include"bits/stdc++.h"
using namespace std;
struct Pancakes {
    double r, h;
    double area;
}a[1050];
const double pi = acos(-1.0);
bool cmp(Pancakes A, Pancakes B)
{
    return A.area > B.area;
}
int main()
{
    freopen("A-large.in", "r",stdin);
    freopen("Aans.out", "w",stdout);
    int T;
    cin >> T;
    int n;
    int cas = 0;
    while(T --){
        int n, k;
        cin >> n >> k;
        for(int i = 1; i <= n; i ++){
            cin >> a[i].r >> a[i].h;
            a[i].area = 2.0 * a[i].r * pi * a[i].h;
        }
        sort(a + 1, a + 1 + n, cmp);
        double ans = 0;
        for(int i = 1; i <= n; i ++){
            int cnt = 1;
            double temans = a[i].r * a[i].r * pi + a[i].area;
            for(int j = 1; j <= n; j ++){
                if(j == i) continue;
                if(cnt == k){
                    break;
                }
                if(a[j].r <= a[i].r){
                    temans += a[j].area;
                    cnt ++;
                }
            }
            if(cnt == k){
                ans = max(ans, temans);
            }
        }
        printf("Case #%d: %.9f\n", ++cas, ans);
    }
    return 0;
}
