#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

bool occupied[1000005];
long long N, K;

int closest(int idx, bool lr) {
    int br = 0;
    if(lr) { // r
        idx++;
        while(!occupied[idx]) //&& idx < N + 2)
            idx++, br++;
    } else {
        idx --;
        while(!occupied[idx])// && idx >= 0)
            idx--, br++;
    }

    return br;
}

int main() {

    int T;
    cin >> T;

    for(int t = 1; t <= T; t++) {
        cin >> N >> K;

        int solution;
        memset(occupied, 0, sizeof(bool) * (N + 2));
        occupied[0] = 1;
        occupied[N + 1] = 1;

        for(int k = 0; k < K; k++) {
            int ideal = -1;

            for(int s = 1; s < N + 1; s++) {
                if(!occupied[s])
                    ideal = max(ideal, min(closest(s, 0), closest(s, 1)));
            }

            vector<int> Stall;
            for(int s = 1; s < N + 1; s++) {
                if(!occupied[s])
                    if(ideal == min(closest(s, 0), closest(s, 1)))
                        Stall.push_back(s);
            }

            solution = -1;
            if(Stall.size() > 1) {
                for(int i = 0; i < Stall.size(); i++)
                    ideal = max(ideal, max(closest(Stall[i], 0), closest(Stall[i], 1)));

                vector<int> S;
                for(int i = 0; i < Stall.size(); i++)
                    if(ideal == max(closest(Stall[i], 0), closest(Stall[i], 1)))
                        S.push_back(Stall[i]);

                sort(S.begin(), S.end());
                solution = S[0];
            } else
                solution = Stall[0];

            occupied[solution] = 1;
        }

        cout << "Case #" << t << ": " << max(closest(solution, 0), closest(solution, 1)) << " " << min(closest(solution, 0), closest(solution, 1)) << endl;
    }

    return 0;
}