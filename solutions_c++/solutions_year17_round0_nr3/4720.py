#include <cstdio>
#include <iostream>
using namespace std;
typedef unsigned long long lln;
int main()
{
	int C,a=1;
	cin >> C;
	while(C--)
	{
		lln room;
		lln p;
		lln base,cnt;
		cin >> room >> p;
		int pwr=0;
		int temp=p;
		while(temp){temp>>=1;pwr++;}
		pwr--;
		cnt=(room-((1<<pwr)-1))%(1<<pwr);
		base=(room-((1<<pwr)-1))/(1<<pwr);
		if(p<=cnt+(1<<pwr)-1) base++;
		printf("Case #%d: %d %d\n",a,base-1-(base-1)/2,(base-1)/2);

		a++;
	}
	return 0;
}
