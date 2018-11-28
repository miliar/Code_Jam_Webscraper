#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
#define FIlkin_Maksim int main()
int pp[1000006];

FIlkin_Maksim
{
	freopen("solve.in","r",stdin);
	freopen("solve.out","w",stdout);
	int kk;
	cin>>kk;
	for(int ll=0;ll<kk;ll++)
	{
		set<int>mas;
		int n,k;
		cin>>n>>k;
		mas.insert(n);
		for(int i=0;i<=n;i++)
			pp[i]=0;
		pp[n]++;
		k--;
		for(int i=0;i<k;i++)
		{
			set<int>::iterator iter=mas.end();
			--iter;
			int p=*iter;
			pp[p]--;
			if(pp[p]<=0)
				mas.erase(iter);
			p--;
			int x1,x2;
			x1=p/2;
			x2=x1+(p%2);
			mas.insert(x1);
			pp[x1]++;
			mas.insert(x2);
			pp[x2]++;
		}
		set<int>::iterator iter=mas.end();
		--iter;
		int ans=*(iter);
		ans--;
		cout<<"Case #"<<ll+1<<": "<<(ans/2)+(ans%2)<<' '<<ans/2<<endl;
	}
}