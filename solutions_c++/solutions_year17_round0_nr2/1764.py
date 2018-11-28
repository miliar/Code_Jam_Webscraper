#include <iostream>
#include <string>

using namespace std;
int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    string s; cin >> s;
    int l = s.length();
    for (int i = 1; i < l; i++)
    {
      if (s[i-1] > s[i])
      {
        for (int j = i; j >= 0; j--)
        {
          if (j == 0 || s[j-1] < s[j])
          {
            s[j] --;
            for (int k = j+1; k < l; k++) 
            {
              s[k] = '9'; 
            }
            break;
          }
        }
        break;
      }
    }
    cout << "Case #" << ii << ": ";
    if (s[0] == '0')
    {
      cout << s.substr(1) << endl;
    }
    else   
    {
      cout << s << endl;
    }
  }
  return 0;
}