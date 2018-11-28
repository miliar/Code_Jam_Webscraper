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
    int n;
    int r, o, y, g, b, v;
    friend istream& operator >>(istream& lhs, Input& rhs) {
        return lhs >> rhs.n >> rhs.r >> rhs.o >> rhs.y >> rhs.g >> rhs.b >> rhs.v;
    }
};

struct Output {
    int id;
    string s;

    friend ostream& operator <<(ostream& lhs, const Output& rhs) {
        lhs << "Case #" << (rhs.id + 1) << ": " << rhs.s;
        return lhs;
    }
};

struct Solver {
    int id;
    string impossible = "IMPOSSIBLE";

    Output solve(Input input) {
        string rn = "R";
        string yn = "Y";
        string bn = "B";
        int q = 0;
        string l;
        while (input.g > 0) {
            --input.g;
            --input.r;
            rn += "GR";
        }
        if (rn.size() > 1) {
            l = rn;
            ++q;
        }
        while (input.v > 0) {
            --input.v;
            --input.y;
            yn += "VY";
        }
        if (yn.size() > 1) {
            l = yn;
            ++q;
        }
        while (input.o > 0) {
            --input.o;
            --input.b;
            bn += "OB";
        }
        if (bn.size() > 1) {
            l = bn;
            ++q;
        }
        if (input.r < 0 || input.y < 0 || input.b < 0) {
            return { id, impossible };
        }
        string ans;
        while (input.r + input.y + input.b > 0) {
            int rr = input.r;
            int yy = input.y;
            int bb = input.b;
            if (!ans.empty() && ans.back() == 'R') {
                rr = -1;
            }
            if (!ans.empty() && ans.back() == 'Y') {
                yy = -1;
            }
            if (!ans.empty() && ans.back() == 'B') {
                bb = -1;
            }
            if (rr >= yy && rr >= bb && !ans.empty() && ans[0] == 'R') {
                if (rr <= 0) {
                    return { id, impossible };
                }
                --input.r;
                ans += rn;
                rn = "R";
            } else if (yy >= rr && yy >= bb && !ans.empty() && ans[0] == 'Y') {
                if (yy <= 0) {
                    return{ id, impossible };
                }
                --input.y;
                ans += yn;
                yn = "Y";
            } else if (bb >= rr && bb >= yy && !ans.empty() && ans[0] == 'B') {
                if (bb <= 0) {
                    return{ id, impossible };
                }
                --input.b;
                ans += bn;
                bn = "B";
            } else if (rr >= yy && rr >= bb) {
                if (rr <= 0) {
                    return { id, impossible };
                }
                --input.r;
                ans += rn;
                rn = "R";
            }
            else if (yy >= rr && yy >= bb) {
                if (yy <= 0) {
                    return{ id, impossible };
                }
                --input.y;
                ans += yn;
                yn = "Y";
            }
            else if (bb >= rr && bb >= yy) {
                if (bb <= 0) {
                    return{ id, impossible };
                }
                --input.b;
                ans += bn;
                bn = "B";
            }
        }
        if (ans.empty() && q == 1) {
            ans = l;
            ans.erase(ans.begin());
        }
        if (ans.empty() || ans[0] == ans.back()) {
            return{ id, impossible };
        }
        return{ id, ans };
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
