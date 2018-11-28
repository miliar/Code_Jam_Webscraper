#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 10100;
typedef long long ll;


ll n;
int digit[100];
inline bool ok(ll x)
{
	int tmp,pre = 10;
	while(x)
	{
		tmp = x % 10;
		x /= 10;
		if(tmp == 0) return 0;
		if(tmp > pre) return 0;
		pre = tmp;
	}
	return 1;

}
int cnt;
void cal(ll x)
{
	memset(digit, 0, sizeof(digit));
	int tmp;
	cnt = 0;
	while(x)
	{
		digit[cnt++] = x % 10;
		x /= 10;
	}

}

inline bool ok2(int pos)
{
	int pre = 10;
	for(int i = pos; i < cnt; ++i)
	{
		if(digit[i] <= 0) return 0;
		if(digit[i] > pre) return 0;
		pre = digit[i];
	}
	return 1;
}

void work()
{
	for(int i = 0; i < cnt - 1; ++i)
	{
		digit[i] = 9;
		digit[i+1]--;
		if(ok2(i+1)) break;
	}
}

int main()
{
	freopen("B-large.in","r", stdin);
	freopen("B-large-attempt.out","w", stdout);
	int t;
	int ca = 0;
	scanf("%d",&t);
	ll ans;
	while(t--)
	{
		scanf("%lld",&n);
		if(ok(n)) printf("Case #%d: %lld\n",++ca,n);
		else
		{
			cal(n);
			work();
			printf("Case #%d: ",++ca);
            for(int i = cnt - 1; i >= 0;)
			{
				if(digit[i] <= 0)
				{
					//cout << digit[i] << endl;
					--i;
				}
				else printf("%d",digit[i--]);
			}

			printf("\n");
		}
	}
	return 0;
}
/*
111111111111111110
Case #4: 999999999999999999
99999999999999999
*/
