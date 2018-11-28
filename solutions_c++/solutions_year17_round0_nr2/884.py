#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
  int tc;
  cin >> tc;
  for (int tt=1; tt<=tc; tt++)
  {
    string str;
    cin >> str ;
    int idx=-1, inc_flg=1;
    for (int i=0; i<str.size()-1; i++)
      if (str[i] > str[i+1])
      {
        inc_flg=0;
        idx = i;
        break;
      }
    cout << "Case #" << tt << ": ";
    if (inc_flg)
      cout << str << endl;
    else
    {
      if (str[0] == str[idx])
      {
        str[0] -= 1;
        for (int i=1; i<str.size(); i++)
          str[i] = '9';
      }
      else
      {
        for (int i=idx; i>0; i--)
          if (str[i-1] != str[idx])
          {
            str[i] -= 1;
            for (int j=i+1;j<str.size(); j++)
              str[j] = '9';
            break;
          }
      }
      while (str[0] == '0')
        str = str.substr(1);
      cout << str << endl;
    }
  }
}
