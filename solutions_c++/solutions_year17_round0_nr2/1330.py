#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

int keta(long long n) {
    int cnt = 0;
    while (n > 0) {
        cnt++;
        n /= 10;
    }
    return cnt;
}

void vectorize(long long n, vector<int> &nums) {
    while (n > 0) {
        nums.push_back(n % 10);
        n /= 10;
    }
    reverse(nums.begin(), nums.end());
}
int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        long long n;
        cin >> n;
        vector<int> nums;
        vectorize(n, nums);
        int k = nums.size();

        FOR(i, 0, k - 1) {
            int idx = k - i - 1;
            if (nums[idx - 1] > nums[idx]) {
                FOR(j, idx, k)
                    nums[j] = 9;
                nums[idx - 1]--;
            }

        }
        bool leadingzero = true;
        for (auto t : nums) {
            if (leadingzero&&t == 0)
                continue;
            else
                leadingzero = false;
            cout << t;

        }
        cout << endl;
    }
    return 0;
}