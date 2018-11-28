#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;
int t,i,d,n,rels,a,b,reld;
pair<int,int> dat[1100];
double ans=0,t1,t2,t3,dis;
int main()
{
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>d>>n;
		for(int j=0;j<n;j++)
		{
			cin>>a>>b;
			dat[j].f=a,dat[j].s=b;
		}
		sort(dat,dat+n);
		ans=((double)d-(double)dat[n-1].f)/(double)dat[n-1].s;
		//cout<<"first "<<ans<<endl;
		for(int j=n-2;j>=0;j--)
		{
			t2=((double)d-(double)dat[j].f)/(double)dat[j].s;
			if(dat[j].s<dat[j+1].s)
			{
				ans=t2;
			}
			else
			{
			rels=dat[j].s-dat[j+1].s;
			reld=abs(dat[j].f-dat[j+1].f);
			//cout<<"rels "<<rels<<" "<<"reld "<<reld<<endl;
			t1=(double)reld/(double)rels;
			
		//	cout<<"t1 "<<t1<<" t2 "<<t2<<endl; 
			if(t1>t2)
			{
				ans=t2;
			}
			else
			{
				dis=(double)dat[j].s*(double)t1;
				dis+=dat[j].f;
				//cout<<"dis"<<dis<<endl;
				t3=((double)d-(double)dis)/(double)dat[j+1].s;
			//	cout<<"t3= "<<t3<<endl;
				ans=t1+t3;
				//cout<<"ans= "<<ans<<endl;
			}
			}
		}
		ans=(double)d/(double)ans;
		printf("Case #%d: %.9f\n",i,ans);
	}
	return 0;
}
