#include<iostream>
using namespace std;
int test()
{
	int cnt[4];
	int n,p;
	cin >> n >>p;
	for(int i=0;i<p;i++)cnt[i]=0;
	for(int i=0;i<n;i++)
	{
		int x;
		cin >> x;
		cnt[x%p]++;
	}
	int res=0;
	res+=cnt[0];
	if(p==2)
	{
		res+=(cnt[1]+1)/2;
	}
	else if(p==3)
	{
		int tmp=min(cnt[1],cnt[2]);
		res+=tmp;
		cnt[1]-=tmp;
		cnt[2]-=tmp;
		tmp=cnt[1]+cnt[2];
		res+=(tmp+2)/3;

	}
	else if(p==4)
	{
		int tmp=min(cnt[1],cnt[3]);
		res+=tmp;
		cnt[1]-=tmp;
		cnt[3]-=tmp;
		tmp=cnt[1]+cnt[3];
		res+=tmp/4;
		tmp%=4;
		res+=cnt[2]/2;
		cnt[2]%=2;
		if(cnt[2]==1 and tmp>=2)
		{
			cnt[2]=1;
			tmp-=2;
			res++;
		}
		if(cnt[2]!=0 or tmp!=0)
			res++;
	}
	return res;
}
int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		auto res=test();
		cout << "Case #"<<i<< ": "<<res << "\n";
	}
}
