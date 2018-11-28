#include<bits/stdc++.h>
using namespace std;
int main()
{
		freopen("A-large.in","r",stdin);
	freopen("big.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		/*long long int n,d;
		cin>>d>>n;
		int a[n][2];
		float ans=0;
		int x,y;
		
		for(int i=0;i<n;i++)
		{
			cin>>x>>y;
			if(ans<float((float(d-x)/y)))
			ans=float((float(d-x)/y));
		}
		 //std::cout << std::fixed;
    //td::cout << std::setprecision(6);
	//cout<<float(d/ans)<<"\n";
	float ans1=float(d/ans);
	printf("Case #%d: %.7f\n",t,(d/ans));*/
	
//	p++;

int n,k;
cin>>n>>k;
float min1=0;
float d;
for(int i=0;i<k;i++)
{
int p,q;
cin>>p>>q;
d=(n-p)/(float)q;
min1=max(min1,d);
//cout<<min1<<endl;
}
d=n/min1;
//cout<<"Case #"<<p<<":"<<" ";
//printf("%.7f",d);
//cout<<endl;
printf("Case #%d: %.7f\n",t,d);
	}
}

