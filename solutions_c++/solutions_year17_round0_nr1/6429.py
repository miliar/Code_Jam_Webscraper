#include<bits/stdc++.h>
using namespace std;
/*author : jatin_jt_narula
           B.tech CSE  
           MNNIT-Allahabad */
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define sf(x) scanf("%lf",&x)
#define sl(x) scanf("%lld",&x)
#define pl(x) printf("%lld",x)
#define pln(x) printf("%lld\n",x)
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define wh(t) while(t--)
#define ms(a , value) memset(a , value , sizeof(a))
#define f(c,itr) for(itr=(c).begin();itr!=(c).end();itr++)
#define sc scanf
#define pr printf
#define pi(x) printf("%d",x)
#define pin(x) printf("%d\n",x)
#define ss(x) scanf("%s",x)
#define ps(x) printf("%s",x)
#define nl() printf("\n")
#define psn(x) printf("%s\n",x)
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define si2(x,y) scanf("%d%d",&x,&y)
#define each(v) v.begin(),v.end()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
const double PI=3.1415926535897;
typedef long long int ll;
int solve(int *arr, int n, int k) {
  int tmp[n];
  int sum=0, ans=0;
  for(int i=0;i<n;i++) 
  	tmp[i]=0;
  for(int i=0;i<n;i++) 
  {
    tmp[i]=(arr[i]+sum)%2!=1;
    sum+=tmp[i]-(i>=k-1?tmp[i-k+1]:0);
    ans+=tmp[i];
    if(i>n-k && tmp[i]!=0) 
    	return -1;
  }
  return ans;
}
int main()
{
	int test;
	int arr[100007];
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		string str;
		int k;
		cin>>str>>k;
		int len = str.length();
		for(int i=0;i<len;i++)
		{
			if(str[i] == '-')
				arr[i]=0;
			else
				arr[i]=1;
		}
		int ans=solve(arr,len,k);
		if(ans == -1)
			pr("Case #%d: IMPOSSIBLE\n",t);
		else
			pr("Case #%d: %d\n",t,ans);
	}
	return 0;
}