#include <bits/stdc++.h>

using namespace std;

int main() {
   int n, k;
   string s;
   cin >> n;
   for(int i = 1; i <= n; ++i) {
      cin >> s >> k;
      int cnt = 0;
      queue<int> deadline;
      for(int j = 0; j < s.size(); ++j) {
         if((deadline.size() % 2 == 0) == (s[j] == '-')) {
            cnt++;
            deadline.push(j+k-1);
         }
         if(!deadline.empty() && deadline.front() == j)
            deadline.pop();
      }
      cout << "Case #" << i << ": ";
      if(deadline.empty()) cout << cnt << endl;
      else cout << "IMPOSSIBLE" << endl;
   }
}
