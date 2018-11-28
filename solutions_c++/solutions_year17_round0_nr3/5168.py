#include <stdio.h>
#include <string>
#include <iostream>
#include <set>
#include <algorithm>
#include <utility>


using namespace std;


int main()
{
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  //string s;
  int k, n;
  for (int cntt = 1; cntt <= t; cntt++) 
  {
    cin >> n >> k;
    set<pair<int, int>> S;
    S.clear();
    S.insert(make_pair(n, 0));
    int ans1, ans2;
    for (int i = 0; i < k; i++)
    {
      int l = S.size();
      pair<int, int> cur = *prev(S.end()); 
      ans1 = (cur.first-1)/2;
      ans2 = cur.first-1-ans1;
      S.erase(prev(S.end()));
      S.insert(make_pair(ans1, cur.second));
      S.insert(make_pair(ans2, -(-cur.second+ans1+1)));
   }

    
    cout << "Case #" << cntt << ": " << ans2 << " " << ans1 << endl;
 
    
  }  
  return 0;
}
