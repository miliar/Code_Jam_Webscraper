#include <iostream>
#include <vector>

using namespace std;

inline bool in_range(const string &N, int i) {
    return i >= 0 && i < N.size();
}
inline int get(const string &N, int i) {
    return N[i] - '0';
}

inline bool is_inc(const vector<int> &num) {
    for (int i = 0; i < num.size(); ++i) {
        if (i + 1 < num.size() && num[i] > num[i+1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string N;
        cin >> N;
        vector<int> m(N.size(), 9);
        vector<int> num;
        for (int i = 0; i < N.size(); ++i) {
            num.push_back(get(N,i));
            const int j = N.size()-i-1;
            int new_m = N[j]-'0';
            if (i > 0) {
                m[j] = m[j+1];
            }
            if (m[j] > new_m) {
                m[j] = new_m;
            }
        }

        while (!is_inc(num)) {
            bool flag = false;
            vector<int> sol;
            for (int i = 0; i < N.size(); ++i) {
                if (flag) {
                    sol.push_back(9);
                } else {
                    if (i+1 < num.size() && num[i] > num[i+1]) {
                        flag = true;
                        if ((i == 0) && (num[i] - 1) == 0) {
                            continue;
                        }
                        sol.push_back(num[i] - 1);
                    } else {
                        sol.push_back(num[i]);
                    }
                }
            }
            num = sol;
        }
        cout << "Case #" << t+1 << ": ";
        for (int i = 0; i < num.size(); ++i) {
            cout << num[i];
        }
        cout << endl;
    }
    return 0;
}
