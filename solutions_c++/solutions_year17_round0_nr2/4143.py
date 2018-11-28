#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
	int tst;
	scanf("%d",&tst);
	for(int t=1;t<=tst;t++)
	{
		ll inp,num=0,now,bef=10,ten=1,tmp=0;
		bool flag=false;
		scanf("%lld",&inp);
		while(inp)
		{
//			cout<<num;
			now = inp%10;
			if(now > bef)
			{
				now--;
				num = now*ten + tmp;
			}
			else
			{
				num = num + now*ten;
			}
			bef = now;
			inp /=10;
			ten*=10;
			tmp = tmp*10+9;
//			cout<<"~"<<now<<" "<<bef<<"~";
//			cout<<" "<<num<<endl;
		}
		printf("Case #%d: %lld\n",t,num);
	}
}
