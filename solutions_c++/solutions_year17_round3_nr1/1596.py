#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int i = 1; i <= T; ++i) {
        int N, K; cin >> N >> K;
        vector<int> R(N, 0);
        vector<int> H(N, 0);
        for (int j = 0; j < N; ++j) {
            cin >> R[j] >> H[j];
        }

        double res = 0; --K;
        for (int j = 0; j < N; ++j) {
            // loop every possible pie as the bottom
            double area = double(R[j]) * R[j] + 2.0 * double(R[j]) * H[j];
            priority_queue<double> pq;
            for (int k = 0; k < N; ++k) {
                if (j == k) continue;
                if (R[k] > R[j]) continue;

                double tmp = 2.0 * double(R[k])*H[k];

                if (pq.size() < K) pq.push(-1.0 * tmp);
                else if (!pq.empty()) {
                    if (-1.0 * pq.top() < tmp) {
                        pq.pop(); pq.push(-1.0 * tmp);
                    }
                }
            }
            if (pq.size() == K) {
                while (!pq.empty()) {
                    area += pq.top() * -1.0; pq.pop();
                }
                res = max(res, area);
            }
        }

        double PI = 3.14159265358979323846;
        std::cout << std::fixed << std::setprecision(9);
        std::cout << "Case #" << i << ": " << (PI * res) << endl;
    }
}