#include <bits/stdc++.h>

using namespace std;

bool is_full(vector<string> &cake) {
    for (int i = 0; i < cake.size(); ++i) {
        for (int j = 0; j < cake[i].size(); ++j) {
            if (cake[i][j] == '?')
                return false;
        }
    }

    return true;
}

void print_cake(vector<string> &cake) {
    for (int i = 0; i < cake.size(); ++i) {
        printf("%s\n", cake[i].c_str());
    }
}

void distribute(vector<string> &cake) {
    if (!is_full(cake)) {
        for (int i = 0; i < cake.size(); ++i) {
            vector<char> alpha_list;

            for (int j = 0; j < cake[i].size(); ++j) {
                if (cake[i][j] != '?')
                    alpha_list.push_back(cake[i][j]);
            }

            if (alpha_list.size() > 0) {
                for (int j = 0; j < cake[i].size(); ++j) {
                    if (cake[i][j] == alpha_list[0]) {
                        if (alpha_list.size() > 1)
                            alpha_list.erase(alpha_list.begin());
                    }

                    if (cake[i][j] == '?')
                        cake[i][j] = alpha_list[0];
                }
            }
        }

        vector<int> row_list;

        for (int i = 0; i < cake.size(); ++i) {
            if (cake[i][0] != '?')
                row_list.push_back(i);
        }

        if (row_list.size() > 0) {
            for (int i = 0; i < cake.size(); ++i) {
                if (i == row_list[0]) {
                    if (row_list.size() > 1)
                        row_list.erase(row_list.begin());
                } else {
                    for (int j = 0; j < cake[i].size(); ++j)
                        cake[i][j] = cake[row_list[0]][j];
                }
            }
        }
    }
}



int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        // scan input
        int r, c;
        cin >> r;
        cin >> c;
        vector<string> cake;
        string slice;

        for (int j = 0; j < r; j++) {
            cin >> slice;
            cake.push_back(slice);
        }

        // process input
        distribute(cake);
        // print answer
        cout << "Case #" << i  << ":" << endl;
        print_cake(cake);
    }

    return 0;
}

