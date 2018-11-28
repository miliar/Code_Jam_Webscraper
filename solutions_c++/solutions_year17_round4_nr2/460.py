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

        int N, C, M; cin >> N >> C >> M;
        vector<vector<int>> tickets(C, vector<int>());
        vector<int> business(N, 0);

        for(int i = 0; i < M; i++) {
            int person, seat;
            cin >> seat >> person;
            seat--;
            person--;
            tickets[person].push_back(seat);
            business[seat]++;
        }
        int minrides = 0;
        for(int i = 0; i < C; i++) {
            minrides = max(minrides, (int)tickets[i].size());
        }
        int acc = 0;
        for(int i = 0; i < N; i++) {
            acc += business[i];
            // heb tenminste acc/(i+1) naar boven afgerond rides nodig. dus
            minrides = max(minrides, (acc + i)/(i+1));
        }
        int switches = 0;
        for(int i = 0; i < N; i++) {
            if(business[i] > minrides) {
                switches += business[i] - minrides;
            }
        }
        cout << minrides << " " << switches << endl;
    }
    return 0;
}
