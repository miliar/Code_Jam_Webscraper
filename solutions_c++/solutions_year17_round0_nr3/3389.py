#include <bits/stdc++.h>
#define ll long long
using namespace std;

struct st
{
	int Max;
	int Min;
	int in;
	int l;
	int r;

	st(int lft, int rght)
	{
		l = lft;
		r = rght;
		calcVal();
		//cout<<"created "<<l<<" "<<r<<" "<<Min<<" "<<Max<<" "<<in<<endl;
	}

	void calcVal()
	{
		Min = (r - l) / 2;
		Max = Min;

		if((r - l) & 1)
		{
			Max++;
		}

		in = (l + r) / 2;
	}
	bool operator < (const st &b) const
	{
		return Min == b.Min ? Max == b.Max ? in > b.in : Max < b.Max : Min < b.Min;
	}
};

priority_queue<st>Q;

int main()
{
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);

	int tc;

	scanf("%d", &tc);

	for(int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		int N, K;

		scanf("%d %d", &N, &K);

		while(!Q.empty()) Q.pop();

		st s = st(1, N);

		Q.push(s);

		while(!Q.empty())
		{
			s = Q.top(); Q.pop();

			K--;

			//cout<<"Now at "<<s.l<<" "<<s.r<<" with min = "<<s.Min<<" max = "<<s.Max<<" ans = "<<s.in<<endl;

			if(!K)
			{
				printf("%d %d\n", s.Max, s.Min);
				break;
			}

			if(s.l == s.r)
			{
				continue;
			}
			if(s.in - 1 >= s.l)
			{
				st F = st(s.l, s.in - 1);
				Q.push(F);
			}
			if(s.in + 1 <= s.r)
			{
				st F = st(s.in + 1, s.r);
				Q.push(F);
			}
		}
	}

	return 0;
}