#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> convert(long n) {
    vector<int> ret;
    ret.reserve(18);
    while (n > 0) {
        ret.push_back(n % 10);
        n /= 10;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

long convert(const vector<int> &nums) {
    long ret = 0;
    for (int i = 0; i < nums.size(); ++i) {
        ret = ret * 10 + nums[i];
    }
    return ret;
}

int main() {

    int t;
    long n;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        if (n < 10) {
            cout << "Case #" << i << ": " << n << endl;
            continue;
        }
        vector<int> nums = convert(n);

        for (int i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]) {
                --nums[i];
                for (int j = i + 1; j < nums.size() && nums[j] != 9; ++j) {
                    nums[j] = 9;
                }
            }
        }
        long ret = convert(nums);
        cout << "Case #" << i << ": " << ret << endl;
    }

    return 0;
}