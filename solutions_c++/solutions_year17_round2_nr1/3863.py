#include<bits/stdc++.h>
using namespace std;
#define for1(i,n) for(int i=0;i<(n);i++)
#define for2(j,a,b) for(int j=a;j<=b;j++)
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ll long long

#define endl "\n"
int main()
{
//ios_base::sync_with_stdio(false);
int t,x,y,i,j,m,s,k,n,d;
freopen("input.txt","r",stdin);
freopen("output.out","w",stdout);
//double ans[100005];
cin>>t;
for(int p=1;p<=t;p++)
{
pair<int,int>z[1004];
	cin>>d>>n;

	for1(i,n)
	{cin>>x>>y;
       z[i].F=x;//dist
       z[i].S=y;
	   }

    double dd,t1,t2,d2;
	/*  if(n==2)
	  {
	  	sort(z,z+n);
	  	if(z[0].S>z[1].S)
	  	{
	  		dd= ( z[1].F *(z[0].S-z[1].S) ) / ( z[1].F - z[0].F );
	  		d2=z[0].F+dd;
	  		if(d2<d)
	  		{
	  			t1=dd/z[0].S;
	  			t2=(d-d2) / z[1].S;
	  			z[0].S=(d-z[0].F) / (t1 +t2);
	  		}
	  	}
	  } */
	   double mx=-20.00,zz;
	   for1(i,n)
	   {
	   	zz= (d-z[i].F);
	   	zz= zz/z[i].S;
	   	
	   	if(zz>mx)
	   		mx=zz;
     
	   }
	   //cout<<"mx is "<<" ";
	   //printf("%.9f\n",mx);
	   mx=d/mx;
	   cout<<"Case #"<<p<<": ";
	   printf("%.6f\n",mx);
}

return 0;
}
