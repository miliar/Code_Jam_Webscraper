#include <iostream>
#include <stdio.h>

using namespace std;


void change_sign(int i, int k, string &s)
{
   for (int j = i; j < i+k; j++)
     s[j] = s[j] == '-' ? '+' : '-';
}

bool finished(string &s)
{
  for(int i = 0; i < s.length(); i++)
    if(s[i] == '-')
        return false;
  return true;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("ou.txt", "w", stdout);

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        string s;
        int k;
        int answ = 0;

        cin>>s;
        cin>>k;

        for (int j = 0; j <= s.length() - k; j++)
        {
          if (s[j] == '-')
          {
            change_sign(j, k, s);
            answ++;
          }
        }

        if (finished(s))
        {
          cout<<"Case #"<< tt <<": "<<answ<<endl;
        }
        else
        {
          cout<<"Case #"<< tt <<": "<<"IMPOSSIBLE"<<endl;
        }
    }

    return 0;
}

