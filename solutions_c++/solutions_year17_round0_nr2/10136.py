#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

long long solve(long long N){
    vector<int> nums;
    int k, n, change;
    k = 0;

    while(N >= pow(10, k)){
        n = int(N % (long long)pow(10, k+1) / pow(10, k));
        nums.push_back(n);
        k++;
    }

    change = 100;
    for(int i=nums.size()-1; i>=1; i-=1){
        if(nums[i] > nums[i-1]){
            change = i;
            break;
        }
    }

    if(change == 100) return N;

    while(change < nums.size()-1 && nums[change] == nums[change+1])
        change++;

    nums[change] -= 1;
    for(int i=0; i<change; i++) nums[i] = 9;

    long long ans = 0;
    for(int k=0; k<nums.size(); k++) ans += nums[k] * (long long)pow(10, k);
    return ans;
}

int main(){
    int T;
    long long N, ans;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N;
        ans = solve(N);
        cout << "Case #" << t << ": " << ans << endl;
    }
}
