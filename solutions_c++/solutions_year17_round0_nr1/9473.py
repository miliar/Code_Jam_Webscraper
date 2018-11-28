#include <bits/stdc++.h>
using namespace std;
int main()
{freopen("large.txt","r",stdin);
freopen("outputtext.txt","w",stdout);
int t,p=1;
cin>>t;
while(t--)
{char str[10001];
cin>>str;
int l=strlen(str),i,k,c=0,j;
cin>>k;
for(i=0;i<l;i++)
{
if (str[i]=='-')
{c++;
if (i+k>l)
{c=-1;
break;
}
for(j=i;j<i+k;j++)
{if (str[j]=='+')
    str[j]='-';
else
    str[j]='+';
  }
}
}
if (c==-1)
    cout<<"Case #"<<p++<<":  Impossible"<<endl;
else
cout<<"Case #"<<p++<<":  "<<c<<endl;
}
return(0);
}

