#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    int cse = 1;
    while(t--) {
        int n,k;
        cin >> n >> k;
        long double u;
        cin >> u;
        long double machines[101];
        long double ort = 0;
        ort += u;
        for(int i=0;i<n;i++) {
            cin >> machines[i];
            ort += machines[i];
        }
        sort(machines,machines+n);
        printf("Case #%d: ", cse++);
        long double prob = 1.0;
        if(ort/n >= 1.0L) printf("%Lf\n", prob);
        else {
            int newn = n;
            long double last;
            int index;
            for(int i=n-1;i>=0;i--) {
                if(machines[i] - ort/newn > 1E-6) {newn--; ort-=machines[i];}
                else {index = i+1; last = ort/newn; break;}
            }
            long double res = 1;
            for(int i=n-1;i>=index;i--)
                res *= machines[i];
            for(int i=index-1;i>=0;i--)
                res *= last;
            printf("%Lf\n", res);
        }
    }
}
