#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>
#include <cmath>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";
        int N, K; cin >> N >> K;
        vector< pair<int,int>> pancake(N);

        for(int i = 0; i < N; i++) {
            cin >> pancake[i].first >> pancake[i].second;
        }

        sort(pancake.begin(), pancake.end());
        reverse(pancake.begin(), pancake.end());
       
        double end = 0, temp;
        for(int i = 0; i < N; i++) {
            temp = M_PI*pancake[i].first*pancake[i].first +
                2*M_PI*pancake[i].first*pancake[i].second;
            vector<double> res(N - i - 1);
            for(int j = i + 1; j < N; j++) {
                res[j - i - 1] = 2*M_PI*pancake[j].first*pancake[j].second;
            }

            sort(res.begin(),res.end());
            reverse(res.begin(),res.end());

            for(int k = 0; k < min(K - 1, (int)res.size()); k++) {
                temp += res[k];
            }
            end = max(temp, end);
            // taking i as base.
        }
        
        printf("%.8lf\n",end);

    }
    return 0;
}
