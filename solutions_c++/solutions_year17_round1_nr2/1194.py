#include <iostream>
#include <cmath>

using namespace std;

int N, P;
int *R, **Q;

bool matching(bool **map, int u, bool *seen, int *match) {

    for(int i = 0; i < P; ++i) {
        if(map[u][i] && !seen[i]) {
            seen[i] = true;
            if(match[i] < 0 || matching(map, match[i], seen, match)) {
                match[i] = u;
                return true;
            }
        }
    }
    return false;
}

int maxMatching(bool **map) {

    int *match = new int[P];
    for(int i = 0; i < P; ++i)
        match[i] = -1;

    int result = 0;
    for(int i = 0; i < P; ++i) {
        bool *seen = new bool[P];
        for(int j = 0; j < P; ++j)
            seen[j] = false;

        if(matching(map, i, seen, match))
            ++result;
    }
    return result;
}

bool works(int n, int m) {
    double n1 = n / 0.9 / R[0];
    double n2 = n / 1.1 / R[0];
    double m1 = m / 0.9 / R[1];
    double m2 = m / 1.1 / R[1];

    if(ceil(m2) > m1 || ceil(n2) > n1 || ceil(m2) > floor(n1) || ceil(n2) > floor(m1))
        return false;
    return true;
}

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cin >> N >> P;

        R = new int[N];
        Q = new int *[N];

        for (int j = 0; j < N; ++j)
            cin >> R[j];

        for (int j = 0; j < N; ++j) {
            Q[j] = new int[P];
            for (int k = 0; k < P; ++k)
                cin >> Q[j][k];
        }

        cout << "Case #" << i << ": ";
        if (N == 1) {
            int acc = 0;
            for (int j = 0; j < P; ++j) {
                double n1 = Q[0][j] / 0.9 / R[0];
                double n2 = Q[0][j] / 1.1 / R[0];

                if(ceil(n2) <= n1)
                    ++acc;
            }
            cout << acc << endl;
        }

        if (N == 2) {
            bool **map = new bool *[P];
            for (int j = 0; j < P; ++j) {
                map[j] = new bool[P];
                for (int k = 0; k < P; ++k) {
                    map[j][k] = works(Q[0][j], Q[1][k]);
                }
            }
            cout << maxMatching(map) << endl;
            for (int j = 0; j < P; ++j)
                delete[]map[j];
            delete[]map;
        }

        for (int j = 0; j < N; ++j)
            delete[]Q[j];
        delete[]Q;
    }
}