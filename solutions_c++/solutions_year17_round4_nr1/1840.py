#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, P;
        cin >> N >> P;
        vector<int> rem(P + 1, 0);
        for (int n = 0; n < N; n++) {
            int G;
            cin >> G;
            G %= P;
            rem[G]++;
        }
        int sol = rem[0];
        rem[0] = 0;
        for (int i = 1; i < P; i++) {
            int j = P - i;
            int auxSol = min(rem[i], rem[j]);
            if (i == j) {
                auxSol = rem[i] / 2;
            }
            sol += auxSol;
            rem[i] -= auxSol;
            rem[P - 1] -= auxSol;
        }
        for (int i = 1; i < P; i++) {
            for (int j = 1; j < P; j++) {
                int k = P - (i + j) % P;
                int auxSol = min(rem[i], min(rem[j], rem[k]));
                if (i == j && j == k) {
                    auxSol = rem[i] / 3;
                } else if (i == j) {
                    auxSol = min(rem[i] / 2, rem[k]);
                } else if (j == k) {
                    auxSol = min(rem[i], rem[j] / 2);
                } else if (i == k) {
                    auxSol = min(rem[i] / 2, rem[j]);
                }
                sol += auxSol;
                rem[i] -= auxSol;
                rem[j] -= auxSol;
                rem[k] -= auxSol;
            }
        }
        //for (int i = 1; i < P; i++) {
        //    for (int j = 1; j < P - i; j++) {
        //        for (int k = 1; k < P - i - j; k++) {
        //            int l = P - i - j - k;
        //            sol += min(rem[i], min(rem[j], min(rem[k], rem[l])));
        //            rem[i] -= min(rem[i], min(rem[j], min(rem[k], rem[l])));
        //            rem[j] -= min(rem[i], min(rem[j], min(rem[k], rem[l])));
        //            rem[k] -= min(rem[i], min(rem[j], min(rem[k], rem[l])));
        //            rem[l] -= min(rem[i], min(rem[j], min(rem[k], rem[l])));
        //        }
        //    }
        //}
        for (int i = 1; i < P; i++) {
            if (rem[i] != 0) {
                sol++;
                break;
            }
        }
        cout << "Case #" << t << ": " << sol << endl;
    }
	return 0;
}
