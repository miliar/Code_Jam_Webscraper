#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <queue>
extern "C" {
#include <stdint.h>
}

using namespace std;

int main(int argc, char *argv[])
{
    ios::sync_with_stdio(true);
    int T;
    cin >> T;
    for (int t = 0 ; t < T ; t++) {
        int N, K;
        cin >> N >> K;
        priority_queue<int> PQ;
        int top = N;
        PQ.push(N);

        int mx = -1, mn = -1;
        for (int i = 0 ; i < K ; i++) {
            if (!PQ.empty()) {
                top = PQ.top();
                PQ.pop();
            }
            // cout << "top=" << top << " " << endl;
            if (top % 2 == 1) {
                int k = (top - 1)/ 2;
                if (k >= 0) {
                    PQ.push(k);
                    PQ.push(k);
                    // cout << "k=" << k <<endl;
                    // cout << "k=" << k <<endl;
                    mx = mn = k;
                }    
            } else {
                int k1 = top/2-1;
                if (k1 >= 0 ) {
                    PQ.push(k1);
                    // cout << "k1=" << k1 <<endl;
                    mn = k1;
                }
                int k2 = top/2;
                if (k2 >= 0) {
                    PQ.push(k2);
                    // cout << "k2=" << k2 <<endl;
                    mx = k2;
                }        
            }
        }

        cout << "Case #" << t+1 << ": " << mx << " " << mn << endl;
    }

    return 0;
}
