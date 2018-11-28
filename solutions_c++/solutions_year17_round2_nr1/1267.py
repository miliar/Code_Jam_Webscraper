#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <stdio.h>

using namespace std;

#define MAX_S 20000

struct Horse {
    int pos;
    double speed;
    Horse(int _pos, double _s) {
        pos = _pos;
        speed = _s;
    }
};

bool operator < (const Horse& a, const Horse& b) {
    return a.pos < b.pos;
}

int main() {
    int T;
    cin >> T;
    for (int tt=0; tt<T; ++tt) {
        int D, N;
        cin >> D >> N;
        vector <Horse> H;
        H.push_back(Horse(0, MAX_S));
        for (int i=0; i<N; ++i) {
            int p;
            int s;
            cin >> p >> s;
            H.push_back(Horse(p, s));
        }
        sort(H.begin(), H.end());

        for (int i=N-1; i>=1; --i) {
            double t1 = (D - H[i+1].pos) / H[i+1].speed;
            double t2 = (D - H[i].pos) / H[i].speed;
            if (t2 < t1) {
                H[i].speed = (D - H[i].pos) / t1;
            }
        }

        double t = (D - H[1].pos) / H[1].speed;
        double speed = D / t;
        printf("Case #%d: %.6lf\n", tt + 1, speed);
//        cout << "Case #" << tt + 1 << ": " << H[0].speed << endl;
    }
    return 0;
}
