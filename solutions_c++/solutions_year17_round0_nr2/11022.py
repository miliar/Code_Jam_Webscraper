// Example program
#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <conio.h>
using namespace std;
int main()
{
  freopen("sampleinput0.txt","rt",stdin);
  freopen("bheem0.out","wt",stdout);
  int t;
  cin >> t;
  for(int i = 1; i<=t;i++)
  {
      long long n;
      cin >> n;
      string s = to_string(n);
      for(int i = 0; i+1< s.size();)
      {
          if(s[i+1] < s[i])
          {
              n--;
              s = to_string(n);
              i=0;
          }
          else
          i++;
      }
      cout << "Case #"<<i<<":"<<" "<<n << endl;
  }      
  getche();
  return 0;
}

