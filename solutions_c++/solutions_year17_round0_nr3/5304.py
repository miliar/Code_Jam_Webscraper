#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
map<long long,long long> mym;
long long n,nk;
void task()
{
	cin>>n>>nk;
	mym.clear();
	mym[n]=1;
	
	long long lastleft=-1,lastright=-1;
	while(nk>0)
	{
		long long right=(--mym.end())->first;
		//cout<<"Now:"<<right<<endl;
		long long count=mym[right];
		mym.erase(right);
		long long dec=min(nk,count);
		lastright=(right-1)/2;
		lastleft=right/2;
		mym[lastleft]+=dec;
		mym[lastright]+=dec;
		nk-=dec;
	}
	cout<<lastleft<<" "<<lastright<<endl;
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt){printf("Case #%d: ",i);task();}
}
