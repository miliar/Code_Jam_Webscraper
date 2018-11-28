#include <bits/stdc++.h>
using namespace std;


void corr(char* s, int index)
{
	if(index!=0)
	{
	for(int i=0;i<index; i++)
	{
       if(s[i]>s[i+1])
       {
       	s[i]--;

       		
       	for(int j=i+1; j<=index; j++)
       		s[j]='9';
          if(i!=0 && s[i]<s[i-1])
           corr(s,i);
       }
	}
  }
  else
  	return;
}


int main()
{
	int t;
	cin>>t;

	for(int i=1; i<=t; i++)
	{
        char s[4];
        cin>>s;

        int len=0;
        for(int j=0; s[j]!='\0'; j++)
        	len++;
        
        
      corr(s,len-1);
      int flag=0;
      
      if(s[0]=='0')
      	flag=1;
      cout<<"CASE #"<<i<<": ";
      
      for(int j=flag; j<len; j++)
        	{
                
  
        		cout<<s[j];
        	}
        	cout<<endl;

	}
}