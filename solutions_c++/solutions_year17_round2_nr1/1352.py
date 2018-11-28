#include <iostream>
#include <cstdio>
using namespace std;

int D, N;
int K[1001];
int S[1001];

void solve()
{
    double maxv = 0;
    for (int i = 0; i < N; i++) {
        maxv = max(maxv, (D - K[i]) / (double)S[i]);
    }
    printf("%.7f", D / maxv);
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> D >> N;
        for (int j = 0; j < N; j++) {
            cin >> K[j] >> S[j];
        }
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
