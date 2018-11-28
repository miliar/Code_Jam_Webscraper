#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <cstdio>
#include <iostream>
#define S(x) scanf("%lld",&x)
#define P(x) printf("%lld",x)
#define LI long long int
using namespace std;




int main() {
	LI t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		LI n,ans,minus,num;
		cin>>n;
		ans=0;
		minus=1;
		num=n;
		while(num>0)
		{
			minus*=10;
			if(num%10<(num/10)%10)
			{
				num/=10;
				num--;
				ans=minus;
			}
			else num/=10;
		}
		if(ans>0)
		{
			n/=ans;
			n--;
			n*=ans;
			n+=(ans-1);
		}
				
		
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
	return 0;
}
