/*
    
    Jaydeep Khandelwal,
    CSE 3rd year,
    MNNIT Allahabad
    
    Kathumar, Alwar, Rajsthan.
    
*/
//For taking input line with spaces: getline(cin,s[i]);


#include<bits/stdc++.h>
using namespace std;

//Constants:
#define mod 1000000007
#define INF 1000000000
#define INFL 1000000000000000000
#define N 100005
#define PI (2.0*acos(0.0))

//Shortcuts:
#define ll long long
#define vec vector<ll>
#define matrix vector<vector<ll> >
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sn struct node
#define sf1(a) scanf("%lld",&a);
#define sf2(a,b) scanf("%lld%lld",&a,&b);
#define sf3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c);
#define pf1(a) printf("%lld\n",a);
#define pf2(a,b) printf("%lld %lld\n",a,b);
#define pf3(a,b,c) printf("%lld %lld %lld\n",a,b,c);
#define ffor(a,b) for(i=a;i<=b;i++)
#define rfor(a,b) for(i=a;i>=b;i--)

//Mistakes:
#define pritnf printf

ll StringToNumber (string str)
{
	stringstream sstr(str);
	ll val;
	sstr >> val;
	return val;
}

struct node{
	ll p,q;
}a[N];

bool comp(sn x,sn y)
{
	if(x.p!=y.p)
		return x.p > y.p;

	return x.q > y.q;

}


int main()
{
	ll t,i=0,j,k,x,y,z,count=0,flag=0,sum=0,l,n,m,max1,min1,pos,tmp,t1,d;
	
	//string s;
	
	scanf("%lld",&t);
	t1=t;
	
	while(t--)
	{
	    
	    scanf("%lld%lld",&d,&n);

	    for(i=0;i<n;i++)
	    {
	    	scanf("%lld%lld",&a[i].p,&a[i].q);


	    }

	    sort(a,a+n,comp);


	    double ans=1.0*(d-a[0].p)/a[0].q;

	    ans=max(ans,1.0*(d-a[n-1].p)/a[n-1].q);

	    ans=1.0*d/ans;

		printf("Case #%lld: %lf\n",t1-t,ans);
		
	}
	
	
	return 0;
}
