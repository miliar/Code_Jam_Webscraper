#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

char ans[2000];
int len = 0;
int x[10];
int last[10];
int m[300];
char rm[10];

bool check()
{
	for (int i = 1;i < len;++ i)
		if (m[ans[i]] & m[ans[i-1]])
			return 0;
	if (m[ans[0]] & m[ans[len-1]])
		return 0;
	return 1;
}

bool get_ans(int pre, int l)
{
	if (l == len)
	{
		ans[l] = 0;
		return check();
	}
	
	for (int i = 0;i <= 2;++ i)
		if (last[1<<i] < last[7-(1<<i)] - 1)
			return 0;
	
	int cnt = 0;
	for (int i = 0;i <= 2;++ i)
		if (pre & (1 << i))
			++ cnt;
	
	if (cnt == 3)
		cerr <<"ERROR" << endl;
	else if (cnt == 2)
	{
		if (last[7-pre] == 0)
			return 0;
		ans[l] = rm[7-pre];
		-- last[7-pre];
		return get_ans(7-pre, l+1);
	}

	if (last[pre] == last[7-pre] && last[pre] != 0)
	{
		for (int i = 0;i < last[pre];++ i)
		{
			ans[l+i*2] = rm[7-pre];
			ans[l+i*2+1] = rm[pre];
		}
		int xx = last[pre];
		last[pre] = last[7-pre] = 0;
		return get_ans(pre, l+xx*2);
	}
	
	int _max = 0;
	int max_p = 0;
	for (int i = 0;i <= 2;++ i)
		if (_max < last[1<<i] && ((1 << i) != pre))
		{
			_max = last[1<<i];
			max_p = (1<<i);
		}
	if (max_p == 0)
	{
		if (last[7-pre] == 0)
			return 0;
		ans[l] = rm[7-pre];
		-- last[7-pre];
		return get_ans(7-pre, l+1);
	}
	
	ans[l] = rm[max_p];
	-- last[max_p];
	return get_ans(max_p, l+1);
}

int main(int argc, char *argv[])
{	
	if (argc == 1)
	{
		freopen("in", "r", stdin);
		freopen("out","w",stdout);
	}
	else
	{
		if (freopen(argv[1], "r",stdin) == NULL)
		{
			cerr << "open file failed" << endl;
			return 0;
		}
		freopen("ans","w",stdout);
	}
	int T;
	scanf("%d" , &T);
	m['R'] = 1;
	m['Y'] = 2;
	m['B'] = 4;
	m['O'] = 3;
	m['G'] = 6;
	m['V'] = 5;
	rm[1] = 'R';
	rm[2] = 'Y';
	rm[3] = 'O';
	rm[4] = 'B';
	rm[5] = 'V';
	rm[6] = 'G';
	for (int Case = 1;Case <= T;++ Case)
	{
		bool have = 0;
		scanf("%d%d%d%d%d%d%d", &len, &x[1], &x[3], &x[2], &x[6], &x[4], &x[5]);
		for (int i = 1;i <= 6;++ i)
		if (x[i])
		{
			for (int j = 1;j <= 6;++ j)
				last[j] = x[j];
			ans[0] = rm[i];
			-- last[i];
			if (get_ans(i, 1))
			{
				have = 1;
				break;
			}
		}
		printf("Case #%d: ", Case);
		if (have)
			printf("%s\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
