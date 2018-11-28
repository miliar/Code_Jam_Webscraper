#include <algorithm>
#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("A-large.in");
    ofstream cout("output.txt");

    int tests;
    cin >> tests;

    for (int test = 1; test <= tests; ++test ) {
        string line;
        int k, ans = 0;
        cin >> line >> k;
        for (int i = k - 1; i < line.size(); ++i) {
            if (line[i - k + 1] == '-') {
                ans++;
                for (int j = i - k + 1; j <= i; ++j) {
                    if (line[j] == '-') {
                        line[j] = '+';
                    } else {
                        line[j] = '-';
                    }
                }
            }
        }
        for (int i = 0; i < line.size(); ++i) {
            if (line[i] == '-') {
                ans = -1;
            }
        }
        cout << "Case #" << test << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}