#include <bits/stdc++.h>
using namespace std;

string str;
int l;

int decpoint()
{
  for(int i=0;i<l-1;i++) if(str[i+1]<str[i]) return i;
  return -1;
}

int main()
{
  int t;
  cin >> t;
  for(int cas=1;cas<=t;cas++)
  {
    cin >> str;
    l=str.length();
    int d=decpoint();
    if(d == -1) cout << "Case #" << cas << ": " << str << endl;
    else
    {
      while(d)
      {
        if(str[d-1] != str[d]) break;
        d--;
      }
      int a=str[d]-'0';
      a--;
      str[d]=(a+'0');
      for(int i=d+1;i<l;i++) str[i]='9';
      while(str[0]=='0') str.erase(str.begin()+0);
      cout << "Case #" << cas << ": " << str << endl;
    }
  }
  return 0;
}
