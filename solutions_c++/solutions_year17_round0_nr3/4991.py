
#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

using Int = int64_t;

struct S {
  S() : stalls(0), num(0){}
  S(Int stalls, Int num) : stalls(stalls), num(num){}
  bool operator<(const S &rhs) const {
    return stalls < rhs.stalls;
  }
  Int stalls;
  mutable Int num;
};

void solve(){
  int64_t people, stalls;
  cin >> stalls >> people;
  vector<S> vs;
  set<S> ss;
  vs.push_back({stalls, 1});
  for(size_t i = 0; vs[i].stalls > 0; ++i){
    S s = vs[i];
    if(s.stalls & 1){
      vs.push_back(S{s.stalls/2, s.num*2});
    }
    else{
      vs.push_back(S{s.stalls/2, s.num});
      vs.push_back(S{s.stalls/2-1, s.num});
    }
  }

  for(auto &i : vs){
    auto it = ss.find(i);
    if(it != ss.end()) it->num += i.num;
    else ss.insert(i);
  }
  //cout << ss.size() << endl;

  /*for(auto it = ss.rbegin(); it != ss.rend(); ++it){
    cout << it->stalls << " " << it->num << endl;
  }*/
  //cout << endl;
  //cout << endl;
  for(auto it = ss.rbegin(); it != ss.rend(); ++it){
    people = people - it->num;
    //cout << people << endl;
    if(people <= 0){
      Int half = it->stalls/2;
      if(it->stalls & 1) cout << half << " " << half << endl;
      else cout << half << " " << half - 1 << endl;
      break;
    }
  }

  return;
}

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i){
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
