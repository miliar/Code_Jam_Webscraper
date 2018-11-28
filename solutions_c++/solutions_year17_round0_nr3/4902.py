#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define LL long long
#define ULL unsigned long long
#define m_p make_pair
#define l_b lower_bound
#define p_b push_back
#define w1 first
#define w2 second
#define maxlongint 2147483647
#define biglongint 2139062143

priority_queue<int> F;
int tt, n, k, c;

int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%d", &tt);
	for (int gb = 1; gb <= tt; gb++)
	{
		scanf("%d %d", &n, &k);
		F.push(n);
		for (int i = 1; i < k; i++)
		{
			c = F.top();
			F.pop();
			if (c % 2 == 1) 
			{
				F.push(c / 2);
				F.push(c / 2);
			}
			else
			{
				F.push(c / 2);
				F.push(c / 2 - 1);
			}
		}
		printf("Case #%d: %d %d\n", gb, F.top() / 2, (F.top() - 1) / 2);
		while (!F.empty()) F.pop();
	}
	return 0;
}
