#include <iostream>
#include <string>
using namespace std;
int shit(bool stl[], int length)
{
	int top(0), len(0);
	int top_(0), len_(0);
	bool last_stl(true);
	for (int i(0); i <= length; i++)
	{
		if (!stl[i])
		{
			if (last_stl){ top_ = i; len_ = 0; }
			++len_;
		}
		else
		{
			if (!last_stl)
			{
				if (len < len_){ top = top_; len = len_; }
			}
		}
		last_stl = stl[i];
	}
	int pos(top + (len / 2));
	stl[pos] = true;
	return pos;
}
#define StlNum	(1000)
void solve(int length, int people, int &max, int &min)
{
	if (length == people)
		return;
	bool stl[StlNum];
	for (int i(0); i < StlNum; i++)
	{
		stl[i] = (i < length) ? false : true;
	}
	// shitdown
	int pos(0);
	for (; people; --people){
		pos = shit(stl, length);
	}
	// max min
	int cnt(0);
	min = length;
	bool last_stl(true);
	for (int i(pos+1); (i < length+1); i++)
	{
		if (!stl[i])
		{
			++cnt;
		}
		else
		{
			if (max < cnt)
				max = cnt;
			if (min > cnt)
				min = cnt;
			break;
		}
	}
	last_stl=true;
	cnt = 0;
	for (int i(pos-1); i >= 0; --i)
	{
		if (!stl[i])
		{
			++cnt;
		}
		else
		{
			break;
		}
	}
	if (max < cnt)
		max = cnt;
	if (min > cnt)
		min = cnt;
#if 0
	int cnt(0);
	min = length;
	bool last_stl(true);
	for (int i(0); i <= length; i++)
	{
		if (!stl[i])
		{
			if (last_stl){ cnt = 0; }
			++cnt;
		}
		else
		{
			if (!last_stl)
			{
				if (max < cnt)
					max = cnt;
				if (min > cnt)
					min = cnt;
			}
			else { min = 0; }
		}
		last_stl = stl[i];
	}
#endif
}
int main() {
	int T;
	cin >> T;
	for (int cas(1); cas <= T; ++cas) {
		int n,k,max(0),min(0);
		cin >> n >> k;
		solve(n, k, max, min);
		cout << "Case #" << cas << ": " << to_string(max) <<" "<< to_string(min) << endl;
	}
	return 0;
}
