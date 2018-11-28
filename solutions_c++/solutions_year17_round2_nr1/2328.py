#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int D, N;
        cin >> D >> N;
        vector<double> K(N), S(N);
        for (int i = 0; i < N; i++)
            cin >> K[i] >> S[i];
        double maxT = 0;
        for (int i = 0; i < N; i++)
            maxT = max(maxT, (D - K[i]) / S[i]);
        double SS = D / maxT;
        cout << "Case #" << testcase << ": ";
        cout.precision(10);
        cout << SS << endl;
    }
    return 0;
}

// vim: sw=4:
