#include <iostream>
#include <cstdio>
using namespace std;

int N, D;

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        cin>>D>>N;
        double time = 0;
        for (int i=0; i<N; i++) {
            int k, s; cin>>k>>s;
            int d = D - k;
            time = max(time, double(d)/s);
        }
//     <<"Case #"<<t<<": "<<(D/time)<<endl;
        printf("Case #%d: %.9lf\n", t, (D/time));
    }
    return 0;
}
