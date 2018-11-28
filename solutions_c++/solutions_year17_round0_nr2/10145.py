#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

bool is_valid (long long num) {
    string num_str = to_string(num);
    int len = num_str.length();

    if (len <= 1) {
        return true;
    }

    char last_num_ch = num_str.at(0);
    char num_ch;

    for (int i = 1; i < len; ++i) {
        num_ch = num_str.at(i);

        if (num_ch < last_num_ch) {
            return false;
        }

        last_num_ch = num_ch;
    }

    return true;
}

long long get_largest_num (long long num) {
    for (long long i = num; i >= 1; --i) {
        if (is_valid(i)) {
            return i;
        }
    }
}

int main () {
    vector<string> filenames = {"small"};
    // vector<string> filenames = {"eg"};

    for (string filename : filenames) {
        int T;
        ifstream in;
        ofstream out;

        in.open(filename + ".in");
        out.open(filename + ".out");

        string tmp;

        getline(in, tmp);
        T = stoi(tmp);

        cout << "T = " << T << endl;

        for (int i = 0; i < T; i++) {
            long long N, L;

            getline(in, tmp);
            N = atoll(tmp.c_str());

            L = get_largest_num(N);

            cout << "N = " << N << endl;
            cout << "L = " << L << endl;

            out << "Case #" << i + 1 << ": " << L << endl;
        }

        in.close();
        out.close();
    }

    return 0;
}
