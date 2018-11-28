#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
int cn=1;
while(t--)
{
string s;
int i,j,k,u=0;
cin>>s>>k;
for(i=0;i+k<= s.size();i++)
 {
    if(s[i] =='-' )
    	{   u++; 
    		for(j=i;j<=i+k-1;j++)
               {
                  if(s[j]=='-')
                  	 s[j]='+';
                  else
                      s[j]='-';	
               }
        }
}
   int flag=1;
   for(i=0;i<s.size();i++)
   	  if(s[i]=='-')
   	  	 {  flag=0; break; }
   if(flag==0)
     cout<<"Case #"<<cn<<": "<<"IMPOSSIBLE"<<endl;
   else
       cout<<"Case #"<<cn<<": "<<u<<endl;  	  	

 cn++;
}	
 return 0;
}