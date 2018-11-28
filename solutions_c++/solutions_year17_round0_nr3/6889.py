#include <bits/stdc++.h>
using namespace std;
vector<bool> v1;
typedef pair<int,int> ii;
typedef pair<ii,int> iii;
bool gg(iii x,iii y)
{
	int di=max(x.first.first,x.first.second);
	int di2=max(y.first.first,y.first.second);
	int diana=min(x.first.first,x.first.second);
	int diana2=min(y.first.first,y.first.second);
	if(diana==diana2)
	{
		if(di==di2)
		{
			return x.second<y.second;
		}
		else return di>di2;
	}
	else return diana>diana2;
}
ii MM(int izi)
{
	int l,r;
	for(int i=izi-1;i>=0;i--)
	{
		if(v1[i]==1)
		{
			l=izi-i-1;
			break;
		}
	}
	for(int i=izi+1;i<v1.size();i++)
	{
		if(v1[i]==1)
		{
			r=i-izi-1;
			break;
		}
	}
	return ii(min(l,r),max(l,r));

}
iii LR(int izi)
{
	int l,r;
	for(int i=izi-1;i>=0;i--)
	{
		if(v1[i]==1)
		{
			l=izi-i-1;
			break;
		}
	}
	for(int i=izi+1;i<v1.size();i++)
	{
		if(v1[i]==1)
		{
			r=i-izi-1;
			break;
		}
	}
	return iii(ii(l,r),izi);
}
int S()
{
	vector<iii> v2;
	for(int i=0;i<v1.size();i++)
	{
		if(v1[i]==0)
		{
			v2.push_back(LR(i));
		}
	}
	sort(v2.begin(),v2.end(),gg);
	//cout<<v2[0].second<<" ";
	return v2[0].second;

}
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C_out.txt","w",stdout);
	int a,b;
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		cin>>a>>b;
		v1.clear();
		v1.push_back(1);
		for(int i=0;i<a;i++)
		{
			v1.push_back(0);
		}
		v1.push_back(1);
		int asd;
		for(int i=0;i<b-1;i++)
		{
			asd=S();
			//cout<<asd;
			v1[asd]=1;
		}
		asd=S();
		cout<<MM(asd).second<<" "<<MM(asd).first<<endl;

	}
}