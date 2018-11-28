#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;


void fill(vector<string>& input, char c, vector<tuple<int, int>>& p) {
    int min_r = 30;
    int min_c = 30;
    int max_r = -1;
    int max_c = -1;

    for (auto x: p) {
        min_r = min(min_r, get<0>(x));
        max_r = max(max_r, get<0>(x));
        min_c = min(min_c, get<1>(x));
        max_c = max(max_c, get<1>(x));
    }

    for (int i = min_r; i <= max_r; ++i) {
        for (int j = min_c; j <= max_c; ++j) {
            input[i][j] = c;
        }
    }
}

void fill_blank(vector<string>& input) {
    int R = input.size();
    int C = input[0].size();

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (input[i][j] == '?')
                continue;

            for (int k = j-1; k >= 0 && input[i][k] == '?'; k--)
                input[i][k] = input[i][j];

            for (int k = j+1; k < C && input[i][k] == '?'; k++)
                input[i][k] = input[i][j];
        }
    }

    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (input[i][j] == '?')
                continue;

            for (int k = i-1; k >= 0 && input[k][j] == '?'; k--)
                input[k][j] = input[i][j];

            for (int k = i+1; k < R && input[k][j] == '?'; k++)
                input[k][j] = input[i][j];
        }
    }
}

void solve(vector<string>& input) {
    int R = input.size();
    int C = input[0].size();

    map<char, vector<tuple<int, int>>> place;

    for (int i = 0; i < R; ++i) {
        for (int j= 0; j < C; ++j) {
            if (input[i][j] != '?')
                place[input[i][j]].push_back(make_tuple(i, j));
        }
    }

    for (auto kv : place) {
        fill(input, kv.first, kv.second);
    }

    fill_blank(input);
}

int main() {
    int T;
    cin >> T;

    for (int kase = 1; kase <= T; ++kase) {
        int R, C;
        cin >> R >> C;

        vector<string> input(R);

        for (int i = 0; i < R; ++i)
            cin >> input[i];

        solve(input);

        printf("Case #%d:\n", kase);
        for (auto s: input)
            cout << s << endl;
    }

    return 0;
}
