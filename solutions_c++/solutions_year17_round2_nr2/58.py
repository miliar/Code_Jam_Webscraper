#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
#include <iterator>
#include <complex>
#include <random>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MEM(x, y) memset((x),(y),sizeof(x))
const LL INF = 1e9 + 7;
const int N = 1e5 + 10;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	scanf("%d", &ncase);
	int ks = 1;
	while (ncase--)
	{
		int n;
		int r, o, y, g, b, v;
		scanf("%d", &n);
		scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
		printf("Case #%d: ", ks++);
		/*
		A mane with only one color of hair appears to be that color. For example, a mane with only blue hairs is blue.
		A mane with red and yellow hairs appears orange. RY->O need B
		A mane with yellow and blue hairs appears green. YB->G need R
		A mane with red and blue hairs appears violet.	 RB->V need Y
		*/
		if (o + b == n)
		{
			if (o == b)
			{
				while (g--) putchar('O'), putchar('B');
				puts("");
			}
			else puts("IMPOSSIBLE");
			continue;
		}
		if(g + r == n)
		{
			if (g == r)
			{
				while (g--) putchar('G'), putchar('R');
				puts("");
			}
			else puts("IMPOSSIBLE");
			continue;
		}
		
		if (y + v == n)
		{
			if (y == v)
			{
				while (y--) putchar('Y'), putchar('V');
				puts("");
			}
			else puts("IMPOSSIBLE");
			continue;
		}
		/*
		A mane with only one color of hair appears to be that color. For example, a mane with only blue hairs is blue.
		A mane with red and yellow hairs appears orange. RY->O need B
		A mane with yellow and blue hairs appears green. YB->G need R
		A mane with red and blue hairs appears violet.	 RB->V need Y
		*/
		if (o > 0 && b <= o)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		if (g > 0 && r <= g)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		if (v > 0 && y <= v)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		r -= g;
		b -= o;
		y -= v;
		string ans;
		string s4;
		string s1 = string(r, 'R');
		string s2 = string(b, 'B');
		string s3 = string(y, 'Y');
		if (s1.length() < s2.length()) swap(s1, s2);
		if (s2.length() < s3.length()) swap(s2, s3);
		if (s1.length() < s2.length()) swap(s1, s2);
		while (!s1.empty() && !s2.empty())
		{
			if (s4.empty() || s4.back() == s2.back()) s4 += s1.back(), s1.pop_back();
			else s4 += s2.back(), s2.pop_back();
		}
		s4 += s1;
		s4 += s2;
		if (s4.back() != s4.front()) swap(s3, s4);
		int l = s3.length() - 1, r0 = s4.length() - 1;
		while (l >= 0 || r0 >= 0)
		{
			if (l >= 0)
			{
				ans.push_back(s3[l--]);
			}
			if (r0 >= 0)
			{
				ans.push_back(s4[r0--]);
			}
		}
		int flag = 1;
		for (int i = 1; i < ans.length(); i++)
		{
			if (ans[i] == ans[i - 1])
			{
				flag = 0;
				break;
			}
		}
		if (ans.front() == ans.back()) flag = 0;
		if (!flag)
		{
			puts("IMPOSSIBLE");
			continue;
		}
		for (auto &c : ans)
		{
			/*
			A mane with only one color of hair appears to be that color. For example, a mane with only blue hairs is blue.
			A mane with red and yellow hairs appears orange. RY->O need B
			A mane with yellow and blue hairs appears green. YB->G need R
			A mane with red and blue hairs appears violet.	 RB->V need Y
			*/
			putchar(c);
			if (c == 'B' && o > 0)
			{
				while (o--) putchar('O'), putchar('B');
			}
			if (c == 'R' && g > 0)
			{
				while (g--) putchar('G'), putchar('R');
			}
			if (c == 'Y' && v > 0)
			{
				while (v--) putchar('V'), putchar('Y');
			}
		}
		puts("");
	}
	return 0;
}