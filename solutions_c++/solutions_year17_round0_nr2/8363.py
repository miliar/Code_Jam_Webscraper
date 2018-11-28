#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;
long long solve(long long N){
    vector<int> working;
    while(N > 0){
        working.push_back(N%10);
        N /= 10;
    }
    int n = working.size();
    int last_pos = -1;
    for(int i = 1; i < n; ++i){
        int curr = working[i];
        if(curr > working[i-1]){
            working[i]--;
            last_pos = i;
        } 
    }
    for(int i = 0; i < last_pos; ++i){
        working[i] = 9;
    }
    long long ret = 0;
    for(int i = n-1; i >= 0; --i){
        ret = ret*10 + working[i];
    }
    return ret;
    
}
int main(){
    size_t T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        long long N;
        cin >> N;
        cout << "Case #" << t << ": " << solve(N) << endl;
    }
}

