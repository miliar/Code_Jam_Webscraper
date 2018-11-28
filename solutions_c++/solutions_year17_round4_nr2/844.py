#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, C, M;
        cin >> N >> C >> M;
        vector<vector<int>> tickets(C);
        vector<vector<int>> seats(C, vector<int>(N, 0));
        for (int i = 0; i < M; i++) {
            int p, c;
            cin >> p >> c;
            c--;
            p--;
            tickets[c].push_back(p);
            seats[c][p]++;
        }
        
        for (auto& ts : tickets) {
            sort(ts.begin(), ts.end());
        }

        // int zeros1 = count_if(tickets[0].begin(), tickets[0].end(), [](int x){ return x == 0; });
        // int other1 = tickets[0].size() - zeros1;
        // int zeros2 = count_if(tickets[1].begin(), tickets[1].end(), [](int x){ return x == 0; });
        // int other2 = tickets[1].size() - zeros2;
        // int result = max(zeros1, other2) + max(zeros2, other1);
        


        int L = 0; // not possible
        for (int i = 0; i < C; i++) {
            L = max(L, (int)(tickets[i].size()) - 1);
        }
        int R = M; // possible
        while (L + 1 < R) {
            int mid = (L + R) / 2;

            vector<int> psum(C, 0);
            vector<int> cnts(N, 0);
            int total = 0;

            bool b = true;
            for (int i = 0; i < N && b; i++) {
                for (int j = 0; j < C && b; j++) {
                    cnts[i] += seats[j][i];
                    // total += seats[j][i];
                    // psum[j] += seats[j][i];
                    // if (psum[j] > mid * (i+1)) {
                    //     b = false;
                    // }
                }
                total += cnts[i];
                if (total > mid * (i+1)) {
                    b = false;
                }
            }

            if (!b || tickets[0].size() > mid || tickets[1].size() > mid)
                L = mid;
            else 
                R = mid;
        }

        int p = 0;

        if (C == 2) {
            for (int seat : tickets[0]) {
                seats[0][seat]--;
                bool b = false;
                
                //look for other  that is identical to  
                for (int i = 0; i < N; i++) {
                    if (seats[1][i] && i != seat && seats[0][i]) {
                        seats[1][i]--;
                        b = true;
                        break;
                    }
                }
                
                if (!b) {
                    for (int i = 0; i < N; i++) {
                        if (seats[1][i] && i != seat) {
                            seats[1][i]--;
                            b = true;
                            break;
                        }
                    }
                }

                if (!b && seats[1][seat] && seat > 0) {
                    seats[1][seat]--;
                    p++;
                }
            }
        }

        cout << "Case #" << t << ": ";

        cout << R << " " << p;

        cout << '\n';
    }
    
}
