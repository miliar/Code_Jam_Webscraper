#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
typedef long long ll;


int T;

int n, k;
pair<double,double> a[1234567];

#define PI 3.14159265359

int main() {
    scanf("%d", &T);
    fo(_,1,T+1) {
        printf("Case #%d: ", _);
        scanf("%d %d", &n, &k);
        fo(i,0,n) scanf("%lf %lf", &a[i].first, &a[i].second), a[i].second *= a[i].first * 2 * PI;
        sort(a, a+n);
        double sm=0, ans = 0;
        multiset<double> s;
        fo(i,0,n) {
            if (s.size() == k-1) {
                double cur = sm + a[i].second + PI * a[i].first * a[i].first;
                
                //printf("c %lf\n", cur);
                
                ans = max(ans, cur);
            }
            sm += a[i].second;
            s.insert(a[i].second);
            if (s.size() >= k) {
                sm -= *s.begin();
                s.erase(s.begin());
            }
        }
        printf("%.9lf\n", ans);
    }

    return 0;
}
