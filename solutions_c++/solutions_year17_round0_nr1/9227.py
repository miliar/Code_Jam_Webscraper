#include<string.h>
#include <iostream> 
using namespace std;  
int main() 
{
  int flag,i,t, n, m;
  string s;	
int at[100000];
int K=0,k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int j= 1; j <= t; ++j) {
K=0;
flag=0;
  cin >> s >> m;  // read n and then mdc

    for(i=0;i<s.length()-m+1;i++)
{
if(s[i]=='-')
{k=m-1;
while(k)
{
if(s[i+k]=='-')
s[i+k]='+';
else
s[i+k]='-';
k--;
}
s[i]='+';
K=K+1;
}}
for(i=0;i<s.length();i++)
{
if(s[i]=='-'){
flag=1;
break;
}}
if(flag==0)
    cout << "Case #" << j << ": " << K  << endl;
else
   cout << "Case #" << j << ": " << "IMPOSSIBLE"<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
}
return 0;  

}