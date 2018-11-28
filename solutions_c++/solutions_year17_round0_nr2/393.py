#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

typedef long long ll;

int main()
{
    int T;
    cin >> T;
    cout.precision(8);
    for (int casenum = 1; casenum <= T; ++casenum) {
        string num;
        cin >> num;
        vector<int> ds;
        for (char c : num) {
            ds.push_back(c - '0');
        }
        bool ok = false;
        const int N = ds.size();
        while (!ok) {
            ok = true;
            for (int i = 1; i < N; ++i) {
                if (ds[i] < ds[i-1]) {
                    --ds[i-1];
                    for (int j = i; j < N; ++j) {
                        ds[j] = 9;
                    }
                    ok = false;
                    break;
                }
            }
        }

        cout << "Case #" << casenum << ": ";
        bool started = false;
        for (int d : ds) {
            if (!started && d == 0) continue;
            started = true;
            cout << d;
        }
        cout << endl;
    }
    return 0;
}

