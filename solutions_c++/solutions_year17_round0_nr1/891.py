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
    int k;
    cin >> str >> k;
    int cnt=0;
    for (int i=0; i<str.size()+1-k; i++)
    {
      if (str[i] == '-')
      {
        cnt++;
        for (int j=0; j<k; j++)
          str[i+j] = (str[i+j] == '+'? '-':'+');
      }
    }
    int flag = 0;
    for (int i=0; i<str.size(); i++)
      if (str[i] == '-')
        flag = 1;
    printf("Case #%d: ", tt);
    if (flag)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", cnt);

  }
}
