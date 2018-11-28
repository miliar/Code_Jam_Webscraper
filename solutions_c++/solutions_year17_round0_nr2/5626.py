#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

long long tidy_num(long long N) {
    if (N < 10) return N;

    vector<int> nums;
    long long temp = N;

    while (temp) {
        nums.push_back(temp % 10);
        temp /= 10;
    }

    reverse(nums.begin(), nums.end());
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] < nums[i - 1]) {
            --nums[i - 1];
            for (int j = i - 2; j >= 0; --j) {
                if (nums[j] > nums[j + 1]) {
                    --nums[j];
                    i = j + 1;
                }
            }

            for (int j = i; j < nums.size(); ++j) {
                nums[j] = 9;
            }
            break;
        }
    }

    temp = 0;
    for (int i = 0; i < nums.size(); ++i) {
        temp *= 10;
        temp += nums[i];
    }

    return temp;
}

int main(int argc, char **argv) {
    int n;
    long long N;

    long long res;

    //cout<< tidy_num(20)<< endl;
    cin>> n;
    for (int i = 1; i <= n; ++i) {
        cin>> N;
        res = tidy_num(N);
        cout<< "Case #"<< i<< ": "<< res<< endl;
    }

    return 0;
}
