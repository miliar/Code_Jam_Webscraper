#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
using namespace std;
#define MAXDIGIT 20
int numm[MAXDIGIT];
void dfs(int digit, int64_t num, int64_t N,bool flag,int64_t &ans)
{
	if (digit == 0)
	{
		if (numm[digit]>=numm[digit+1]&&num * 10 + numm[digit] <= N)
			ans = max(ans, num * 10 + numm[digit]);
		if (flag)
			ans = max(ans, num * 10 + 9);
	}
	else
	{
		//flag表示前面选了的一位比num的对应位小
		if (flag)
		{
			dfs(digit - 1, num * 10 + 9,N, flag, ans);
		}
		else
		{
			if (numm[digit] >= numm[digit + 1])
			{
				dfs(digit - 1, num * 10 + numm[digit], N, false, ans);
			}
			if (numm[digit] - 1 >= numm[digit + 1])
			{
				dfs(digit - 1, num * 10 + numm[digit] - 1, N, true, ans);
			}
		}
	}
}
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int64_t T, N;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cin >> N;
		int64_t M=N;
		int l = 0;
		fill(numm, numm + MAXDIGIT, 0);
		while (N)
		{
			numm[l++] = N %10;
			N /= 10;
		}
		int64_t ans = 0;
		dfs(l-1, 0, M, false, ans);
		cout << "Case #"<<t<<": "<<ans << endl;
	}

	return 0;
}
