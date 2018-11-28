#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

void solve(int R, int Y, int B, int G, int V, int O) {
    int N = R + Y + B;
    if (R > Y + B || Y > B + R || B > R + Y) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    char pos[10000];

    memset(pos, 0, sizeof(pos));
    if (R >= Y && R >= B) {
        int p = 0;
        while (R > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'R';
            R--;
            p = (p + 2) % N;
        }
        while (Y > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'Y';
            Y--;
            p = (p + 2) % N;
        }
        while (B > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'B';
            B--;
            p = (p + 2) % N;
        }
    } else if (Y >= B && Y >= R) {
        int p = 0;
        while (Y > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'Y';
            Y--;
            p = (p + 2) % N;
        }
        while (R > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'R';
            R--;
            p = (p + 2) % N;
        }
        while (B > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'B';
            B--;
            p = (p + 2) % N;
        }
    } else if (B >= R && B >= Y) {
        int p = 0;
        while (B > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'B';
            B--;
            p = (p + 2) % N;
        }
        while (R > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'R';
            R--;
            p = (p + 2) % N;
        }
        while (Y > 0) {
            while (pos[p]) {
                p++;
                p %= N;
            }
            pos[p] = 'Y';
            Y--;
            p = (p + 2) % N;
        }
    }

    int fg = 0, fv = 0, fo = 0;
    for (int i = 0; i < N; i++) {
        if (pos[i] == 'R' && fg == 0) {
            for (int j = 0; j < G; j++) cout << "RG";
            fg = 1;
        }
        if (pos[i] == 'Y' && fv == 0) {
            for (int j = 0; j < V; j++) cout << "YV";
            fv = 1;
        }
        if (pos[i] == 'B' && fo == 0) {
            for (int j = 0; j < O; j++) cout << "BO";
            fo = 1;
        }
        cout << pos[i];
    }
    cout << endl;
}

int main () {
    int nc;

    cin >> nc;
    for (int tc = 1; tc <= nc; tc++) {
        cout << "Case #" << tc << ": ";

        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        if (O > B || G > R || V > Y) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        if (O > 0 && O == B) {
            if (R > 0 || Y > 0 || G > 0 || V > 0) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            for (int i = 0; i < O; i++) {
                cout << "OB";
            }
            cout << endl;
            continue;
        } else if (G > 0 && G == R) {
            if (O > 0 || Y > 0 || B > 0 || V > 0) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            for (int i = 0; i < G; i++) {
                cout << "GR";
            }
            cout << endl;
            continue;
        } else if (V > 0 && V == Y) {
            if (R > 0 || O > 0 || G > 0 || B > 0) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            for (int i = 0; i < V; i++) {
                cout << "VY";
            }
            cout << endl;
            continue;
        } else {
            solve(R - G, Y - V, B - O, G, V, O);
        }
    }
    return 0;
}