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
#include <bitset>
#include<math.h>
using namespace std;
#define MAXN 1005
int N, K,Q;
struct Cake
{
	int Ri;
	int Hi;
}cakes[MAXN];
bool cmpR(const Cake &a, const Cake&b)
{
	return a.Ri > b.Ri;
}
double f[MAXN][MAXN];
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	const double PI = 3.14159265358979323846;
	cin >> Q;
	for (size_t q = 0; q < Q; q++)
	{
		cin >> N >> K;
		for (int t = 1; t <= N; t++)
		{
			cin >> cakes[t].Ri >> cakes[t].Hi;
		}
		sort(cakes+1,cakes+N+1,cmpR);
		fill_n(f[0], MAXN*MAXN, 0);
		for (int i = 1; i <= N; i++)
		{
			for (int j = 1; j <= K; j++)
			{
				if(j==1)
					f[i][j] =  2 * PI*cakes[i].Ri*cakes[i].Hi + PI*cakes[i].Ri*cakes[i].Ri;
				for (int ii = j-1; ii < i; ii++)
				{
					if (j != 1)
						f[i][j] = max(f[i][j], f[ii][j - 1] + 2 * PI*cakes[i].Ri*cakes[i].Hi);
					else
						f[i][j] = max(f[i][j], f[ii][j - 1] + 2 * PI*cakes[i].Ri*cakes[i].Hi+PI*cakes[i].Ri*cakes[i].Ri);
				}
			}
		}
		double ans = 0;
		for (size_t i = 0; i <= N; i++)
		{
			ans = max(ans, f[i][K]);
		}
		cout << "Case #" << q + 1 << ": " << fixed << setprecision(9) << ans << endl;
	}

	return 0;
}
