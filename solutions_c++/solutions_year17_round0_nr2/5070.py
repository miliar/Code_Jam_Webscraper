#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

vector<long> intToList(long a){
    vector<long> nums;
    while (a>9) {
        nums.push_back(a%10);
        a /= 10;
    }
    nums.push_back(a);
    reverse(nums.begin(), nums.end());
    return nums;
}

long listToInt(vector<long> nums){
    long n = 0;
    for (int i = 0; i < nums.size(); i++){
        n += nums[i] * (long)pow(10, nums.size()-i-1);
    }
    return n;
}

long backtracking(vector<long> nums){
    for (int i = 0; i < nums.size()-1; i++){
        if (nums[i]>nums[i+1]){
            nums[i]-=1;
            for (int j = i+1; j<nums.size(); j++) nums[j] = 9;
            return backtracking(nums);
        }
    }
    return listToInt(nums);
}

int main(){
    int t;
    cin >> t;
    for (int ncase = 1; ncase <= t; ncase++){
        long n; cin >> n;
        printf("Case #%d: ", ncase);
        cout << backtracking(intToList(n)) << endl;
    }
}