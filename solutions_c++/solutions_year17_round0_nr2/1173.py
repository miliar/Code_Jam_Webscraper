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
    string n;

    friend istream& operator >>(istream& lhs, Input& rhs) {
        return lhs >> rhs.n;
    }
};

struct Output {
    int id;
    string ans;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << "Case #" << (rhs.id + 1) << ": ";
        lhs << rhs.ans;
        return lhs;
    }
};

struct Solver {
    int id;

    Output solve(Input input) {
        string ans;
        ans = input.n;
        for (size_t i = ans.size() - 1; i > 0; --i) {
            if (ans[i] < ans[i - 1]) {
                --ans[i - 1];
                for (size_t j = i; j < ans.size(); ++j) {
                    ans[j] = '9';
                }
            }
        }
        if (ans[0] == '0') {
            ans.erase(ans.begin());
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
