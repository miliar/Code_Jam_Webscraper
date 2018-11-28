#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//allenite
int main()
{ 
	freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
  int i,j,k,n,m,count=0,count1=0,t=1,sa1,koi,lkoij=0;
  string s,s1;
  cin>>m;
  while(m)
  {cin>>s;
   cin>>n;
   count=0;//aashish singh
   int sder;
   count1=0;
   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='+')
     count++;
     else
     count1++;
   }
   int nbh=0;
   if(count==s.length())
   { cout<<"Case #"<<t<<": "<<0<<endl;
     goto hhh;
   }
   count=0;
   //int asdert1=9;

   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='-'&&s.length()-i>=n)
    { for(j=i;j<i+n;j++)
       { if(s[j]=='+')//cout<<
         s[j]='-';
         else
         s[j]='+';
	   }
	   //cout<<count;
	  count++;
	}
   }
   for(i=0;s[i]!='\0';i++)
   { if(s[i]=='-')
     { cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
      goto hhh;
	 }
   }
   //long long int asderw=19;
   //cout<<count;
   cout<<"Case #"<<t<<": "<<count<<endl;
   hhh:
   m--;
   long long int zzz1;
   t++;
  }
}
