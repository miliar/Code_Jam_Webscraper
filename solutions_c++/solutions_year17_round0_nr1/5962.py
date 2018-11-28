#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000000;

int flips(vector<int> pancakes, int flipper_size, int want) {
  int temp[pancakes.size()];
  for(int i = 0; i < pancakes.size(); i++){
      temp[i] = 0;
  }
  int sum=0, ans=0;
  for(int i = 0; i < pancakes.size(); i++) {
    temp[i] = (pancakes[i]+sum)%2 != want;
    sum += temp[i] - (i>=flipper_size-1?temp[i-flipper_size+1]:0);
    ans += temp[i];
    if(i>pancakes.size()-flipper_size and temp[i]!=0) return INF;
  }
  return ans;
}

int main() {
    int testcases;
    cin >> testcases;
    for(int testcase = 1; testcase <= testcases; testcase++){
        string current_state;
        int flipper_size;
        cin >> current_state >> flipper_size;
        vector<int> pancakes;
        for(auto i : current_state){
            if(i == '+')
                pancakes.push_back(1);
            else
                pancakes.push_back(0);
        }
        int ans = flips(pancakes, flipper_size, 1);
        if(ans == INF){
            cout << "Case #" << testcase << ": " << "IMPOSSIBLE" << endl;
        }
        else{
            cout << "Case #" << testcase << ": " << ans << endl;
        }
    }
}