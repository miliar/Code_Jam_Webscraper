#include <bits/stdc++.h>

using namespace std;

int main ()
{
  int t;
  cin>>t;
  for (int a = 1 ; a <= t ; a++)
  {
    string s;
    cin>>s;
    int tam = s.size();
    for (int i = tam-1; i > 0 ; i--)
    {
      if(s[i]<s[i-1])
      {
        if (s[i-1]>'0')
          s[i-1]--;
        else
          s[i-1]='0';
        for (int j = i ; j < tam ; j++)
        {
          s[j]='9';
        }
      }
    }
    stringstream ss(s);
    long long resp;
    ss>>resp;
    cout<<"Case #"<<a<<": "<<resp<<endl;
  }
  return 0;
}

