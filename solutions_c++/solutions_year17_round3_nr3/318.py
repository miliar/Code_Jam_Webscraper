#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";

        int N, K; cin >> N >> K;
        double U; cin >> U;

        vector<double> P(N);

        for(int i = 0; i < N; i++)
            cin >> P[i];

        sort(P.begin(),P.end());
        
        for(int i = 0; i < N; i++) {
            double gap;
            if(i < N-1)
                gap = P[i+1] - P[i];
            else
                gap = 1 - P[i];

            if((i+1)*gap <= U) {
                U -= (i+1)*gap;
                for(int j = 0; j <= i; j++) {
                    P[j] += gap;
                }
            }
            else {
                for(int j = 0; j <= i; j++) {
                    P[j] += U/(i+1.0);
                }
                break;
            }

        }
        double prod = 1;
        for(int i = 0; i < N; i++) {
            prod *= P[i];
        }

        printf("%.8lf\n", prod);
    }
    return 0;
}
