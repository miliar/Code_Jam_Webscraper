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
    int n, p;
    vector<int> x;

    friend istream& operator >>(istream& lhs, Input& rhs) {
        lhs >> rhs.n >> rhs.p;
        rhs.x.resize(4);
        for (int i = 0; i < rhs.n; ++i) {
            int x;
            lhs >> x;
            ++rhs.x[x % rhs.p];
        }
        return lhs;
    }
};

struct Output {
    int id;
    int ans;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << "Case #" << (rhs.id + 1) << ": " << rhs.ans;
        return lhs;
    }
};

struct Solver {
    int id;
    int p;
    tuple<int, int, int> pos;
    int left;
    map<tuple<int, int, int>, int> ans[4];

    int solve() {
        if (ans[left].count(pos)) {
            return ans[left][pos];
        }
        int& res = ans[left][pos];
        if (get<0>(pos) == 0 && get<1>(pos) == 0 && get<2>(pos) == 0) {
            return res = 0;
        }
        res = 0;
        if (get<0>(pos) > 0) {
            left = (left + 1) % p;
            --get<0>(pos);
            res = max(res, solve());
            ++get<0>(pos);
            left = (left + p - 1) % p;
        }
        if (get<1>(pos) > 0) {
            left = (left + 2) % p;
            --get<1>(pos);
            res = max(res, solve());
            ++get<1>(pos);
            left = (left + p - 2) % p;
        }
        if (get<2>(pos) > 0) {
            left = (left + 3) % p;
            --get<2>(pos);
            res = max(res, solve());
            ++get<2>(pos);
            left = (left + p - 3) % p;
        }
        if (left == 0) {
            ++res;
        }
        return res;
    }

    Output solve(Input input) {
        p = input.p;
        left = 0;
        pos = {input.x[1], input.x[2], input.x[3]};
        return {id, solve() + input.x[0]};
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
