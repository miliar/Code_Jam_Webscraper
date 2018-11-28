#include<cstdio>
#include<algorithm>
#define N 210
using namespace std;

int T, AC, AJ, CC[N], CJ[N], CL, JL, list[N], WC[N], WJ[N], YC[N], YJ[N];
struct Data
{
	int l, r;
	void read(){scanf("%d%d", &l, &r);}
}C[N], J[N];
bool operator < (Data a, Data b){return a.l < b.l;}
bool cmp1(int a, int b){return WC[a] < WC[b];}
bool cmp2(int a, int b){return WJ[a] < WJ[b];}

int Calc()
{
	if (AC + AJ == 1) return 2;
	for (int i = 1; i <= AC; i++) YC[i] = CC[i] = 0;
	for (int i = 1; i <= AJ; i++) YJ[i] = CJ[i] = 0;
	sort(C + 1, C + 1 + AC);
	sort(J + 1, J + 1 + AJ);
	int i = 1, j = 1, fl = 0;
	if (i <= AC && j <= AJ)
	{
		if (C[1].l < J[1].l)
		{
			i++;
			fl = 0;
		}
		else
		{
			j++;
			fl = 1;
		}
		while (i <= AC && j <= AJ)
		{
			if (C[i].l < J[j].l)
			{
				if (!fl)
				{
					CC[i - 1] = 1;
					WC[i - 1] = C[i].l - C[i - 1].r;
				}
				i++;
				fl = 0;
			}
			else
			{
				if (fl)
				{
					CJ[j - 1] = 1;
					WJ[j - 1] = J[j].l - J[j - 1].r;
				}
				j++;
				fl = 1;
			}
		}
	}
	if (i <= AC)
	{
		for (int I = i; I < AC; I++)
		{
			CC[I] = 1;
			WC[I] = C[I + 1].l - C[I].r;
		}
		if (!AJ || C[1].l < J[1].l)
		{
			CC[AC] = 1;
			WC[AC] = C[1].l + 1440 - C[AC].r;
		}
	}
	else
	{
		for (int I = j; I < AJ; I++)
		{
			CJ[I] = 1;
			WJ[I] = J[I + 1].l - J[I].r;
		}
		if (!AC || C[1].l > J[1].l)
		{
			CJ[AJ] = 1;
			WJ[AJ] = J[1].l + 1440 - J[AJ].r;
		}
	}
	CL = JL = 720;
	int tot = 0;
	for (int i = 1; i <= AC; i++) if (CC[i]) list[++tot] = i;
	sort(list + 1, list + 1 + tot, cmp1);
	for (int i = 1; i <= AC; i++) CL -= (C[i].r - C[i].l);
	for (int i = 1; i <= tot; i++)
	{
		if (CL < WC[list[i]]) break;
		CL -= WC[list[i]];
		YC[list[i]] = 1;
	}
	tot = 0;
	for (int i = 1; i <= AJ; i++) if (CJ[i]) list[++tot] = i;
	sort(list + 1, list + 1 + tot, cmp2);
	for (int i = 1; i <= AJ; i++) JL -= (J[i].r - J[i].l);
	for (int i = 1; i <= tot; i++)
	{
		if (JL < WJ[list[i]]) break;
		JL -= WJ[list[i]];
		YJ[list[i]] = 1;
	}
	int ans = 0;
	for (int i = 1; i <= AC; i++)
	{
		if (CC[i])
		{
			if (!YC[i]) ans += 2;
		}
		else ans++;
	}
	for (int i = 1; i <= AJ; i++)
	{
		if (CJ[i])
		{
			if (!YJ[i]) ans += 2;
		}
		else ans++;
	}
//	if (ans == 1) ans++;
//	for (int i = 1; i <= AC; i++) printf("%d\n", CC[i]);
	return ans;
}

int main()
{
//	freopen("B.in", "r", stdin);
//	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &AC, &AJ);
		for (int i = 1; i <= AC; i++) C[i].read();
		for (int i = 1; i <= AJ; i++) J[i].read();
		printf("Case #%d: %d\n", I, Calc());
	}
	return 0;
}
