#include <iostream>
#include <vector>

using namespace std;

bool is_non_decreasing(long N) {
    cerr << N << endl;
    int low_digit = N%10;

    while(N > 0) {
        int next_digit = N%10;
        if(next_digit > low_digit) {
            return false;
        }
        if(next_digit < low_digit) {
            low_digit = next_digit;
        }
        N /= 10;
    }

    return true;
}

long least_non_increasing(long N) {
    for (long n = N; n > 0; --n) {
        if(is_non_decreasing(n)) {
            return n;
        }
    }

    return 0;
}

vector<int> str2digits(const string& input) {
    vector<int> result;
    for(const auto& d : input) {
        result.push_back(d-'0');
    }

    return result;
}

vector<int> last_tidy(vector<int> number) {
    vector<int>::iterator last_digit = number.begin();
    vector<int>::iterator cur_digit = number.begin();
    cur_digit++;
    for (; cur_digit != number.end(); ++cur_digit) {
        if(*cur_digit < *last_digit) {
            //cerr << "L: " << *last_digit << " C: " << *cur_digit << endl;
            (*last_digit)--;
            for (; cur_digit != number.end(); ++cur_digit) {
                (*cur_digit) = 9;
            }
            return last_tidy(number);
        }
        last_digit = cur_digit;
    }

    return number;
}


int main() {

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string N;
        cin >> N;

        /*for(auto c : str2digits(N)) {
            cout << c << ",";
        }
        cout << endl;*/

        cout << "Case #" << t+1 << ": ";

        bool beginning = true;
        for(auto c : last_tidy(str2digits(N))) {
            if(beginning && c == 0) {
                continue;
            }
            beginning = false;
            cout << c;
        }
        cout << endl;
    }

    return 0;
}