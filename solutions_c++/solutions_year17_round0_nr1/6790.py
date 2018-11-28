#include <bits/stdc++.h>
using namespace std;

int main()
{
   freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);

	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
      string s;
      cin>>s;
      int n,count=0,flag=0;
      cin>>n;


      		for(int i=0;i<=(s.length()-n);i++)
           {
      	     if(s[i]=='-')
      	    {
      		  for(int j=i;j<(i+n);j++)
      		  {
      			if(s[j]=='+')
                    s[j]='-';

                else if(s[j]=='-')
                    s[j]='+';

      		  }
      		  count++;
      		  i=-1;

      	    }

          }
          for(int i=0;i<s.length();i++)
          {
              if(s[i]=='-')
                flag=1;
          }




            if(flag)
            	{cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<"\n";}
            else
              {cout<<"Case #"<<k<<": "<<count<<"\n";}

	}//end test
	return 0;
}//end main
