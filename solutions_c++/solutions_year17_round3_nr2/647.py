#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
struct node{
  int s;int t;int id;
  bool operator<(const node &right) const{
    return s < right.s;
  }
};

void solve(){
  int ac,aj;
  cin >> ac >> aj;
  vector< node > tasks;
  int sumc = 0,sumj = 0;;
  for(int i = 0;i < ac;++i){
    int s,t;
    cin >> s >> t;
    node n = {s,t,0};
    tasks.push_back(n);
    sumc += t - s;
  }
  for(int i = 0;i < aj;++i){
    int s,t;
    cin >> s >> t;
    node n = {s,t,1};
    tasks.push_back(n);
    sumj += t - s;
  }
  sort(tasks.begin(),tasks.end());
  node n = {tasks[0].s+1440,
            tasks[0].t+1440,
            tasks[0].id};
  tasks.push_back(n);
  vector< P > spaces;
  for(int i = 0;i < ac+aj;++i){
    int sp = tasks[i+1].s - tasks[i].t;
    if(tasks[i].id == 0 &&
       tasks[i+1].id == 0)
      spaces.push_back(P(sp,0));
    else if(tasks[i].id == 1 &&
            tasks[i+1].id == 1)
      spaces.push_back(P(sp,1));
    else
      spaces.push_back(P(sp,2));
  }
  sort(spaces.begin(),spaces.end());
  int res = 0;
  for(int i = 0;i < ac+aj;++i){
    if(spaces[i].second == 0){
      if(sumc + spaces[i].first <= 720){
        sumc += spaces[i].first;
      }else{
        res += 2;
        sumc = 720;
      }
    }else if(spaces[i].second == 1){
      if(sumj + spaces[i].first <= 720){
        sumj += spaces[i].first;
      }else{
        res += 2;
        sumj = 720;
      }
    }else{
      ++res;
    }
  }
  cout << res << endl;
}


int main(void){
  int t;
  cin >> t;
  for(int i = 0;i < t;++i){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
