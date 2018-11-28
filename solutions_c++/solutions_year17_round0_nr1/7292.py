#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		char s[1011];
		scanf("%s", s);
		int d;
		scanf("%d", &d);
		int len = strlen(s);
		int cnt = 0;
		int flag = 0;
		for(int i = 0; i < len; i++)
			if(s[i] == '-')
			{
				if(i > len - d)
				{
					flag = 1;
					break;
				}
				else
				{
					cnt += 1;
					for(int j = i; j < i + d; j++)
						if(s[j] == '-')
							s[j] = '+';
						else s[j] = '-';
				}
			}
		printf("Case #%d: ", ++cas);
		if(flag)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", cnt);
	}
}