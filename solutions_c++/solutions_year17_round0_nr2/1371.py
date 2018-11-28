#include<bits/stdc++.h>
#define	    ll		    long long int
#define     D               double
#define     LD              long double
#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))
#define     mp              make_pair
#define     vi              vector<ll>
#define     pb              push_back
#define     s               second
#define     f               first
#define     mod             1000000007
using namespace std;
inline ll getn(){
	ll n=0, c=getchar();
	while(c < '0' || c > '9')
		c = getchar();
	while(c >= '0' && c <= '9')
		n = (n<<3) + (n<<1) + c - '0', c = getchar();
	return n;
}


int main()
{
	//	std::ios_base::sync_with_stdio(0);
	ll t,n,j,i,p,k,l,ji;
	FILE *wfile;
	
	cin>>t;
//	string str,str1;
	wfile=fopen("output1.txt","w");
	ji=0;
	string str,str1;
	ll dp[1005];
	ll arr[1005];
while(t--)
{
	ji++;
	cin>>str;
	ll ans=0;
	n=str.size();
	memset(dp,0,sizeof(dp));
	memset(arr,0,sizeof(arr));
	for(i=n-2;i>=0;i--)
	{
		if(str[i]>str[i+1])
		{
			for(j=i+1;j<n;j++)
				str[j]='9';
			str[i]=char(str[i]-1);
			
		}
	}




	fprintf(wfile,"Case #%lld: ",ji);
	for(i=0;i<n;i++)
		if(str[i]!='0')
			break;
		for(j=i;j<n;j++)
fprintf(wfile,"%c",str[j]);
	fprintf(wfile,"\n");
}
	
	return 0;
}
