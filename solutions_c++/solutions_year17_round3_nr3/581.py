#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
int n, t, k;
struct Node
{
	ld am;
	int num;
	bool operator<(const Node &o) const
	{
		return am > o.am;
	}
};
int main()
{
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d", &n, &k);
		ld u;
		scanf(" %Lf", &u);
		priority_queue<Node> pq;
		Node no;
		for (int i = 0; i < n; i++)
		{
			ld in;
			scanf(" %Lf", &in);
			no.am = in;
			no.num = 1;
			pq.push(no);
		}
		while (u && pq.size() > 1)
		{
			Node fir = pq.top(); pq.pop();
			Node sec = pq.top();
			if ((sec.am-fir.am)*fir.num <= u)
			{
				
				u-= (sec.am-fir.am)*fir.num;
				sec.num+=fir.num;
				pq.pop();
				pq.push(sec);
			}
			else
			{
				fir.am += u/fir.num;
				pq.push(fir);
				u = 0;
			}
		}
		ld ans = 1.0;
		if (pq.size())
		{
			Node fir = pq.top(); pq.pop();
			fir.am += u/fir.num;
			pq.push(fir);
		}
		while (!pq.empty())
		{
			Node a = pq.top();
			pq.pop();
			for (int i = 0; i < a.num; i++) ans*=a.am;
		}
		printf("Case #%d: %Lf\n", i, ans);
	}
}