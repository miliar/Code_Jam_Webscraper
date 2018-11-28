#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>

using namespace std;

void solve()
{
    long long n;
    cin >> n;

    vector <int> res;
    while (n) {
        res.push_back(n % 10);
        n /= 10;
    }
    res.push_back(n);

    reverse(res.begin(), res.end());
    for (int i = 1; i < res.size(); i++) {
        if (res[i] < res[i - 1]) {

            for (int j = i - 1; j > 0; j--) {
                if (res[j] > res[j - 1]) {

                    res[j]--;
                    for (int p = j + 1; p < res.size(); p++) {
                        res[p] = 9;
                    }
                    break;
                }

            }
            break;
        }
    }

    for (int i = 0; i < res.size(); i++) {
        if (res[i] == 0) continue;
        for (int j = i; j < res.size(); j++) {
            cout << res[j];
        }
        cout << "\n";
        break;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int cntTests;
    cin >> cntTests;
    for (int numTest = 1; numTest <= cntTests; numTest++) {
        cout << "Case #" << numTest << ": ";
        solve();
    }
}
