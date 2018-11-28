#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
    
	freopen("output.txt","w",stdout);
	int t,p=1;
	cin>>t;
	while(t--)
	{   int n=0,f=1,k;
		string s;
		cin>>s>>k;
		int l=s.length();
		for(int i=0;i<s.length();i++)
		 {
		 	if(s[i]=='-')
		 	 { n++;
			  if(i+k<=l)
		 	  {
			   for(int j=i;j<i+k;j++)
			   { if(s[j]=='+')
			       s[j]='-';
				 else
				   s[j]='+';  
			   }
			  }	
			  else
			  { f=0;
			  	break;
			  }
			 }
		 }
		 for(int i=0;i<s.length();i++)
		 {
		 	if(s[i]=='+');
		 	else
		 	{   f=0;
		 		break;
			 }
		 }
		if(f==1) 
			printf("Case #%d: %d\n",p,n);
	    else
		    printf("Case #%d: IMPOSSIBLE\n",p);	
			p++;	
	}
}
