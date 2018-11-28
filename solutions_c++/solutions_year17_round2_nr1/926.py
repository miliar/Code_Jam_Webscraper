#include <bits/stdc++.h>
using namespace std;

#define MAX 10000
double loc[MAX], speed[MAX];
double timp[MAX];

int main() {

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++){

        double D; int N; cin >> D >> N;
        for (int i = 0; i < N; i++) {
            cin >> loc[i] >> speed[i];

            timp[i] = 1.0 * (D - loc[i]) / (speed[i] * 1.0);
        }

        sort(timp, timp + N);
        double tt = timp[N - 1];

        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(9) << (D / tt) << "\n";
    }

    return 0;
}