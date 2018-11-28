#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int tmp_t = 0; tmp_t < T; tmp_t++) {
        long K, N;
        cin >> N >> K;
        map<long, long> A;
        A[N] = 1;
        long L, R;
        while (K > 0) {
            auto C = A.rbegin();
            if(K > C->second) {
                K = K - C->second;
                long tf = C->first, ts = C->second;
                A.erase(tf);
                if(tf % 2) {
                    if(A.find(tf / 2) == A.end()) {
                        A[tf / 2] = ts * 2;
                    }
                    else {
                        A[tf / 2] = A[tf / 2] + ts * 2;
                    }
                }
                else {
                    if(A.find(tf / 2) == A.end()) {
                        A[tf / 2] = ts;
                    }
                    else {
                        A[tf / 2] = A[tf / 2] + ts;
                    }
                    if(A.find((tf / 2) - 1) == A.end()) {
                        A[(tf / 2) - 1] = ts;
                    }
                    else {
                        A[(tf / 2) - 1] = A[(tf / 2) - 1] + ts * 2;
                    }
                }
            }
            else {
                long ts = K;
                K = 0;
                C -> second = (C -> second) - K;
                if(C->first % 2) {
                    if(A.find(C->first / 2) == A.end()) {
                        A[C->first / 2] = ts * 2;
                    }
                    else {
                        A[C->first / 2] = A[C->first / 2] + ts * 2;
                    }
                    L = R = C->first / 2;
                }
                else {
                    if(A.find(C->first / 2) == A.end()) {
                        A[C->first / 2] = ts;
                    }
                    else {
                        A[C->first / 2] = A[C->first / 2] + ts;
                    }
                    if(A.find((C->first / 2) - 1) == A.end()) {
                        A[(C->first / 2) - 1] = ts;
                    }
                    else {
                        A[(C->first / 2) - 1] = A[(C->first / 2) - 1] + ts * 2;
                    }
                    L = C->first / 2;
                    R = C->first / 2 - 1;
                }
            }
        }
        cout << "Case #" << tmp_t + 1<< ": " << L << " " << R << "\n";
    }
    return 0;
}