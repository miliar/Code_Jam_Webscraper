#include <iostream>
#include <string>
using namespace std;
void flip(string &s, int i, int k)
{
  for(int j = i; j < k+i; j++)
  {
    if(s[j] == '-') s[j] = '+';
    else s[j] = '-';
  }
}
int number(string s,int k)
{
  int l = s.length(), count = 0;
  for(int  i = 0; s[i] != '\0';i++)
  {
    if(s[i] == '-')
    {
      if(l-i < k)
      {
        return -1;
      }
      count++;
      flip(s,i,k);
    }
  }
  return count;
}
int main()
{
  int t;
  cin>>t;
  string s;
  int k;
  for(int a0 = 1; a0 <= t; a0++)
  {
    cin>>s>>k;
    if(number(s,k)==-1)
      cout<<"Case #"<<a0<<": IMPOSSIBLE\n";
    else
      cout<<"Case #"<<a0<<": "<<number(s,k)<<"\n";

  }
}
