#include <iostream>
#include <string>
#include <set>
#include <queue>

using namespace std;

struct state{
  string a;
  int count;
};

string swap(string a, int x, int len){
  for(int i = x; i < x + len; i++){
    if(a[i] == '-')
      a[i] = '+';
    else
      a[i] = '-';
  }
  return a;
}

bool check(string a){
  for(int i = 0; i < a.size(); i++){
    if(a[i] == '-')
      return false;
  }
  return true;
}

int main(){
  int T;
  int xxx;
  cin >> T;
  for(xxx = 1; xxx <= T; xxx++){
    queue<struct state> qq;
    string a;
    struct state xy;
    int d;
    cin >> a >> d;
    xy.a = a;
    xy.count = 0;
    qq.push(xy);
    set<string> visited;
    int have_result = 0;
    while(!qq.empty()){
      struct state xy = qq.front();
      qq.pop();
      int visited_count = visited.size();
      visited.insert(xy.a);
      if(visited.size() == visited_count)
        continue;
      if(check(xy.a)){
        printf("Case #%d: %d\n",xxx, xy.count);
        have_result = 1;
        break;
      }
      for(int i = 0; i < xy.a.size() - d + 1; i++){
          struct state x;
          x.a = swap(xy.a, i, d);
          x.count = xy.count + 1;
          qq.push(x);
      }
    }
    if(have_result == 0)
    printf("Case #%d: IMPOSSIBLE\n",xxx);

  }
  return 0;
}
