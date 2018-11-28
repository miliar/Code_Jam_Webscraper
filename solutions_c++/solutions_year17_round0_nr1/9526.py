#include<bits/stdc++.h>
using namespace std;
#define INF 2000000000
#define Clear(x, Num) memset(x, Num, sizeof(x))
#define Dig(x) ((x>='0') && (x<='9'))
#define Neg(x) (x=='-')
#define G_c() getchar()
typedef long long ll;

int T, k, flag, Res;
string str;

inline int gcd(int x, int y) { if (!y) return x; return gcd(y, x%y); }
inline void read(int &x){ char ch; int N=1; while ((ch=G_c()) && (!Dig(ch)) && (!Neg(ch))); if (Neg(ch)) { N=-1; while ((ch=G_c()) && (!Dig(ch))); } x=ch-48; while ((ch=G_c()) && (Dig(ch))) x=x*10+ch-48; x*=N; }
//inline void Insert(int u, int v) { To[Cnt]=v; Next[Cnt]=Head[u]; Head[u]=Cnt++; }

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> T;
	for (int _=1; _<=T; _++)
	{
		cin >> str >> k;
		flag=Res=0; int Len=str.length();
		for (int i=0; i<Len; i++)
			if (str[i]=='-')
				if (i+k>Len) { flag=1; break; }
				else
				{
					Res++;
					for (int j=0; j<k; j++) str[i+j]=(str[i+j]=='+')?'-':'+';
				}
		printf("Case #%d: ", _);
		if (!flag) printf("%d\n", Res); else puts("IMPOSSIBLE");
	}
}
