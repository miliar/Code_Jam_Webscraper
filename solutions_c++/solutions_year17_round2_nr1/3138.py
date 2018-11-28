#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++) {
        int D,N; cin>>D>>N;
        double max_time = 0;
        for (int i=0; i < N;i++) {
            int K,S;cin>>K>>S;
            double time = double(D - K) / (double)S;
            max_time = max(max_time, time);
        }
        double speed = (double)D / max_time;
        printf ("Case #%d: %f\n",tt, speed);
    }
}
