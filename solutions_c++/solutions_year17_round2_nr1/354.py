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
    int d, n;
    vector<int> s, k;

    friend istream& operator >>(istream& lhs, Input& rhs) {
        lhs >> rhs.d >> rhs.n;
        rhs.k.resize(rhs.n);
        rhs.s.resize(rhs.n);
        for (int i = 0; i < rhs.n; ++i) {
            lhs >> rhs.k[i] >> rhs.s[i];
        }
        return lhs;
    }
};

struct Output {
    int id;
    long double ans;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << fixed << setprecision(10);
        lhs << "Case #" << (rhs.id + 1) << ": " << rhs.ans;
        return lhs;
    }
};

struct Solver {
    int id;

    Output solve(Input input) {
        long double ans = 1e100;
        for (int i = 0; i < input.n; ++i) {
            long double d = input.d - input.k[i];
            long double t = d / input.s[i];
            long double v = input.d / t;
            ans = min(ans, v);
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
