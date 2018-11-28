#include<bits/stdc++.h>

using namespace std;
int n,a[100],b[100];
string s;
int cnt=0;
void input()
{
  cin>>s;
  n=s.size();
  for(int i=1;i<=n;i++)
    a[i]=s[i-1]-'0';
}
void show()
{
  cout<<"Case #"<<cnt<<": ";
  int i=1;
  while(b[i]<=0 && i<=n)
    i++;
  
    for(;i<=n;i++)
      cout<<b[i];
    cout<<endl;
}
void delet()
{
  fill(a,a+40,0);
  fill(b,b+40,0);
}
int main()
{
  int T;
  cin>>T;
  while(T--)
  {
    cnt++;
  input();
  b[1]=a[1];
  for(int i=2;i<=n;i++)
    if(a[i]>=b[i-1])
      b[i]=a[i];
    else
      {
	b[i]=9;
	for(int j=i;j<=n;j++)
	  b[j]=9;
	
	b[i-1]--;
	for(int j=i-2;j>=1;j--)
	  if(b[j]<=b[j+1])
	    break;
	  else{
	    b[j]--;
	    b[j+1]=9;}
	break;
      }
  show();
  delet();
  }
  return 0;
}
