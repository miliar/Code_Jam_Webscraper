#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {
    long test, n, i;
    double t, d, l, s;
    cin >> test;
    for(int k=1;k<=test;k++) {
        cin >> d >> n;
        t = 0;
        for(i=0;i<n;i++) {
            cin >> l >> s;
            l = d-l;
            if(l/s > t)
                t = l/s;
        }
        cout << "Case #" << k << ": ";
        printf("%0.6f\n", d/t);
    }
    return 0;
}