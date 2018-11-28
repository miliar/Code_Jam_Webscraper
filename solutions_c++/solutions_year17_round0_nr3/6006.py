//
// Created by jeraz on 4/7/17.
//

#include <iostream>
#include <cmath>

using namespace std;

struct Counts{
    long max;
    long min;
    long maxCount;
    long minCount;

    void rec (int depth);
};

void Counts:: rec(int depth) {

    while (depth > 0) {
        if (max == min) {
            maxCount *= 2;
            minCount *= 2;
        } else if (max % 2 == 0) {
            minCount = (2 * minCount) + maxCount;
        } else {
            maxCount = (2 * maxCount) + minCount;
        }
        if (max == min && max % 2 == 1) {
            max = max / 2;
            min = max;
        } else {
            max = max / 2;
            min = max - 1;
        }

        depth --;
    }

}


int main() {
    int t;
    cin >> t;

    for (unsigned i = 0; i < t; i++) {
        long n, k;
        cin >> n >> k;
        long max, min;
        max = n / 2;
        min = n / 2;
        if (n % 2 == 0) min --;
        int depth = (int)floor(log2(k));
        long index = k - (long)pow(2, depth);

        Counts c;
        c.max = max;
        c.min = min;
        c.maxCount = 1;
        c.minCount = 1;
        c.rec(depth - 1);

        if (k != 1) {
            if (index < c.maxCount) {
                if (c.max % 2 == 0) {
                    max = c.max / 2;
                    min = (c.max / 2) - 1;
                } else {
                    max = c.max / 2;
                    min = c.max / 2;
                }
            } else {
                if (c.min % 2 == 0) {
                    max = c.min / 2;
                    min = (c.min / 2) - 1;
                } else {
                    max = c.min / 2;
                    min = c.min / 2;
                }
            }
        }
        //if (k == n) min = 0;
        cout << "Case #" << i + 1 << ": " << max << " " << min <<endl;

    }

    return 0;
}