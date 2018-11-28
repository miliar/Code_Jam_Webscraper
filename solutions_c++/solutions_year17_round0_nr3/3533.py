#include <iostream>
#include <c++/vector>
#include <c++/fstream>
#include <c++/cmath>
#include <c++/algorithm>
#include <functional>

using namespace std;

// G 0 0 0 1 0 0 0 G

struct Solve {
    Solve(int n, int k) {
        if (k == n) {
            answer = "0 0";
            return;
        }
        bt.resize(k * 2);
        int i = 1;
        k -= 1;
        bt[0] = n;

        int layer = 1;

        while (k > 0) {

            vector<int> row;

            int c = 0;
            while (c++ < pow(2, layer)) {

                int p_space = bt[parent(i + c)];
                auto r = split(p_space);
                row.emplace_back(r.first);
                row.emplace_back(r.second);

                c++;

            }

            sort(row.begin(), row.end());

//            for (auto n : row) {
//                cout << n << ", ";
//            }cout << endl;

            while (!row.empty()) {
                if (k > 0) {
                    bt[i++] = row.back();
                    k--;
                } else {
                    break;
                }
                row.pop_back();
            }

            layer++;

        }

        // create answer string.

        int answer_working_space = bt[i - 1]; // last calculated value
        n = answer_working_space;

        int rem = n - 1;
        int half = rem / 2;
        if (rem % 2 == 0) {
            answer = to_string(half) + " " + to_string(half);
        } else {
            answer = to_string(half + 1) + " " + to_string(half);
        }

//        for (auto n : bt) {
//            cout << n << ", ";
//        } cout << ": " << answer_working_space << " -- " << i - 1 << endl;
    }

    // parent index of i.
    int parent(int i) {
        return (i - 1) / 2;
    }

    // the split values of working-space N.
    pair<int, int> split(int n) {
        int rem = n - 1;
        int half = rem / 2;
        if (rem % 2 == 0) {
            return make_pair(half, half);
        }
        return make_pair(half + 1, half);
    }

    vector<int> bt; // working space of the nth entrant.

    string answer = "";
};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);


    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    string line;
    int N;
    int K;

    while (ifs >> N) {
        ifs >> K;

        Solve solution(N, K);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}