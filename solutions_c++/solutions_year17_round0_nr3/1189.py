#include <fstream>
using namespace std;

inline long long maxlr(long long x) {
    return (x >> 1);
}

inline long long minlr(long long x) {
    if (x & 1)
        return x >> 1;
    return ((x >> 1) - 1);
}

int main () {
    ifstream cin("C.in");
    ofstream cout("C.out");

    int T;
    cin >> T;

    for (int tst = 1 ; tst <= T ; ++tst) {
        long long n, k;
        cin >> n >> k;

        long long mare = n, mic = -1, sol;
        long long cntmare = 1, cntmic = 0;

        while (k) {
            if (cntmare >= k) {
                sol = mare;
                k = 0;
            }
            else {
                k -= cntmare;
                if (mic != -1 && cntmic >= k) {
                    sol = mic;
                    k = 0;
                }
                else {
                    k -= cntmic;
                    long long mare2 = -1, mic2 = -1;
                    long long cntmare2 = 0, cntmic2 = 0;

                    if ((mare & 1) == 0) {
                        mare2 = mare >> 1;
                        mic2 = ((mare >> 1) - 1);

                        cntmare2 = cntmic2 = cntmare;

                        if (mic != -1) {
                            cntmic2 += (2 * cntmic);;
                        }
                    }
                    else {
                        mare2 = ((mare - 1) >> 1);
                        cntmare2 = (2 * cntmare);

                        if (mic != -1) {
                            cntmare2 += cntmic;
                            mic2 = ((mare - 1) >> 1) - 1;
                            cntmic2 = cntmic;
                        }
                    }

                    mare = mare2, mic = mic2;
                    cntmare = cntmare2, cntmic = cntmic2;
                }
            }
        }

        cout << "Case #" << tst << ": " << maxlr(sol) << " " << minlr(sol) << "\n";
    }

    return 0;
}
