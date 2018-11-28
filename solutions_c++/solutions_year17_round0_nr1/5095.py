#include <bits/stdc++.h>
using namespace std;

#define R(i,a,b) for(int i=a;i<b;i++)
#define RE(i,a,b) for(int i=a;i<=b;i++)
#define RR(i,a,b) for(int i=a;i>b;i--)
#define RRE(i,a,b) for(int i=a;i>=b;i--)
#define F(i,n) for(int i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <int, int>
#define pb push_back
#define ft first
#define sd second
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

bool flag[1005];
string s;

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		printf("Case #%d: ", __rep);
		
		int k;
		
		cin >> s;
		get(k);

		int n = s.length();
		int counter = 0;
		memset(flag, 0, sizeof flag);
		int ans = 0;
		for (int i=0; i<n; i++)
		{
			counter += (int)(flag[i]);
			counter %= 2;

			if (counter == 0)
			{
				if (s[i] == '+')
					continue;
				else
				{
					counter = (counter+1)%2;
					if (i+k > n)
					{
						ans = -1;
						break;
					}
					flag[i+k] = true;
					ans++;
				}
			}
			else
			{
				if (s[i] == '-')
					continue;
				else
				{
					counter = (counter+1)%2;
					if (i+k > n)
					{
						ans = -1;
						break;
					}
					flag[i+k] = true;
					ans++;
				}
			}
		}
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}