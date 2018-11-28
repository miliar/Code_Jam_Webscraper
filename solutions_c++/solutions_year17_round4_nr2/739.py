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
    int n, c, m;
    vector<unordered_map<int, int>> t;

    friend istream& operator >>(istream& lhs, Input& rhs) {
        lhs >> rhs.n >> rhs.c >> rhs.m;
        rhs.t.resize(rhs.c);
        for (int i = 0; i < rhs.m; ++i) {
            int p, b;
            lhs >> b >> p;
            ++rhs.t[--p][--b];
        }
        return lhs;
    }
};

struct Output {
    int id;
    int roads, cost;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << "Case #" << (rhs.id + 1) << ": " << rhs.roads << ' ' << rhs.cost;
        return lhs;
    }
};

struct Solver {
    int id;

    int check(int roads, const vector<unordered_map<int, int>>& p, int n) {
        int cost = 0;
        int free = roads;
        int was1 = 0;
        int was2 = 0;
        for (int i = 0; i < n; ++i) {
            int used = 0;
            int rides = p[0].count(i) ? p[0].at(i) : 0;
            used += rides;
            if (rides > free + was2) {
                return -1;
            }
            int d = min(free, rides);
            was1 += d;
            free -= d;
            was2 -= rides - d;
            rides = p[1].count(i) ? p[1].at(i) : 0;
            used += rides;
            if (rides > free + was1) {
                return -1;
            }
            if (i == 0 && rides > free) {
                return -1;
            }
            d = min(free, rides);
            was2 += d;
            free -= d;
            was1 -= rides - d;
            cost += max(0, used - roads);
        }
        return cost;
    }

    Output solve(Input input) {
        int l = 0, r = input.m;
        int ans = 0;
        while (r - l > 1) {
            int cost = check((r + l) / 2, input.t, input.n);
            if (cost > -1) {
                r = (r + l) / 2;
                ans = cost;
            } else {
                l = (r + l) / 2;
            }
        }
        return {id, r, ans};
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
