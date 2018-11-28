
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned ll
#define db double
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PII pair<int, int>

const string INPUT_FILE = "input.txt";
const string OUTPUT_FILE = "a.txt";

const int N=1010;

int t;
int n;
db d;
db k[N],s[N];

bool ok(db speed) {
    db a=d/speed;
    for (int i=1;i<=n;i++) {
        db b=(d-k[i])/s[i];
        if (a<b) return false;
    }
    return true;
}

int main() {

    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);

    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++) {
        scanf("%lf%d",&d,&n);
        db tmn=1e10;
        for (int i=1;i<=n;i++) {
            scanf("%lf%lf",k+i,s+i);
            tmn=min(tmn,(d-k[i])/s[i]);
        }
        db lo=0.0;
        db hi=(d+1)/tmn;
        for (int i=0;i<300;i++) {
            db mid=(lo+hi)/2;
            if (ok(mid)) {
                lo=mid;
            } else {
                hi=mid;
            }
        }
        printf("Case #%d: %.6f\n",tt,lo);
    }
}