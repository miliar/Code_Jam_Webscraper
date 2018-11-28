//
// Created by quuynh on 15/04/17.
//

#include <climits>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;


bool checkRight(int lx, int ly, int rx, int ry, string input[], char ch) {
    for (int i = lx; i <= rx; i++) if (input[i][ry + 1] != '?') return false;
    return true;
}

bool checkLeft(int lx, int ly, int rx, int ry, string input[], char ch) {
    for (int i = lx; i <= rx; i++) if (input[i][ly - 1] != '?') return false;
    return true;
}

bool checkUp(int lx, int ly, int rx, int ry, string input[], char ch) {
    for (int i = ly; i <= ry; i++) if (input[lx - 1][i] != '?') return false;
    return true;
}

bool checkDown(int lx, int ly, int rx, int ry, string input[], char ch) {
    for (int i = ly; i <= ry; i++) if (input[rx + 1][i] != '?') return false;
    return true;
}


int main() {
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/codejam15042017/A-small-attempt2.in", "r", stdin);
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/codejam15042017/output2.out", "w", stdout);
    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        int m, n;
        cin >> m >> n;
        string input[m];
        for (int i = 0; i < m; i++) cin >> input[i];
        string output[m];
        unordered_map<char, pair<int, int>> left, right;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char x = input[i][j];
                if (x != '?') {
                    if (left.find(x) == left.end()) {
                        left.insert({x, {i, j}});
                    }
                    if (right.find(x) == right.end()) {
                        right.insert({x, {i, j}});
                    }
                    left[x].first = min(left[x].first, i);
                    left[x].second = min(left[x].second, j);
                    right[x].first = max(right[x].first, i);
                    right[x].second = max(right[x].second, j);
                }
            }
        }
        for (char ch = 'A'; ch <= 'Z'; ch++)
            if (left.find(ch) != left.end()) {
                for (int i = left[ch].first; i <= right[ch].first; i++)
                    for (int j = left[ch].second; j <= right[ch].second; j++) input[i][j] = ch;
            }
        for (int i = 0; i < m; i++) output[i] = input[i];

        for (char ch = 'A'; ch <= 'Z'; ch++)
            if (left.find(ch) != left.end()) {
                int lx = left[ch].first;
                int ly = left[ch].second;
                int rx = right[ch].first;
                int ry = right[ch].second;
                while (ly > 0 && checkLeft(lx, ly, rx, ry, input, ch)) ly--;
                while (ry < n - 1 && checkRight(lx, ly, rx, ry, input, ch)) ry++;
                while (lx > 0 && checkUp(lx, ly, rx, ry, input, ch)) lx--;
                while (rx < m - 1 && checkDown(lx, ly, rx, ry, input, ch)) rx++;
                for (int i = lx; i <= rx; i++)
                    for (int j = ly; j <= ry; j++) input[i][j] = ch;
            }
        bool ok = true;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) if (input[i][j] == '?') ok = false;
        if (ok == false) {
            for (int i = 0; i < m; i++) input[i] = output[i];
            for (char ch = 'A'; ch <= 'Z'; ch++)
                if (left.find(ch) != left.end()) {
                    int lx = left[ch].first;
                    int ly = left[ch].second;
                    int rx = right[ch].first;
                    int ry = right[ch].second;
                    while (lx > 0 && checkUp(lx, ly, rx, ry, input, ch)) lx--;
                    while (rx < m - 1 && checkDown(lx, ly, rx, ry, input, ch)) rx++;
                    while (ly > 0 && checkLeft(lx, ly, rx, ry, input, ch)) ly--;
                    while (ry < n - 1 && checkRight(lx, ly, rx, ry, input, ch)) ry++;
                    for (int i = lx; i <= rx; i++)
                        for (int j = ly; j <= ry; j++) input[i][j] = ch;
                }
        }
        cout << "Case #" << test << ": " << endl;
        for (int i = 0; i < m; i++) {
            cout << input[i];
            if (i < m - 1 || test < ntest) cout << endl;
        }
    }
    return 0;
}