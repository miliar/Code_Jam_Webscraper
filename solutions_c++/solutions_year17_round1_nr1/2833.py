#include <iostream>
#include <vector>
#include <cstdio>
#include <unordered_set>

using namespace std;

int qpow(int n, int k, int m) {
    if (k == 0) {
        return 1;
    }
    vector<int> nums;
    nums.reserve(32);
    nums.push_back(n % m);
    for (int i = 1; i < 32; ++i) {
        if ((1 << i) < k) {
            nums.push_back((1LL * nums.back() * nums.back()) % m);
        } else {
            break;
        }
    }
    long long ret = 1;
    for (int i = 0; i < 32; ++i) {
        if (k & (1 << i)) {
            ret *= nums[i];
            ret %= m;
        }
    }
    return ret;
}

int fnn(int n, int k, int m) {
    long long ret = 1;
    for (int i = 0; i < k; ++i) {
        ret *= n - i;
        ret %= m;
    }
    return ret;
}

int mdiv(int a, int b, int m) {
    int rb = qpow(b, m - 2, m);
    long long ret = a;
    ret *= rb;
    ret %= m;
    return ret;
}

int cnk(int n, int k, int m) {
    int a = fnn(n, k, m);
    int b = fnn(k, k, m);
    cout << a << ' ' << b << endl;
    return mdiv(a, b, m);
}


char *intToHex(int num) {
    char *p = new char[20];
    sprintf(p, "%x", num);
    return p;
}

bool can_up(const vector<vector<char>> &matrix, int i, int j) {
    if (i == 0) {
        return false;
    }
    int k = i - 1;
    while (k >= 0 && matrix[k][j] == matrix[i][j]) {
        --k;
    }
    if (k < 0) {
        return false;
    }
    for (int l = 0; l < matrix[0].size(); ++l) {
        if (matrix[k + 1][l] == matrix[i][j]) {
            if (matrix[k][l] != '?') {
                return false;
            }
        }
    }
    return true;
}

bool can_down(const vector<vector<char>> &matrix, int i, int j) {
    if (i == matrix.size() - 1) {
        return false;
    }
    int k = i + 1;
    while (k < matrix.size() && matrix[k][j] == matrix[i][j]) {
        ++k;
    }
    if (k == matrix.size()) {
        return false;
    }
    for (int l = 0; l < matrix[0].size(); ++l) {
        if (matrix[k - 1][l] == matrix[i][j]) {
            if (matrix[k][l] != '?') {
                return false;
            }
        }
    }
    return true;
}

bool can_left(const vector<vector<char>> &matrix, int i, int j) {
    if (j == 0) {
        return false;
    }
    int k = j - 1;
    while (k >= 0 && matrix[i][k] == matrix[i][j]) {
        --k;
    }
    if (k < 0) {
        return false;
    }
    for (int l = 0; l < matrix.size(); ++l) {
        if (matrix[l][k + 1] == matrix[i][j]) {
            if (matrix[l][k] != '?') {
                return false;
            }
        }
    }
    return true;
}

bool can_right(const vector<vector<char>> &matrix, int i, int j) {
    if (j == matrix[0].size() - 1) {
        return false;
    }
    int k = j + 1;
    while (k < matrix[0].size() && matrix[i][k] == matrix[i][j]) {
        ++k;
    }
    if (k == matrix[0].size()) {
        return false;
    }
    for (int l = 0; l < matrix.size(); ++l) {
        if (matrix[l][k - 1] == matrix[i][j]) {
            if (matrix[l][k] != '?') {
                return false;
            }
        }
    }
    return true;
}

bool ok = false;
vector<vector<char>> mt;

void solve(vector<vector<char>> &matrix, int cnt) {
    if (ok) {
        return;
    }
//    for (auto &line:matrix) {
//        for (auto &ch:line) {
//            cout << ch;
//        }
//        cout << endl;
//    }
    if (cnt == 0) {
        ok = true;
        mt = matrix;
        return;
    }
    unordered_set<char> st;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[0].size(); ++j) {
            if (matrix[i][j] == '?') {
                continue;
            }
            if (st.find(matrix[i][j]) != st.end()) {
                continue;
            }
            st.insert(matrix[i][j]);

            if (can_up(matrix, i, j)) {
//                cout << "up" << endl;
                int new_cnt = cnt;
                auto new_matrix(matrix);
                int k = i - 1;
                while (k >= 0) {
                    if (matrix[k][j] == matrix[i][j]) {
                        --k;
                    } else {
                        break;
                    }
                }
                for (int l = 0; l < new_matrix[0].size(); ++l) {
                    if (new_matrix[k + 1][l] == new_matrix[i][j]) {
                        new_matrix[k][l] = new_matrix[i][j];
                        --new_cnt;
                    }
                }
                solve(new_matrix, new_cnt);
            }
            if (can_down(matrix, i, j)) {
//                cout << "down" << endl;
                int new_cnt = cnt;
                auto new_matrix(matrix);
                int k = i + 1;
                while (k < matrix.size()) {
                    if (matrix[k][j] == matrix[i][j]) {
                        ++k;
                    } else {
                        break;
                    }
                }
                for (int l = 0; l < new_matrix[0].size(); ++l) {
                    if (new_matrix[k - 1][l] == new_matrix[i][j]) {
                        new_matrix[k][l] = new_matrix[i][j];
                        --new_cnt;
                    }
                }
                solve(new_matrix, new_cnt);
            }
            if (can_left(matrix, i, j)) {
//                cout << "left" << endl;
                int new_cnt = cnt;
                auto new_matrix(matrix);
                int k = j - 1;
                while (k >= 0) {
                    if (matrix[i][k] == matrix[i][j]) {
                        --k;
                    } else {
                        break;
                    }
                }
                for (int l = 0; l < new_matrix.size(); ++l) {
                    if (new_matrix[l][k + 1] == new_matrix[i][j]) {
                        new_matrix[l][k] = new_matrix[i][j];
                        --new_cnt;
                    }
                }
                solve(new_matrix, new_cnt);
            }
            if (can_right(matrix, i, j)) {
//                cout << "right" << endl;
                int new_cnt = cnt;
                auto new_matrix(matrix);
                int k = j + 1;
                while (k < matrix[0].size()) {
                    if (matrix[i][k] == matrix[i][j]) {
                        ++k;
                    } else {
                        break;
                    }
                }
                for (int l = 0; l < new_matrix.size(); ++l) {
                    if (new_matrix[l][k - 1] == new_matrix[i][j]) {
                        new_matrix[l][k] = new_matrix[i][j];
                        --new_cnt;
                    }
                }
                solve(new_matrix, new_cnt);
            }
        }
    }
    return;
}

int main() {

    int T, R, C;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cin >> R >> C;
        ok = false;
        vector<vector<char>> matrix(R, vector<char>(C, '?'));
        int cnt = 0;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cin >> matrix[i][j];
                if (matrix[i][j] == '?') {
                    ++cnt;
                }
            }
        }
//        cout << cnt << endl;
//        for (auto &line:matrix) {
//            for (auto &ch:line) {
//                cout << ch;
//            }
//            cout << endl;
//        }

        solve(matrix, cnt);
        cout << "Case #" << t << ":" << endl;
        //TODO
        for (auto &line:mt) {
            for (auto &ch:line) {
                cout << ch;
            }
            cout << endl;
        }
    }

    return 0;
}