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
inline void getll(LL &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		printf("Case #%d: ", __rep);
		LL n;
		getll(n);

		char buf[25];
		sprintf(buf, "%lld", n);

		int len = strlen(buf);
		
		R(i,1,len)
		{
			if (buf[i-1] > buf[i])
			{
				int bc = i-1;
				while (bc > 0 && buf[bc-1] == buf[bc])
				{
					bc--;
				}
				buf[bc] = buf[bc]-1;
				R(j,bc+1,len)
				{
					buf[j] = '9';
				}
				break;
			}
		}
		int i=0;
		while (buf[i] == '0')
			i++;

		printf("%s\n", buf+i);
	}

	return 0;
}
	// char buf[10];
	// F(i,100000)
	// {
	// 	sprintf(buf,"%d",i);
	// 	for (int j=1; j<strlen(buf); j++)
	// 	{
	// 		if (buf[j-1] > buf[j])
	// 			break;
	// 		if (j==strlen(buf)-1)
	// 			cout << i << endl;
	// 	}
	// }
