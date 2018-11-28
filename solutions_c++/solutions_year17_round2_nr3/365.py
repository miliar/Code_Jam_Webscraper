#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <future>
#include <chrono>
#include <experimental/filesystem>

using namespace std;

experimental::filesystem::path getNewest() {
    using namespace experimental::filesystem;
    path dir("C:\\Users\\alexe\\Downloads");
    path ans("");
    for (directory_iterator it(dir); it != directory_iterator(); ++it) {
        if (ans.empty() || last_write_time(ans) < last_write_time(*it)) {
            ans = *it;
        }
    }
    return ans;
}

struct Input {
    int n, q;
    vector<int> e, s;
    vector<vector<int>> d;
    vector<int> u, v;

    friend istream& operator >>(istream& lhs, Input& rhs) {
        lhs >> rhs.n >> rhs.q;
        rhs.e.resize(rhs.n);
        rhs.s.resize(rhs.n);
        for (int i = 0; i < rhs.n; ++i) {
            lhs >> rhs.e[i] >> rhs.s[i];
        }
        rhs.d.resize(rhs.n);
        for (int i = 0; i < rhs.n; ++i) {
            rhs.d[i].resize(rhs.n);
            for (int j = 0; j < rhs.n; ++j) {
                lhs >> rhs.d[i][j];
            }
        }
        rhs.u.resize(rhs.q);
        rhs.v.resize(rhs.q);
        for (int i = 0; i < rhs.q; ++i) {
            lhs >> rhs.u[i] >> rhs.v[i];
            --rhs.u[i];
            --rhs.v[i];
        }
        return lhs;
    }
};

struct Output {
    int id;
    vector<long double> ans;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << fixed << setprecision(10);
        lhs << "Case #" << (rhs.id + 1) << ":";
        for (long double ans : rhs.ans) {
            lhs << ' ' << ans;
        }
        return lhs;
    }
};

struct Solver {
    int id;

    Output solve(Input input) {
        vector<long double> ans;
        vector<vector<long long>> d;
        d.resize(input.n);
        for (int i = 0; i < input.n; ++i) {
            d[i].assign(input.d[i].begin(), input.d[i].end());
            d[i][i] = 0;
        }
        for (int k = 0; k < input.n; ++k) {
            for (int i = 0; i < input.n; ++i) {
                for (int j = 0; j < input.n; ++j) {
                    if (d[i][k] != -1 && d[k][j] != -1) {
                        if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]) {
                            d[i][j] = d[i][k] + d[k][j];
                        }
                    }
                }
            }
        }
        for (int i = 0; i < input.q; ++i) {
            int from = input.u[i];
            int to = input.v[i];
            vector<long double> t;
            t.resize(input.n);
            for (int j = 0; j < input.n; ++j) {
                if (d[j][to] >= 0 && d[j][to] <= input.e[j]) {
                    t[j] = d[j][to] * (long double)(1) / input.s[j];
                } else {
                    t[j] = 1e100;
                }
            }
            for (int l = 0; l < input.n; ++l) {
                for (int j = 0; j < input.n; ++j) {
                    for (int k = 0; k < input.n; ++k) {
                        if (d[j][k] >= 0 && d[j][k] <= input.e[j]) {
                            long double time = t[k] +
                                d[j][k] * (long double)(1) / input.s[j];
                            t[j] = min(t[j], time);
                        }
                    }
                }
            }
            ans.push_back(t[from]);
        }
        return {id, ans};
    }
};

int main(void) {
    using namespace chrono;
    auto start = high_resolution_clock::now();
    ifstream fin(getNewest());
    ofstream fout("output.txt");
    int q;
    fin >> q;
    vector<Input> inputs;
    for (int i = 0; i < q; ++i) {
        Input input;
        fin >> input;
        inputs.push_back(input);
    }
    vector<future<Output>> futures;
    mutex mtx;
    int solved = 0;
    for (int i = 0; i < q; ++i) {
        futures.push_back(async([i, &inputs, &solved, &q, &mtx, &start]() {
            Solver s{i};
            Output ans = s.solve(inputs[i]);
            mtx.lock();
            ++solved;
            auto end = high_resolution_clock::now();
            auto elapsed = duration_cast<milliseconds>(end - start);
            cout << (elapsed.count() * 1e-3) << "s,\tSolved " << solved 
            << " of " << q << endl;
            mtx.unlock();
            return ans;
        }));
    }
    for (int i = 0; i < q; ++i) {
        fout << futures[i].get() << "\n";
    }
    auto end = high_resolution_clock::now();
    auto elapsed = duration_cast<milliseconds>(end - start);
    cout << (elapsed.count() * 1e-3) << "s,\tCalculation finished" << endl;
    return 0;
}
