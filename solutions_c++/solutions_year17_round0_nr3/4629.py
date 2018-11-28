#include <iostream>
#include <queue>
using namespace std;

#define VALUE	0
#define CNT		1
unsigned long long ary[100][2];
int idx = 0;
int fd(unsigned long long val, int cnt)
{
	for (int i = idx - 1; i >= 0; i--)
	{
		if (ary[i][VALUE] == val)
		{
			ary[i][CNT] += cnt;
			return 1;
		}
	}
	return 0;
}
struct NS
{
	unsigned long long Nv;
	int Nc;
};
void process(int tc)
{
	idx = 0;
	for (int i = 0; i < 100; i++) ary[i][0] = ary[i][1] = 0;
	unsigned long long N, K;
	cin >> N >> K;

	queue<NS> Q;
	NS start;
	start.Nv = N;
	start.Nc = 1;

	Q.push(start);
	ary[idx][VALUE] = N;
	ary[idx][CNT] = 1;
	idx++;

	NS v;
	NS next;
	while (!Q.empty())
	{
		v = Q.front();
		if (v.Nv < 1) break;
		Q.pop();
		if (v.Nv % 2 == 1)
		{
			next.Nv = (v.Nv >> 1);
			next.Nc = (v.Nc << 1);
			Q.push(next);
			if (next.Nv >0 && fd(next.Nv, next.Nc) == 0)
			{
				ary[idx][VALUE] = next.Nv;
				ary[idx][CNT] = next.Nc;
				idx++;
			}
		}
		else
		{
			next.Nv = (v.Nv >> 1);
			next.Nc = (v.Nc);	

			Q.push(next);
			if (next.Nv > 0 && fd(next.Nv, next.Nc) == 0)
			{
				ary[idx][VALUE] = next.Nv;
				ary[idx][CNT] = next.Nc;
				idx++;
			}

			next.Nv = (v.Nv >> 1)-1;
			next.Nc = (v.Nc);

			Q.push(next);
			if (next.Nv > 0 && fd(next.Nv, next.Nc) == 0)
			{
				ary[idx][VALUE] = next.Nv;
				ary[idx][CNT] = next.Nc;
				idx++;
			}
		}
	}



	int idx2 = 0;
	unsigned long long remain = K;
	unsigned long long ans[2] = {-1, -1};
	while (ans[0] == -1)
	{
		if (remain <= ary[idx2][CNT])
		{
			if (ary[idx2][VALUE] % 2 == 1)
			{
				ans[0] = ans[1] = (ary[idx2][VALUE] >> 1);
			}
			else
			{
				ans[0] = (ary[idx2][VALUE] >> 1);
				if (ans[0] == 0) ans[1] = ans[0];
				else ans[1] = (ary[idx2][VALUE] >> 1)-1;
			}
		}
		else
		{
			remain -= ary[idx2][CNT];
		}
		idx2++;
	}
	cout << "Case #" << tc << ": " << ans[0] << " " << ans[1] << endl;

}
int main()
{
	int C;
	cin >> C;

	for (int i = 0; i < C; i++) process(i + 1);
	return 0;
}