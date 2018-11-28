#include <bits/stdc++.h>
using namespace std;
const int N = 1210;
#define PI acos(-1)
typedef long long ll;
int mod = 1000000007;
struct Node
{
	int r, h;
	ll cp;
	void input()
	{
		scanf("%d%d", &r, &h);
		cp = (ll)r*h;
	}

}rec[N];
bool cmp(const Node &a, const Node &b)
{
	return a.cp > b.cp;
}

int n;

void run()
{
	int k;
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		rec[i].input();
	sort(rec, rec + n, cmp);
	ll ans = 0;
	for (int i = 0; i < n; i++)
	{
		ll tmp = (ll)rec[i].r*rec[i].r + (ll)rec[i].r*rec[i].h*2;
		int c = k - 1;
		for (int j = 0; j < n && c; j++) if (i != j)
		{	
			c--;
			if (rec[j].r <= rec[i].r)
				tmp += (ll)rec[j].r*rec[j].h*2;
		}
		if (c == 0)
			ans = max(tmp, ans);
	}
	printf("%.9f\n", (double)ans * PI);
}

int main()
{
	freopen("in.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);
	 freopen("output.txt", "w", stdout);
	int T, cas = 1;
	scanf("%d", &T);
	 
	while (T--)
	{ 
		printf("Case #%d: ", cas++);
		run();
	}
    return 0;
}