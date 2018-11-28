#include <iostream>
#include <cmath>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

int main(){

  int T;
  cin >> T;
  for(int o = 1; o <= T; o++){
    int n, k;
    cin >> n >> k;

    priority_queue<int> q;

    q.push(n);

    int la, lb, lv;

    while(k > 0){

      int lv = q.top();
      q.pop();

      la = ceil((float)lv/2) - 1;
      lb = lv - 1 - la;

      q.push(la);
      q.push(lb);


      k -= 1;
    }

    cout << "Case #" << o << ": " << max(la, lb) << " " << min(la, lb) << endl;

  }

  return 0;
}
