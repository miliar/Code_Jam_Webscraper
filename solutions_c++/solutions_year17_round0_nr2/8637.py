#include<bits/stdc++.h>
using namespace std;
bool tidy(int n)
{   bool flag=true;
int last_d=12,new_d;
while(n!=0)
{ new_d=n%10;n=n/10;
if(new_d>last_d)
{flag=false;break;}
last_d=new_d;
}
			 return(flag);
}
int main()
{  freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
  int t,p=1;
  cin>>t;
  while(t--)
  {  int n,number;
  cin>>n;
		 for(int i=n;i>=1;i--)
		 {if(tidy(i))
		 {    number=i;
		 break;}
		 }
		   cout<<"Case #"<<p<<": "<<number<<endl;

	p++;}
return 0;
}
