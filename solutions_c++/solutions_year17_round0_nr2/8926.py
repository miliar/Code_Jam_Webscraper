#include <iostream>
using namespace std;
typedef long long LL;
const int N = 1005;

#define BUG

LL n,m;
int s[N];

int main()
{
#ifdef BUG
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
#endif
	int cc;
	scanf("%d",&cc);
	int cnt=0;
	for (int kk=1;kk<=cc;kk++)
	{
		scanf("%lld",&n);
		LL x=n;
		int pos=0;
		memset(s,0,sizeof(s));
		while (x>0)
		{
			s[pos++]=x%10;
			x/=10;
		}
		// cout<<pos<<" "<<n<<endl;
		LL tmp=0;
		for (int i=pos;i>0;i--)
		{
			LL se=0;
			for (int j=1;j<=i;j++)
				se=se*10+1;
			while (tmp+se<=n && tmp%10<=8)
				tmp+=se;
			// cout<<i<<" "<<se<<" "<<tmp<<endl;
		}
		printf("Case #%d: %lld\n",kk, tmp);
	}
	return 0;
}
