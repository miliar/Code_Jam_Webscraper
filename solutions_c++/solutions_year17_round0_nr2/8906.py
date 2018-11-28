//
// Created by Andrei Zakharevich on 07.04.17.
//

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
int main() {
    int T;
    cin >> T;
    for (int j = 1; j <= T; j++) {
        long long N;
        cin >> N;
        long long cur = N;
        vector<long long> nums;
        while (cur) {

            if (!nums.size() || cur % 10 <= nums.back()) {
                nums.push_back(cur % 10);
                cur /= 10;
            } else {
                for (int i = 0; i < nums.size(); i++)
                    nums[i] = 9;
                cur -= 1;
            }

        }
        cout << " Case #" << j << ": ";
        for (auto i = nums.rbegin(); i != nums.rend(); i++)
            cout << *i;
        cout << endl;
    }
    return 0;
}