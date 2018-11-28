#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(string st, ll data)
{
  string nuevo=st;
  int i;
  for( i = 1 ; i < st.size() ; ++i)
    if(st[i-1] > st[i])
      break;
  i--;
  int j = i-1;
  for(int l = i+1 ; l < st.size() ; ++l)
    nuevo[l] = '9';
  char who= nuevo[i];
  nuevo[i] = '9';
  while(i-1 >= 0 and st[i-1] == st[i])
    {
      nuevo[i-1] = nuevo[i];
      --i;
    }
  nuevo[i] = char(who-1);
  ll num = stoll(nuevo);
  cout << num << "\n";

  // (st[i] == '1')
  //   {
  //     for(int j = 0 ; j < st.size()-1 ; ++j)
  //       nuevo += '9';
  //     ll imp = stoll(nuevo);
  //     cout << imp << "\n";
  //     return ;
  //   }
  // cout << "jeje\n";
  // cout << st[i] <<"\n";
  // for(int j =  0 ; j < i ; ++j)
  //   cout << st[j];
  // cout << char(st[i]-1);
  // for(int j =  i+1 ; j < st.size() ; ++j)
  //   cout << 9;
  // cout << "\n";
}

int main()
{
  ll data;
  int t; cin >> t;
  for(int i = 0;i < t ; ++i)
    {
      cin >> data;
      int j;
      string st = to_string(data);
      for(j = 1;j < st.size() ; ++j)
        if(st[j-1] > st[j])
          break;
      cout << "Case #" << i+1 << ": ";
      if(j == st.size() or data < 10)
        {
          cout << data << "\n";
        }
      else solve(st,data);
    }
  return 0;
}
