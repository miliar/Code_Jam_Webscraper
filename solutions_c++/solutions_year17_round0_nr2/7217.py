#include <iostream>
#include <fstream>
#include <deque>

using namespace std;

deque<int> digits;

void make_tidy() {
    bool complete = true;
    for (int i = 1; i < digits.size(); ++i) {
        if (digits[i] < digits[i-1]) {
            digits[i-1]--;
            for (int j = i; j < digits.size(); ++j)
                digits[j] = 9;
            complete = false;
            break;
        }
    }
    if (! complete)
        make_tidy();
}

long long last_tidy(long long N) {
    while (N > 0) {
        digits.push_front(N%10);
        N /= 10;
    }
    make_tidy();
    long long tidy_num = 0;
    long long pos = 1;
    while (! digits.empty()) {
        tidy_num += digits.back() * pos;
        digits.pop_back();
        pos *= 10;
    }
    return tidy_num;
}

int main() {
    ifstream input("B-large.in");
    if (! input) {
        cerr << "Could not open file!" << endl;
        return 1;
    }
    ofstream output("B-large.out");
    int T;
    input >> T;
    for (int x = 1; x <= T; x++) {
        long long N;
        input >> N;
        output << "Case #" << x << ": ";
        output << last_tidy(N) << endl;
    }
    input.close();
    output.close();

    return 0;
}