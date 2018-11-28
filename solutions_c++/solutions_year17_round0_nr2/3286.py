#include <bits/stdc++.h>
#define ll long long
using namespace std;

int ar[20];
int len;


int findLen(ll n)
{
	int len = 0;
	while(n)
	{
		len++;
		n = n / 10;
	}
	return len;
}

ll makeVal(int l)
{
	ll k = 0;
	while(l)
	{
		l--;
		k = k * 10 + 9;
	}
	return k;
}

bool isOK(int l)
{
	for(int i = l - 1; i >= 1; i--)
	{
		if(ar[i + 1] > ar[i])
		{
			return false;
		}
	}
	return true;
}

void split(ll n, int len)
{
	for(int i = 1; i <= len; i++)
	{
		ar[i] = n % 10;
		n = n / 10;
	}
	/*for(int i = len; i >= 1; i--)
	{
		cout<<ar[i]<<" ";
	}cout<<endl;*/
}


int main()
{
	freopen("0.in", "r", stdin);
	freopen("00.out", "w", stdout);

	int tc;

	scanf("%d", &tc);

	ll N;

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		cin>>N;

		int l = findLen(N);

		if(l == 1)
		{
			cout<<N<<endl;
			continue;
		}
		ll ans = makeVal(l - 1);
		split(N, l);

		int fpos = -1;

		if(isOK(l))
		{
			cout<<N<<endl;
			continue;
		}

		bool br = true;

		for(int i = l; i >= 1; i--)
		{
			if(i < l)
			{
				if(ar[i + 1] > ar[i])
				{
					br = false;
				}
			}
			if(ar[i] > 1)
			{
				if(i == l)
				{
					fpos = i;
				}
				else
				{
					if(br)
					{
						if(ar[i] > ar[i + 1])
						{
							fpos = i;
						}
					}
				}
			}
		}
		if(fpos == -1)
		{
			cout<<ans<<endl;
			continue;
		}
		ll ansi = 0;

		for(int i = l; i > fpos; i--)
		{
			ansi = ansi * 10 + ar[i];
		}
		ansi = ansi * 10 + ar[fpos] - 1;

		for(int i = fpos - 1; i >= 1; i--)
		{
			ansi = ansi * 10 + 9;
		}
		cout<<max(ansi, ans)<<endl;
	}

	return 0;
}