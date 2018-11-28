#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int64_t solve(int64_t N) {
        vector<int> d;
        while (N > 0) {
                d.push_back(N % 10);
                N /= 10;
        }
        int n = d.size(), m = -1;
        for (int i = 0; i < n - 1; i++) {
                if (d[i] < d[i + 1]) {
                        d[i + 1]--;
                        m = i;
                }
        }
        int64_t x = 0;
        for (int i = n - 1; i >= 0; i--)
                x = x * 10 + (i > m ? d[i] : 9);
        return x;
}

int main(int argc, char **argv)
{
        int T;
        cin >> T;
        for (int testcase = 0; testcase < T; testcase++) {
                int64_t N;
                cin >> N;
                cout << "Case #" << testcase+1 << ": ";
                cout << solve(N);
                cout << endl;
        }
        return 0;
}
