#include <bits/stdc++.h>
 using namespace std;

#define ll long long int
#define pb push_back 
#define mp make_pair
#define ff first
#define ss second


int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
   ll n,b,i,j,k,z,x=0,y=0,p,q,l,T,m,ans=0;
    double xx,yy;   
   bool f;
   cin>>T;
   string s;
   for(int t = 1; t <= T; t++)
   {
   	ans = 0;
   	cin>>s>>k;
   	l = s.length();
    f = true;
   	for( i = 0 ;i < l; i++)
   	{
      if( s[i] == '-' && (i + k <= l))
      { ans++;
         //cout<<i<<endl;
      	for( j = i; j < min( i + k, l); j++)
      	{
          if(s[j] == '-')
          	s[j] = '+';
          else
          	s[j] = '-';
      	}
      }

   	}

   	for(i = 0; i < l; i++)
   	{
   		if(s[i] == '-')
   		{
   			f = false;
   			break;
   		}
   	}

   	if(f)
   		cout<<"Case #"<< t <<": "<< ans<<"\n";
   	else
   		cout<<"Case #"<< t <<": IMPOSSIBLE"<<"\n";

   }





 return 0;
}