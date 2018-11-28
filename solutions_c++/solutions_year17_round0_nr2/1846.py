#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

vector<int> X;

void dfs(int a) {
    if (X[a] > X[a + 1]) {
        --X[a];
        for (int i = a + 1; i < X.size(); ++i) X[i] = 9;
        if (a > 0) dfs(a - 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        string P;
        cin >> P;
        X.clear();
        for (int i = 0; i < P.size(); ++i) X.push_back(P[i] - '0');
        for (int i = 0; i + 1 < X.size(); ++i) dfs(i);

        cout << "Case #" << times << ": ";
        bool flag = true;
        for (int i = 0; i < X.size(); ++i) {
            if (X[i] != 0) flag = false;
            if (X[i] == 0 && flag) continue;
            cout << X[i];
        }
        cout << endl;
    }


    return 0;
}