#include <bits/stdc++.h>
#define H 1440
#define CT 720
#define INF 100000
using namespace std;
bool can_C[24*60+2];
bool can_J[24*60+2];
int memo1[1441][721][2];
int memo2[1441][721][2];
pair<pair<int, int>, int> pred[1441][721][2];
int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int Ac, Aj;
        cin >> Ac >> Aj;
        memset(can_C, true, sizeof can_C);
        memset(can_J, true, sizeof can_J);
        for(int i = 0; i < Ac; i++) {
            int c, d;
            cin >> c >> d;
            for(int x = c + 1; x <= d; x++) {
                can_C[x] = false;
            }
        }
        for(int i = 0; i < Aj; i++) {
            int j, k;
            cin >> j >> k;
            for(int x = j + 1; x <= k; x++) {
                can_J[x] = false;
            }
        }
        /*
        for(int i = 1; i <= H; i++) {
            cout << "i: " << i << " " << can_C[i] << " " << can_J[i] << endl;
        }
        */
        memo1[0][0][true] = 0;
        memo1[0][0][false] = INF;
        for(int cameron_time = 1; cameron_time <= CT; cameron_time++) {
            memo1[0][cameron_time][true] = INF;
            memo1[0][cameron_time][false] = INF;
        }
        for(int tim = 1; tim <= H; tim++) {
            for(int cameron_time = 0; cameron_time <= CT; cameron_time++) {
                memo1[tim][cameron_time][true] = INF;
                memo1[tim][cameron_time][false] = INF;
                if(cameron_time > 0 && can_C[tim]) {
                    memo1[tim][cameron_time][true] = min(
                        memo1[tim - 1][cameron_time - 1][true],
                        1 + memo1[tim - 1][cameron_time - 1][false]
                    );
                }
                if(tim - 1 >= cameron_time && can_J[tim]) {
                    memo1[tim][cameron_time][false] = min(
                        1 + memo1[tim - 1][cameron_time][true],
                        memo1[tim - 1][cameron_time][false]
                    );
                }
            }
        }

        memo2[0][0][true] = INF;
        memo2[0][0][false] = 0;
        for(int cameron_time = 1; cameron_time <= CT; cameron_time++) {
            memo2[0][cameron_time][true] = INF;
            memo2[0][cameron_time][false] = INF;
        }
        for(int tim = 1; tim <= H; tim++) {
            for(int cameron_time = 0; cameron_time <= CT; cameron_time++) {
                memo2[tim][cameron_time][true] = INF;
                memo2[tim][cameron_time][false] = INF;
                if(cameron_time > 0 && can_C[tim]) {
                    memo2[tim][cameron_time][true] = min(
                        memo2[tim - 1][cameron_time - 1][true],
                        1 + memo2[tim - 1][cameron_time - 1][false]
                    );
                }
                if(tim - 1 >= cameron_time && can_J[tim]) {
                    memo2[tim][cameron_time][false] = min(
                        1 + memo2[tim - 1][cameron_time][true],
                        memo2[tim - 1][cameron_time][false]
                    );
                }
            }
        }
        cout << "Case #" << t << ": " << min(
            min(memo1[H][CT][true], 1 + memo1[H][CT][false]),
            min(1 + memo2[H][CT][true], memo2[H][CT][false])) << endl;
    }
    return 0;
}
