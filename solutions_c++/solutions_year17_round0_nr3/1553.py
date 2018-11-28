#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int T; cin>>T;
    for (int tt = 1; tt <= T; tt++) {
        unsigned long long N,K; cin>>N>>K;
        unsigned long long N1=0,N2=0,C1=0,C2=0;
        if (N & 1) {
            N1=N;C1=1;
        } else {
            N2=N;C2=1;
        }
        while(1) {
            if (K <= C1+C2) {
                unsigned long long max = (N1>N2) ? C1 : C2;
                unsigned long long d, l,r;
                if (K <= max) {
                    d = (N1>N2) ? N1 : N2;
                } else {
                    d = (N1>N2) ? N2 : N1;
                }
                l=r=d/2;
                if (~d & 1) {
                    r--;
                }
                cout << "Case #"<<tt<<": "<<l<<" "<<r<<"\n";
                break;
            }
            K -= C1+C2;
            unsigned long long n1=0,n2=0,c1=0,c2=0;
            if (C1) {
                if (N1/2 & 1) {
                    n1=N1/2;c1=2*C1;
                } else {
                    n2=N1/2;c2=2*C1;
                }
            }
            if (C2) {
                if (N2/2 & 1) {
                    n1=N2/2;n2=n1-1;
                } else {
                    n2=N2/2;n1=n2-1;
                }
                c1+=C2;c2+=C2;
            }
            N1=n1;N2=n2;C1=c1;C2=c2;
        }
    }
}
