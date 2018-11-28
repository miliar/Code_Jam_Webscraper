#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int testcase;
    cin >> testcase;
    for (int tc = 1; tc <= testcase; ++tc) {
        int N, D;
        cin >> D >> N;
        double t = -1;
        for (int i = 0; i < N; ++i) {
            int K, S;
            cin >> K >> S;
            t = max(t, (double)(D - K) / (double)S);
        }
        t = D / t;
        cout << "Case #" << tc << ": ";
        cout << setprecision(7) << fixed << t << endl;
    }
    return 0;
}