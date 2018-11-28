#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;cin>>cases;
    for(int caseno=1;caseno<=cases;caseno++) {
        int n, di, ki, si; cin >> di >> n;
        double d = (double)di, t, mx=0.0;
        for(int i=0;i<n;i++) {
            cin>>ki>>si;
            t = (d-ki)/si;
            if(t>mx) mx = t;
        }
        printf("Case #%d: %.8lf\n", caseno, d/mx);
        //cerr<<(d/mx)<<"\n";
    }
    return 0;
}
