#include <bits/stdc++.h>
using namespace std;

typedef pair <int, int> pii;
const double PI = acos(-1);
const int MAX = 1001;
int test, n, m, k;
pii cake[MAX];
double res, tmp, a[MAX];

double area(const double& r){
    return r * r * PI;
}

double perimetor(const double& r){
    return 2 * r * PI;
}

double cal(const double r, const double h){
    return perimetor(r) * h;
}

int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int tt = 1; tt <= test; ++tt){
        scanf("%d %d", &n, &k);
        for (int i = 1; i <= n; ++i)
            scanf("%d %d", &cake[i].first, &cake[i].second);
        sort(cake + 1, cake + 1 + n);
        res = 0;
        for (int i = k; i <= n; ++i){
            tmp = cal(cake[i].first, cake[i].second) + area(cake[i].first);
            m = i - 1;
            for (int j = 1; j <= m; ++j){
                a[j] = cal(cake[j].first, cake[j].second);
            }
            sort(a + 1, a + 1 + m, greater <double>());
            for (int j = 1; j < k; ++j)
                tmp += a[j];

            res = max(res, tmp);
        }
        printf("Case #%d: %.9f\n", tt, res);
    }
    return 0;
}
