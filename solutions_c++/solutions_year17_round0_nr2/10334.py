#include<bits/stdc++.h>
#define sd(mark) scanf("%d",&mark)
#define slld(mark) scanf("%lld",&mark)
#define ss(mark) scanf("%s",mark)
#define pd(mark) printf("%d",mark)
#define plld(mark) printf("%lld",mark)
#define pdd(mark1,mark2) printf("%d %d",mark1,mark2)
#define pn() printf("\n")
#define ps(mark) printf("%s",#mark)
#define debugd(val) printf("%s : %d\n",#val,val)
#define debuglld(val) printf("%s : %lld\n",#val,val)
#define ford(itr,start,end) for(int itr=start;itr<end;itr++)
#define fsd(mark) fscanf(in,"%d",&mark)
#define fslld(mark) fscanf(in,"%lld",&mark)
using namespace std;
typedef long long ll;
FILE *in = fopen("new","r");
FILE *out = fopen("output","w");
bool verify(ll n)
{
	ll a,b;
	while(n)
	{
		a=n%10;
		n/=10;
		b=n%10;
		if(a<b)
			return 0;
	}
	return 1;
}

int main(){
	
	int t;
	sd(t);
	ford(j,0,t)
	{
		ll n;
		cin >> n;
		while(!verify(n--))
			;
		 fprintf(out,"case #%d: %lld\n",j+1,n+1);		
	}
    return 0;
}

