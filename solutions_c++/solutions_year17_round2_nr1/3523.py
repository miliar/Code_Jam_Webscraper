#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

double d,n,k,s,mint;

int main() {
    freopen("A-large.in", "rb", stdin);
    freopen("out.txt", "wb", stdout);
    int T;
    cin>>T;
    for(int cas = 1; cas <= T; ++ cas) {
        cout<<"Case #"<<cas<<": ";
        cin>>d>>n;
        mint = 0;
        for(int i = 0; i < n; ++ i) {
            cin>>k>>s;
            mint = max(mint, (d - k) / s);
        }
        printf("%.6lf\n", d / mint);
    }
    return 0;
}