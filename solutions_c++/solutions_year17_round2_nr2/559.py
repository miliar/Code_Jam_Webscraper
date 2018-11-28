#include<iostream>
#include<vector>
using namespace std;

int col[10];
char c[] = {'R' , 'O' , 'Y' , 'H' , 'B' , 'V'};
int main()
{
  int T;
  cin >> T;
  for(int t = 0;t < T;t ++)
  {
    int n;
    cin >> n;
    //cin >> r >> o >> y >> g >> b >> v;

    for(int p = 0;p < 6;p ++)
      cin >> col[p];

    int mx = 0;
    for(int p = 0;p < 6;p ++)
      if(col[mx] < col[p]) mx = p;

    int ot1 = -1 , ot2 = -1;
    for(int p = 0;p < 6;p ++)
      if(col[p] != 0 && mx != p)
      {
        if(ot1 != -1)
          ot2 = p;
        else
          ot1 = p;
      }
    if(ot2 == -1) ot2 = ot1;

    vector<char> ans;
    bool imp = false;
    while((int)ans.size() < n)
    {
      if(imp)
        break;
      if(col[mx] > 0)
      {
        ans.push_back(c[mx]);
        col[mx] --;

        if(ans.size() == n)
          break;

        if(col[ot1] > col[ot2] && col[ot1] > 0)
          ans.push_back(c[ot1]) , col[ot1] --;
        else if(col[ot2] > 0)
          ans.push_back(c[ot2]), col[ot2] --;

        continue;
      }
      if((int)ans.back() == c[ot1])
      {
        if(col[ot2] == 0)
          imp = true;
        else
          ans.push_back(c[ot2]) , col[ot2]--;
      }
      else
      {
        if(col[ot1] == 0)
          imp = true;
        else
          ans.push_back(c[ot1]) , col[ot1]--;
      }
    }


    imp |= (ans.size() != n) || (ans.back() == ans[0]);

    cout << "Case #" << t + 1 << ": ";
    if(imp)
      cout << "IMPOSSIBLE" << endl;
    else
    {
      for(int i = 0;i < n;i ++)
        cout << ans[i];
      cout << endl;
    }
  }
  return 0;
}
