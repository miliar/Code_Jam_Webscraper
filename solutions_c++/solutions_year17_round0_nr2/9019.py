#include <iostream>
#include <string>
using namespace std;
void fetchLast(string s,int &i){
    i--;
    while(i>0){
        if(s[i] != s[i-1])
          return;
        else
          i--;
    }
}
long long number(long long n)
{
  string s  = to_string(n);
  int i;
  for(i=1;s[i]!='\0';i++)
  {
      if(s[i]<s[i-1])
      {
          fetchLast(s,i);
          s[i] -= 1;
          break;
      }
  }
  i++;
  while(s[i]!='\0'){
      s[i] = '9';
      i++;
  }
  return stol(s);
}
int main()
{
  int t;
  long long n;
  cin>>t;
  for(int a0 = 1; a0<=t; a0++)
  {
    cin>>n;
    cout<<"Case #"<<a0<<": "<<number(n)<<"\n";

  }
}
