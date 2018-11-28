#include <bits/stdc++.h>

using namespace std;

void true_main(int testcase) {
    long long n, k;

    cin >> n >> k;

    long long r = n;
    long long l = n - 1;
    long long cr = 1;
    long long cl = 0;

    long long step = 1;
    while (step < k) {
        k -= step;

        if (r % 2 == 0) {
            r = r / 2;
            l = r - 1;
            cl += step;
        }
        else {
            r = l / 2;
            l = r - 1;
            cr += step;
        }
        step *= 2;
    }

    if (k <= cr) {
        l = r - r / 2 - 1;
        r = r / 2;
    }
    else {
        r = l / 2;
        l = l - r - 1;
    }
    cout << "Case #" << testcase << ": " << r << " " << l << "\n";

}

main () {
#define FILES
#ifdef FILES
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif
    int T;

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        true_main(t);
    }
}
/*
300 -  1
150 -  1, 149 -   1
 75 -  1,  74 -   3
 37 -  5,  36 -   3
 18 - 13,  17 -   3
  9 - 13,   8 -  19
  4 - 45,   3 -  19
  2 - 45,   1 -  83
  1 - 45,   0 - 211
-------------------
       0 - 300

                                              300
                      150                                             149
           75                      74                      74                      74
     37          37          37          36          37          36          37          36
  18    18    18    18    18    18    18    17    18    18    18    17    18    18    18    17
 9  8  9  8  9  8  9  8  9  8  9  8  9  8  8  8  9  8  9  8  9  8  8  8  9  8  9  8  9  8  8  8


*/
