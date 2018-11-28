#include <iostream>
#include<string.h>
using namespace std;

int main() {
	int o=0,k,r=0,f=0;
	cin>>o;
	for(int i=0;i<o;i++)
	{
	    r=0;f=0;
	    char s[1000];
	   cin>>s;   
	   cin>>k;
	   for(int j=0;j<(strlen(s)-k+1);j++)
	   {
	       if(s[j]=='-')
	       {
	           for(int t=j;t<(k+j);t++)
	           {
	               if(s[t]=='-')
	               s[t]='+';
	               else
	               s[t]='-';
	           }
	           r++;
	           
	       }
	   }
	   for(int p=0;p<strlen(s);p++)
	   {
	       if(s[p]=='-'){ r=0;f=1;break;}
	   }
	   if(r==0&&f==1)
	   cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
	   else 
	   cout<<"Case #"<<(i+1)<<": "<<r<<endl;
	   
	}
	
	
	return 0;
}
