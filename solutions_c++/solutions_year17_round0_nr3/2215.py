#include <iostream>
using namespace std;

typedef pair<long long, long long> LR;

LR get_stalls(long long n, long long k) {
    long long max = n;
    long long min = n-1;
    long long intervals_max = 1;
    long long intervals_min = 0;
    while(true) {
        long long next_max = (max-1)/2 + (max-1)%2;
        long long next_min = next_max-1;
        long long aux = 0;

        k -= intervals_max;
        if(max % 2 != 0) {
            if(k <= 0) {
                return LR(next_max, next_max);
            }
            intervals_max *= 2;
        } else {
            if (k <= 0) {
                return LR(next_max, next_min);
            }
            aux = intervals_max;
        }

        k -= intervals_min;
        if(min % 2 != 0) {
            if (k <= 0) {
                return LR(next_min, next_min);
            }
            intervals_min *= 2;
        } else {
            if (k <= 0) {
                return LR(next_max, next_min);
            }
            intervals_max += intervals_min;
        }
        intervals_min += aux;
        max = next_max;
        min = next_min;
    }
}

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        long long n, k;
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        LR result = get_stalls(n, k);
        cout << result.first << " " << result.second << endl;
    }
}