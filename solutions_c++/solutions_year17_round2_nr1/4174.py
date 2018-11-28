#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

struct Horse {
    int speed;
    int pos;
    double meetTime;
    int meetHorse;

    bool operator< (const Horse& r) const {
        return pos < r.pos;
    }
};

double getMeetTime(int pos1, int speed1, int pos2, int speed2) {
    double x = (pos2 - pos1) * speed2 / ((double)(speed1 - speed2));
    return x / speed2;
}

double solve(int D, vector<Horse>& horses) {
    const int N = horses.size();
    sort(horses.begin(), horses.end());
    horses[N - 1].meetTime = (D - horses[N - 1].pos) / (double)horses[N - 1].speed;
    int slovest = N - 1;
    for (int i = N - 2; i >= 0; --i) {
        double pos = horses[i].pos;
        double finishTime = (D - horses[i].pos) / (double)horses[i].speed;
        bool canBeSlovest = true;
        for (int x = i + 1; x < N && canBeSlovest; ++x) {
            double meetTime = getMeetTime(horses[i].pos, horses[i].speed, horses[x].pos, horses[x].speed);
            if (meetTime > 0.0 && meetTime <= finishTime) {
                canBeSlovest = false;
            }
        }
        if (canBeSlovest && finishTime >= horses[slovest].meetTime) {
            slovest = i;
            horses[slovest].meetTime = finishTime;
        }
    }

    return D / horses[slovest].meetTime;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int D, N;
        cin >> D >> N;
        vector<Horse> horses(N);
        for (int i = 0; i < N; ++i) {
            cin >> horses[i].pos >> horses[i].speed;
            horses[i].meetHorse = -1;
            horses[i].meetTime = 0.0;
        }

        cout.precision(17);
        cout << "Case #" << t << ": " << solve(D, horses) << endl;
    }
    return 0;
}
