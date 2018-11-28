#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

int N;
long long D[100][100];
long long E[100];
long long S[100];
long double T[100][100];

long long INF = 1000000000000000LL;

string doit() {
    int Q;
    cin >> N >> Q;
    for (int i = 0; i < N; i++) {
        cin >> E[i] >> S[i];
    }
    int d;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> d;
            if (d < -0.5) {
                D[i][j] = INF;
            } else {
                D[i][j] = d;
            }
        }
    }
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (D[i][k] + D[k][j] < D[i][j]) {
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                T[i][j] = 0;
                continue;
            }
            if (D[i][j] >= INF) {
                T[i][j] = INF;
                continue;
            }
            if (D[i][j] > E[i]) {
                T[i][j] = INF;
                continue;
            }
            T[i][j] = (long double)(D[i][j]) / (long double)(S[i]);
        }
    }

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (T[i][k] + T[k][j] < T[i][j]) {
                    T[i][j] = T[i][k] + T[k][j];
                }
            }
        }
    }

    char buf[10000];
    char *ptr = buf;
    int U, V, n;
    for (int q = 0; q < Q; q++) {
        cin >> U >> V;
        U--;
        V--;
        n = sprintf(ptr, " %.8lf", (double)(T[U][V]));
        ptr += n;
        *ptr = 0;
    }
    return string(buf);
}

int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        string res = doit();
        cout << "Case #" << i << ":" << res << endl;
    }
    return 0;
}
