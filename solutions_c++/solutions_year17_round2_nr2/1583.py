#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <tuple>

using namespace std;

map <tuple<int, int, int, int, int>, string> DP;

string calc(int i, int j, int k, int color1, int color2) {
    // Reindex so i >= j >= k
    //cout << i << " " << j << " " << k << " " << endl;

    if (i + j + 1 < k || i + k + 1 < j || j + k + 1 < i) return "IMPOSSIBLE";

    tuple<int, int, int, int, int> to_index = make_tuple(i,j,k,color1, color2);

    if (DP.find(to_index) != DP.end()) { return DP[to_index]; }

    if (i == 0 && j == 0 && k == 0) {
        if (color1 == color2) DP[to_index] = "IMPOSSIBLE";
        else DP[to_index] = "";
        return DP[to_index];
    }

    else if (i > 0 && color1 != 0 && calc(i-1, j, k, 0, color2) != "IMPOSSIBLE") {
        DP[to_index] = "R" + calc(i-1, j, k, 0, color2);
        return DP[to_index];
    }

    else if (j > 0 && color1 != 1 && calc(i, j-1, k, 1, color2) != "IMPOSSIBLE") {
        DP[to_index] = "Y" + calc(i, j-1, k, 1, color2);
        return DP[to_index];
    }

    else if (k > 0 && color1 != 2 && calc(i, j, k-1, 2, color2) != "IMPOSSIBLE") {
        DP[to_index] = "B" + calc(i, j, k-1, 2, color2);
        return DP[to_index];
    }

    else {
        DP[to_index] = "IMPOSSIBLE";
    }

    return DP[to_index];
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        int N,R,O,Y,G,B,V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        if (R == 0 && Y == 0 && B == 0) {
            if (O == 0 && G == 0 && V == 0) {
                cout << "Case #" << i << ": " << "\n";
                continue;
            }

            else {
                cout << "Case #" << i << ": " << "IMPOSSIBLE\n";
                continue;
            }
        }

        if (R > 0 && calc(R-1,Y,B,0,0) != "IMPOSSIBLE") {
            cout << "Case #" << i << ": " << "R" + calc(R-1,Y,B,0,0) + "\n";
            continue;
        }

        if (Y > 0 && calc(R,Y-1,B,1,1) != "IMPOSSIBLE") {
            cout << "Case #" << i << ": " << "Y" + calc(R,Y-1,B,1,1) + "\n";
            continue;
        }

        if (B > 0 && calc(R,Y,B-1,2,2) != "IMPOSSIBLE") {
            cout << "Case #" << i << ": " << "B" + calc(R,Y,B-1,2,2) + "\n";
            continue;
        }

        cout << "Case #" << i << ": " << "IMPOSSIBLE\n";
    }
}