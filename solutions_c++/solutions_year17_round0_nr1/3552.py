#include<bits/stdc++.h>
using namespace std;
#define for1(i,n) for(int i=0;i<(n);i++)
#define for2(j,a,b) for(j=a;j<=b;j++)
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ll long long

#define endl "\n"
int main()
{
freopen("input1.txt","r",stdin);
freopen("output1.txt","w",stdout);
int t,x,y,i,m,k,a[1005],j;
string s;
cin>>t;
for(x=1;x<=t;x++)
{
cin>>s>>k;
int l=s.length();
int n=l;
j=1;
for(i=0;i<l;i++)
	{
		if(s[i]=='+')
	a[j++]=1;
else
	a[j++]=0;
    }
 int ans=0;
    for(i=1;i<=n-k+1;i++)
    {
    	if(a[i]==1)
    		continue;
    

    ans++;
    	for(j=i;j<=i+k-1;j++)
    		a[j]=1-a[j];
    }
    int ct=0;
    for(i=1;i<=n;i++)
    	if(a[i]==1)
    		ct++;
cout<<"Case #"<<x<<": ";
    	if(ct==n)
    		cout<<ans<<endl;
    	else
    		cout<<"IMPOSSIBLE"<<endl;





}


return 0;
}
