#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long int
#define M(x) M(x%MOD + MOD)
#define _pb push_back
#define ff first
#define ss second
#define _mp make_pair
#define sc(x) scanf("%lld",&x)

ll mul(ll x,ll y)
{ ll ans=1;
  while(y>0)
  { if(y&1)
	ans=(ans*x)%MOD;

	x=(x*x)%MOD;
	y/=2;
  }
  return ans;
}

//........................................................................................................................................................


int main()
{ freopen("B-large.in","r",stdin);
  freopen("out4.txt","w",stdout);

  ll t,c;
  cin>>t;

  for(c=1;c<=t;c++)
  {  string str;
	 cin>>str;
	 ll in,j,l=str.size(),i;
	 char ch;

	 for(i=1;i<l;i++)
	 if(str[i-1]>str[i])
	 { ch=str[i-1];

	   for(j=i-1;j>=0;j--)
	   if(str[j]==ch)
	   in=j;
	   else
	   break;

	   --str[in];

	   for(j=in+1;j<l;j++)
	   str[j]='9';

	   break;
	 }


     cout<<"Case #"<<c<<": ";

     ll flag=0;
     for(i=0;i<l;i++)
     if(str[i]!='0' && flag==0)
     {
     	cout<<str[i];
     	flag=1;
	 }
	 else if(flag==1)
	 cout<<str[i];

	 cout<<"\n";
  }

   return 0;
}
