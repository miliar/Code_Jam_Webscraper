#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int a;

bool ck(int x)
{
	int a1=x/1000;
	int a2=(x/100)%10;
	int a3=(x/10)%10;
	int a4=x%10;
	if(a1<=a2 && a2<=a3 && a3<=a4) return 1;
	return 0;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bs.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>a;
		for(int j=a;j>=1;j--)
			if(ck(j)) {printf("Case #%d: %d\n",i,j);break;}
	}
	return 0;
}
