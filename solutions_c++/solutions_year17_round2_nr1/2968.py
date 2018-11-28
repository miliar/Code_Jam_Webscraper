#include<bits/stdc++.h>

using namespace std;



int main()
{
		freopen("inul.in","r",stdin);
		freopen("oupu.txt","w",stdout);
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t;
	cin>>t;
	int p=1;
	while(p<=t)
	{
		double des,hor,m=-1,ti;
		cin>>des>>hor;
		for(int i=0;i<hor;i++)
		{
			double po,sp;
			cin>>po>>sp;
			ti=des-po;
			ti/=sp;
			if(m<ti)
			{
				m=ti;
			}
		}
		double ans=des/m;
		printf("case #%d: %.6f\n",p,ans);
		p++;
	}
}
