#include <algorithm>
#include <iostream>
using namespace std;

const int N_MAX = 50;
int T, N, K;
double u, p[N_MAX];
int U, P[N_MAX];

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        double u;
        cin >> N >> K >> u;
        U = (int)(u*10000 + 0.1);
        for (int i = 0; i < N; i++) {
            cin >> p[i];
            P[i] = (int)(p[i]*10000 + 0.1);
        }

        sort(P, P+N);

        while (0 < U) {
            int i = 0;
            while (i < N-1 && P[i] == P[i+1]) i++;
            bool e = true;
            if (i < N-1 && (i+1)*(P[i+1]-P[i]) < U) e = false;
            if (!e) {
                for (int j = 0; j <= i; j++) {
                    U -= P[i+1]-P[i];
                    P[j] += P[i+1]-P[i];
                }
                if (U == 0) e = true;
                /*
                cout << U << "* ";
                for (int i = 0; i < N; i++) cout << P[i] << " ";
                cout << endl;
                */
            }
            if (e) {
                for (int j = 0; j < N; j++)
                    p[j] = (P[j] + 0.0)/10000;
                u = (U + 0.0)/10000;
                for (int j = 0; j <= i; j++)
                    p[j] += u/(i+1);
                U = 0;
            }
        }
        double ans = 1;
        for (int j = 0; j < N; j++)
            ans *= p[j];
        printf("Case #%d: %.9f\n", t, ans);
    }
    return 0;
}
