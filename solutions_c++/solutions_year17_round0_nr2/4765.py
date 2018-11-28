#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <deque>

using namespace std;

void get_digits(long long number, deque<int> &digits) {

    while(1) {
        int res = number % 10;

        digits.push_front(res);

        number /= 10;
        if (number == 0) break;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(2);
    cout << fixed;

    int T;

    cin >> T;

    for(int i = 1;i <= T;++i) {
        long long N;
        cin >> N;

        long long res = 0;

        deque<int> d;
        get_digits(N, d);

        for(int j = 0;j < d.size() - 1;++j) {
            if (d[j+1] >= d[j]) continue;

            fill(&d[j+1], &d[d.size()], 9);

            d[j]--;
            for(int k = j; k > 0;--k) {
                if (d[k] >= d[k-1]) continue;

                d[k] = 9;
                d[k-1]--;
            }


        }




        for(int j = 0;j < d.size();++j) {
            res *= 10;
            res += d[j];
        }

        cout << "Case #" << i << ": " << res << '\n';
    }



    return 0;
}
