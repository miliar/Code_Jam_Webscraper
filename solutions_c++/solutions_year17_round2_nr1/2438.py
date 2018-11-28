#include <bits/stdc++.h>
#define X first
#define Y second
#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,b,a) for(int i=(b);i>=(a);i--)
using namespace std;
using LL = long long;
using PII = pair<int, int>;

const int N = 1005;
int n, d;

void work(int testCase) {
    scanf("%d%d", &d, &n);
    double timeReach = 0;
    FI(i,1,n) {
        int k, s;
        scanf("%d%d", &k, &s);
        double t = (double)(d-k) / s;
        timeReach = max(timeReach, t);
    }
    printf("Case #%d: %f\n", testCase, d / timeReach);
}

int main() {
    int T;
    scanf("%d", &T);
    FI(i,1,T) work(i);
}