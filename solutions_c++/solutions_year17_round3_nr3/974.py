#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second
typedef long long ll;
typedef pair<int,int> pt;
const int base = 1000000007;
const int maxn = 100002;
const double eps = 1e-7;

int n, K;
double a[maxn], U, res;

bool cmp(double a, double b) {
    return a > b;
}

double abs(double a, double b) {if (a>b) return a-b; else return b-a;}

bool eq(double a, double b) {
    return abs(a-b) <= eps;
}

double getres() {
    int i;
    double res = 1;
    for (i=1;i<=n;i++) res *= min(double(1),a[i]);
    return res;
}

void solve(int test) {
    int i,j,k;

    cin >> n >> K;
    cin >> U;
    for (i=1;i<=n;i++) cin >> a[i];

    sort(a+1,a+n+1,cmp);
    n = K;
    a[n+1] = 1;
    sort(a+1,a+n+1);

    k = 0;
    while (U > 0) {
        if (eq(U,0) || U<0) break;

        sort(a+1,a+n+1);
        i = 1;
        while (eq(a[i],a[i+1])) i++;

        double diff = a[i+1] - a[i];
        if (U >= i*diff-eps) {
            U -= i*diff;
            for (j=1;j<=i;j++) a[j] = a[i+1];
        }
        else {
            for (j=1;j<=i;j++) a[j] += U/i;
            U = 0;
        }
    }

    printf("Case #%d: %.8lf\n",test,getres());
}

int main()
{
    int i,t;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    cin >> t;
    for (i=1;i<=t;i++) solve(i);

    return 0;
}

