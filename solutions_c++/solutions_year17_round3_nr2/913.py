#include<bits/stdc++.h>
#define X first
#define Y second
#define mp make_pair
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B_small.txt","w",stdout);
	int a,Ac,Aj,T,b;
	pair<int,int> m[5],n[5];
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>T;
	for(a=0;a<T;a++)
	{
		cin>>Ac>>Aj;
		for(b=0;b<Ac;b++)
		{
			cin>>m[b].X>>m[b].Y;
		}
		for(b=0;b<Aj;b++)
		{
			cin>>n[b].X>>n[b].Y;
		}
		cout<<"Case #"<<a+1<<": ";
		if(Ac<2&&Aj<2)cout<<"2\n";
		else
		{
			if(Ac==2)
			{
				if(m[0].X>m[1].X)swap(m[0],m[1]);
				if((m[1].Y-m[0].X<=720)||(m[1].X-m[0].Y>=720))cout<<"2\n";
				else cout<<"4\n";
			}
			else
			{
				if(n[0].X>n[1].X)swap(n[0],n[1]);
				if((n[1].Y-n[0].X<=720)||(n[1].X-n[0].Y>=720))cout<<"2\n";
				else cout<<"4\n";
			}
		}
	}
}
