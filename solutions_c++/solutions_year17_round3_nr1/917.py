#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

#define sqr(x) ((x)*(x))

typedef long long LL;

const double PI = 2*acos(0.0);

struct C {
    LL r, h, rh;
    void scan() {
        cin>>r>>h;
        rh=r*h;
    }
};

C a[1005];
bool comp(const C& a, const C& b) {
    return a.rh > b.rh;
}

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;cin>>cases;
    for(int caseno=1;caseno<=cases;caseno++) {
        int n,k;cin>>n>>k;
        for(int i=0;i<n;i++) {
            a[i].scan();
        }
        sort(a, a+n, comp);

        LL allRH=0, maxR=0;
        for(int i=0;i<k;i++) {
            allRH += a[i].rh;
            maxR = max(maxR, a[i].r);
        }
        //cerr<<maxR<<"\n";
        allRH*=2;

        LL base = sqr(maxR), extra=0.0, temp;
        for(int i=k;i<n;i++) {
            for(int j=0;j<k;j++) /*if(maxR<a[j].r)*/{
                temp = (sqr(a[i].r)+2*a[i].rh) - (sqr(maxR)+2*a[j].rh);
                extra = max(extra, temp);
            }
        }
        base+=extra;

        double ans = PI*(allRH+base);
        //cerr<<ans<<"\n";
        printf("Case #%d: %.8lf\n", caseno, ans);
    }
    return 0;
}
