#include<bits/stdc++.h>
using namespace std;
int main()
{ freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
  int i,j,k,n,m,count=0,count1=0,t=1;
  string s,s1;
  cin>>m;
  while(m)
  {cin>>s;
   cin>>n;
   count=0;
   count1=0;
   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='+')
     count++;
     else
     count1++;
   }
   if(count==s.length())
   { cout<<"Case #"<<t<<": "<<0<<endl;
     goto hhh;
   }
   //s1=s;
   count=0;
   //cout<<"hello";
   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='-'&&s.length()-i>=n)
    { for(j=i;j<i+n;j++)
       { if(s[j]=='+')
         s[j]='-';
         else
         s[j]='+';
	   }
	  count++;
	}
   }
   //cout<<s;
   //cout<<"hello";
   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='-')
     { cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
      goto hhh;
	 }
   }
   cout<<"Case #"<<t<<": "<<count<<endl;
   hhh:
   m--;
   t++;
  }
}
