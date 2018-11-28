#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        string s;
        int K = 0;
        cin >> s >> K;
        int res = 0;
        size_t pos = s.find('-'); 
        while (pos != string::npos) {
            if (pos > s.size() - K) {
                res = -1;
                break;
            }
            for (int i = 0; i < K; ++i)
                s[pos+i] = (s[pos+i] == '+' ? '-' : '+');
            res++;
            pos = s.find('-');
        }
        if (res == -1)
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << endl;
    }
}

