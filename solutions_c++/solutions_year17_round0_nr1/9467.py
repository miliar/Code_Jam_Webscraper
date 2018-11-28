#include <bits/stdc++.h>
using namespace std;
int main()
{
     int t;
     cin>>t;
     int p=1;
     while(t--)
     {
	  char s[1005];
	  scanf("%s",s);
	  int x;
	  cin>>x;
	  int i,j;
	  int l=strlen(s);
	  int count=0,y=0;
	  for(i=0;i<=l-x;i++)
	  {
	       if(s[i]=='-')
	       {
		    y++;
		    s[i]='+';
		    int j;
		    for(j=1;j<x;j++)
		    {
			 if(s[i+j]=='+')
			      s[i+j]='-';
			 else
			      s[i+j]='+';
		    }
	       }
	  }
	  for(i=0;s[i]!='\0';i++)
	  {
	       if(s[i]=='+')
		    count++;
	  }
	  if(count==l)
	       printf("Case #%d: %d\n",p,y);
	  else
	       printf("Case #%d: IMPOSSIBLE\n",p);
	  p++;
     }
     return 0;
}
