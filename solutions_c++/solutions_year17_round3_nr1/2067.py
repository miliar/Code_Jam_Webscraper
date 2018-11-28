#if 1
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
//#define PI 3.14159265
#define PI 3.1415926535897932384626433
int N, K;
double dp[1001][1001];
FILE* pF;

FILE* pAnsF;
void reset()
{
	for (int i = 0; i <= N; i++)
		for (int j = 0; j <= N; j++)
			dp[i][j] = 0;

}
typedef struct node
{
	int r;
	int h;
};
vector<node>v;
bool comp(node A, node B)
{
	if (A.r > B.r)
	{
		return true;
	}
	return false;
}
double solve(int lastSelected, int soFarSelected)
{
	if (lastSelected >= 0)
		if (dp[lastSelected][soFarSelected])
			return dp[lastSelected][soFarSelected];
	if (soFarSelected == K)
	{
		return 0;
	}
	if (lastSelected == N-1)
		return -1000000;
	double ans = 0;
	for (int i = lastSelected+1; i < N; i++)
	{
		if (soFarSelected == 0)
			ans = max(ans, PI * v[i].r * v[i].r + 2 * PI * v[i].r*v[i].h + solve(i, soFarSelected + 1));
		else
			ans = max(ans,2 * PI * v[i].r*v[i].h + solve(i, soFarSelected + 1));
	}
	if(lastSelected >= 0)
		dp[lastSelected][soFarSelected] = ans;
	return ans;
}
int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);

	freopen_s(&pAnsF, "output.txt", "w", stdout);
	
	int Cases;	

	cin >> Cases;

	for (int c = 1; c <= Cases; c++)
	{
		cin >> N >> K;
		int R, H;
		for (int i = 1; i <= N; i++)
		{
			cin >> R >> H;
			node n;
			n.r = R;
			n.h = H;
			v.push_back(n);
		}
		sort(v.begin(), v.end(), comp);
		double ans = solve(-1, 0);
		cout << "Case #" << c << ": ";	
		printf("%.6f", ans);
		cout << endl;
		reset();
		v.clear();
	}

	return 0;
}
#endif