
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <string>
using namespace std;

int T, K, S, i, s, N;
string line;

int main () {
    cin >> T;

    for(int tcase=1;tcase <= T; tcase++) {
        cin >> line >> K;

        N = 0;
        for(i = 0; i <= line.size() - K; i++) {
            if(line[i] == '-') {
                for(s=i; s<i+K; s++) {
                    line[s] = (line[s] == '-') ? '+' : '-';
                }
                N++;
            }
        }

        bool chk = false;
        for(i = 0; i < line.size() && !chk; i++)
            if(line[i] == '-') chk = true;

        if(chk) {
            cout << "Case #" << tcase << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << tcase << ": " << N << endl;
        }
    }

    return 0;
}
