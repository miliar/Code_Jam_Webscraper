#include<bits/stdc++.h>
using namespace std;
int tot;
void solve()
{
  tot++;
  string s;
  cin >> s;
  int k;
  cin >> k;
  int count = 0;
  for(int i=0;i<s.length();i++)
  {
    if(s[i] == '-')
    {
      if(i+k-1 <s.length()){
      
        for(int j=i;j<i+k;j++)
        {
          if(s[j] == '-')
            s[j] = '+';
          else
            s[j] = '-';
        }
        count++;
        }
      else{
      
       cout << "Case #" << tot <<": " <<"IMPOSSIBLE" << endl;
       return;
       }
    }
    
  }
  cout << "Case #" << tot <<": " count << endl;
}

int main()
{
  int t;
  tot =0;
  cin >> t;
  while(t--)
    solve();
}
