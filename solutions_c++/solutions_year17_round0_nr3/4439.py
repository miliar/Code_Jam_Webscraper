#include <iostream>
#include <queue>
#include <vector>
#include <cstdio>

using namespace std;

int main(){

  auto comp = [](const pair<int,int>& p1, const pair<int,int>& p2){
    if(p1.second-p1.first != p2.second-p2.first){
      return p1.second-p1.first < p2.second-p2.first;
    } else {
      return (p1.first > p2.first ? true : false);
    }
  };

  int t, no = 1;
  cin >> t;
  while(t--){
    int n, k;
    cin >> n >> k;
    priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(comp)> q(comp);
    q.emplace(make_pair(0,n-1));

    for(int i = 0; i < k - 1; i++){
      auto interval = q.top();
      // cout << i << "\t" << interval.first << "\t" << interval.second << endl;
      q.pop();
      int m = (interval.second+interval.first)/2;
      auto left = make_pair(interval.first,m-1);
      auto right = make_pair(m+1,interval.second);
      if(comp(left,right)){
        if(left.second-left.first >= 0) q.emplace(left);
        if(right.second-right.first >= 0) q.emplace(right);
      } else {
        if(right.second-right.first >= 0) q.emplace(right);
        if(left.second-left.first >= 0) q.emplace(left);
      }
    }
    auto last_interval = q.top();
    int middle = (last_interval.second+last_interval.first)/2;
    // cout << q.size() << "\t" << last_interval.first << "\t" << middle << "\t" << last_interval.second << endl;
    int minimum = min(middle-last_interval.first,last_interval.second-middle);
    int maximum = max(middle-last_interval.first,last_interval.second-middle);
    printf("Case #%d: %d %d\n", no, maximum, minimum);
    no++;
  }

  return 0;
}
