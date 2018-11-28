#include<bits/stdc++.h>
#define	    ll		    long long int
using namespace std;
ll dp[55][55];
ll ppp[55][1005];
ll arr[55];
#define mod 10000000000005
int main()
{
	ll t,nn,i,j,temp,temp1,l,r,val,val1,x,y,b,ji,n,m,p,x1,y1;
	FILE *wfile;
	
cin>>t;
nn=t;
	wfile=fopen("output1.txt","w");
	ji=0;
	
while(t--)
{
	ji++;
	fprintf(wfile,"Case #%lld: ",ji);
	//memset(ppp,0,sizeof(ppp));
	cin>>n>>m;
	double dl=10000000000000000.0;
	for(i=0;i<m;i++)
	{
		cin>>l>>r;
		dl=min(dl,(double(double(n*r)/double(n-l))));
	}

	fprintf(wfile,"%.6lf",dl);
	fprintf(wfile,"\n");
}
	
	return 0;
}
