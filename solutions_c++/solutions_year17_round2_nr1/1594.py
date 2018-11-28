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

        int D, N; cin >> D >> N;

        vector<double> K(N), S(N);

        for(int i = 0; i < N; i++) {
            cin >> K[i] >> S[i];
        }

        double dtime = 0;
        for(int i = 0; i < N; i++) {
            dtime = max(dtime, (D-K[i])/S[i]);
        }

        printf("%.8lf\n", D/dtime);
    }
    return 0;
}
