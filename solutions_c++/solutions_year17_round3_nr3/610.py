#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

double P[1000];

void solve(int tst) {
    int N, K;
    double U;
    cin >> N >> K;
    cin >> U;
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
    }
    
    double cnt = 10000000;
    double add = U / cnt;
    
    for (int i = 0; i < cnt; ++i) {
        sort(P, P + N);
        P[0] += add;
    }

    
    /*while (true) {
        if (fabs(U) <= 1e-12) {
            break;
        }
        
        if (P[0] == P[N - 1]) {
            double avg = U / N;
            for (int i = 0; i < N; ++i) {
                P[i] += avg;
            }
            break;
        } else {
            for (int i = 0; i < N - 1; ++i) {
                double dif = P[i + 1] - P[i];
                double add = min(dif, U);
                U -= add;
                P[i] += add;
            }
        }
    }*/
    
    /*
    while (true) {
        if (fabs(U) <= 1e-12) {
            break;
        }
        double sum = U;
        sort(P, P + N);
        for (int i = 0; i < N; ++i) {
            sum += P[i];
        }
        double avg = sum / N;
        for (int i = 0; i < N; ++i) {
            if (P[i] >= avg) {
                break;
            }
            double add = avg - P[i];
            add = min(U, add);
            P[i] += add;
            U -= add;
        }
    }
    */
    double ans = 1;
    for (int i = 0; i < N; ++i) {
        ans *= P[i];
    }
	printf("Case #%d: %0.12lf\n", tst, ans);
}

int main() {
	freopen("/Users/ryuzmukhametov/gcj/input.txt", "r", stdin);
	//freopen("/Users/ryuzmukhametov/gcj/output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
