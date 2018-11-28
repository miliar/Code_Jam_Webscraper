#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

#define err 1e-10

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;cin>>cases;
    for(int caseno=1;caseno<=cases;caseno++) {
        int n,k;cin>>n>>k;
        double hand;cin>>hand;
        vector<double> a(n);
        double rest = 0.0;
        double ans = 0.0;
        for(int i=0;i<n;i++) {
            cin>>a[i];
            rest += 1.0 - a[i];
        }

        double beg = 0.0, end = 1.0, mid, temp, x, mul;

        //cerr<<hand<<"\n"<<rest<<"\n";
        if(hand - rest > -err) {
            //cerr<<"here\n";
            ans = 1.0;
            goto END;
        }

        for(int loop=100; loop>0 && end - beg > err; loop--) {
            mid = (beg+end)/2;

            vector<double> b = a;
            temp = hand;

            bool f=true;
            for(int i=0;i<n;i++) {
                if(b[i]<mid) {
                    if(mid-b[i] > temp - err) {
                        f = false;
                        break;
                    }
                    temp -= mid-b[i];
                    b[i] = mid;
                }
            }
            if(!f) {
                end = mid;
                continue;
            }
            mul = 1.0;
            for(int i=0;i<n;i++) mul *= b[i];
            if(mul > ans) ans = mul;
            beg = mid;
        }

    END:;
        printf("Case #%d: %.8lf\n", caseno, ans);
    }
    return 0;
}
