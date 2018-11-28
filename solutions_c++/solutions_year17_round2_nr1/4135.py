#include <bits/stdc++.h>
#define lli long long int
#define pb push_back
#define mp make_pair
#define cases int tcases;cin>>tcases;while(tcases--)
using namespace std;

int main()
{ lli dist,sped;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	lli loop,t,i,j,d,n,k[1001],s[1001];
	scanf("%lld",&t);
	for(loop=1;loop<=t;loop++)
	{
	    scanf("%lld",&d);
	    scanf("%lld",&n);
	  double time;
	  double maxt=0;
	  for(i=0;i<n;i++)
	  {
	    scanf("%lld",&k[i]);
	    scanf("%lld",&s[i]);
	  }
	  for(i=n-1;i>=0;i--)
	  {
	    dist=d-k[i];
		sped=s[i];
		time=(1.0*dist)/((double)(sped));
		maxt=max(maxt,time);
	  }
	  time=maxt;
	  double speed=(1.0*d)/time;
	  
	  printf("Case #%lld: %.6f\n",loop,speed);
	}
return 0;
}