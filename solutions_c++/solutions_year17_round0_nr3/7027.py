#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>

using namespace std;

#define IS_EVEN(a) (a % 2 == 0)
#define IS_ODD(a) (a % 2 == 1)
#define MIN min
#define MAX max

class Bathroom {
public:
    Bathroom (long long stall_c) {
        this->stall_c = stall_c + 2;

        this->remaining_s = stall_c;

        this->stalls = vector<bool>(this->stall_c);

        fill(this->stalls.begin(), this->stalls.end(), false);

        this->stalls.at(0) = true;
        this->stalls.at(this->stall_c - 1) = true;

        this->display_bathroom();
    }

    long long stall_c;

    long long remaining_s;

    vector<bool> stalls;

    vector<long long> get_stall_pos_l_r () {
        --this->remaining_s;

        long long pos, l, r, pos_s, len_s, stop_s;

        vector<long long> pos_and_len = this->get_pos_and_len_of_sparsest();

        pos_s = pos_and_len.at(0);
        len_s = pos_and_len.at(1);
        stop_s = pos_s + len_s;

        /*
        1,0,0,0,0,1
        1,0,1,0,0,1
        1,0,1,1,0,1
        */

        /*
        1,0,0,0,0,0,1
        1,0,0,1,0,0,1
        1,1,0,1,0,0,1
        */

        // If length is even there's no middle so go left
        if (IS_EVEN(len_s)) {
            // cout << "Even" << endl;
            pos = pos_s + (len_s / 2) - 1;
        }
        // If length is odd there's a middle so pick it
        else if (IS_ODD(len_s)) {
            // cout << "Odd" << endl;
            pos = pos_s + ((len_s + 1) / 2) - 1;
        }

        this->stalls.at(pos) = true;

        l = this->count_left(pos);
        r = this->count_right(pos);

        this->display_bathroom();

        // cout << "# Pos = " << pos << ", L = " << l << ", R = " << r << ", Pos_S = " << pos_s << ", Len_S = " << len_s << ", Stop_S = " << stop_s << endl;
        // 1,0,0,0,0,0,0,1

        vector<long long> stall_pos_l_r = {pos, l, r};

        return stall_pos_l_r;
    }

    void display_bathroom () {
        /*
        cout << "{" << this->stalls.at(0);
        for (long long i = 1; i < this->stall_c; ++i) {
            cout << "," << this->stalls.at(i);
        }
        cout << "}" << endl;
        */
    }

    long long count_right (long long pos) {
        long long count = 0;

        for (long long i = pos + 1; ; ++i) {
            if (this->stalls.at(i) == true) {
                break;
            }

            ++count;
        }

        return count;
    }

    long long count_left (long long pos) {
        long long count = 0;

        for (long long i = pos - 1; ; --i) {
            if (this->stalls.at(i) == true) {
                break;
            }

            ++count;
        }

        return count;
    }

    vector<long long> get_pos_and_len_of_sparsest () {
        vector<long long> pos_and_len;
        long long pos = 0, len = 0;

        for (long long i = 0; i < this->stall_c;) {
            if (this->stalls.at(i++) == false) {
                long long l = 1;
                long long p = i - 1;

                for (;;) {
                    if (this->stalls.at(i++) == false) {
                        ++l;

                        continue;
                    }

                    if (l > len) {
                        len = l;
                        pos = p;
                    }

                    break;
                }
            }
        }

        pos_and_len = {pos, len};

        return pos_and_len;
    }
};

vector<long long> get_max_min (long long stalls, long long people) {
    Bathroom b(stalls);
    vector<long long> max_min_last_person;
    vector<long long> pos_l_r;

    for (long long i = 0; i < people; i++) {
        pos_l_r = b.get_stall_pos_l_r();
        // cout << "Pos = " << pos_l_r.at(0) << ", L = " << pos_l_r.at(1) << ", R = " << pos_l_r.at(2) << endl;
    }

    long long l = pos_l_r.at(1), r = pos_l_r.at(2);

    max_min_last_person = {MAX(l, r), MIN(l, r)};

    return max_min_last_person;
}

int main () {
    // vector<string> filenames = {"small_1"};
    // vector<string> filenames = {"small_2"};
    // vector<string> filenames = {"large"};
    vector<string> filenames = {"C-small-1-attempt0"};

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
            long long N, K, _min, _max;

            in >> N;
            in >> K;

            getline(in, tmp);

            cout << "N = " << N << ", K = " << K << endl;

            vector<long long> max_min = get_max_min(N, K);
            _max = max_min.at(0);
            _min = max_min.at(1);

            cout << "N = " << N << ", K = " << K << ", max = " << _max << ", min = " << _min << endl;

            out << "Case #" << i + 1 << ": " << _max << " " << _min << endl;
        }

        in.close();
        out.close();
    }

    return 0;
}
