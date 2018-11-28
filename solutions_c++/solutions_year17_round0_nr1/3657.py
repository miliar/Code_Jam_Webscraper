#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

void solve(int t){
    queue <int> q;
    string s;
    int k;
    cin >> s >> k;
    int dif = 0;
    int ans = 0;
    bool fine = true;
    for (int i = 0; i < s.size(); ++i)
    {
      if( !q.empty() && q.front()==i){
        dif = (dif+1)%2;
        q.pop();
      }
      int val = s[i]=='+'?1:0;
      if (val^dif == 0){
        if (i+k <= s.size()){
          q.push(i+k);
          ans+=1;
          dif = (dif+1)%2;
        }
        else{
          fine = false;
          break;
        }
      }

    }
    if (fine){
      cout << "Case #" << t << ": " << ans << endl;
    }
    else{
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }

}
int main(int argc, char const *argv[])
{
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i)
  {
    solve(i+1);
  }
  return 0;
}


