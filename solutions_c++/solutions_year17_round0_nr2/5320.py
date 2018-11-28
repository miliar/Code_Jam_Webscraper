#include<bits/stdc++.h>
using namespace std;
vector<long long> v;
vector<long long>::iterator it;
void gen(string,int);
int t;
int main()
{
//	scanf("%d",&n);
	gen("",0);
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		long long n;
		scanf("%lld",&n);
		it=upper_bound(v.begin(),v.end(),n);
		printf("Case #%d: ",l);
		it--;
		printf("%lld\n",(*it));
	}
}
void gen(string tmp,int lv)
{
	if(lv==18)
	{
		stringstream ss;
		ss<<tmp;
		long long q;
		ss>>q;
//		printf("%lld %s\n",q,tmp.c_str());
		v.push_back(q);
		return;
	}
	int st;
	if(tmp.size()==0)
		st='0';
	else
		st=tmp[tmp.size()-1];
//	printf("B %d %s %d\n",st,tmp.c_str(),lv);
	for(int i=st;i<='9';i++)
	{
		char c=i;
//		printf("A %c\n",c);
//		getchar();
		gen(tmp+c,lv+1);
	}
}
