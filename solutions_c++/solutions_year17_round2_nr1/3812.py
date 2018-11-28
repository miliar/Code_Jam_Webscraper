#include <cstdio>
#include <algorithm>
#include <functional>
#include <map>
//#include <math.h>

using namespace std;
typedef long long ll;

#ifdef _MSC_VER
#pragma warning(disable: 4996) // Disable deprecation
#endif

pair<int, int> gHorses[10000+16];
pair<int, int> gHorses2[10000 + 16];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int D, N;
		scanf("%d%d", &D, &N);
		for (int i = 0; i < N; ++i)
		{
			int Ki, Si;
			scanf("%d%d", &Ki, &Si);
			gHorses[i] = { Ki, Si };
		}
		sort(gHorses, gHorses + N);
		int nH = 0;
		gHorses2[nH++] = gHorses[0];
		for (int i = 1; i<N; ++i)
		{
			int dv = gHorses[i].second - gHorses2[nH-1].second; //dv
			if (dv < 0)
			{
				gHorses2[nH++] = gHorses[i];
			}
		}

		double st = 0.0;
		double lastV = gHorses2[nH-1].second;
		for (int i = nH-1; i>=0; --i)
		{
			double s = gHorses2[i].first + st * gHorses2[i].second;
			if (s < D)
			{
				double dt = (D - s) / gHorses2[i].second;
				st += dt;
			}
		}
		double ans = D / st;
		printf("Case #%d: %.7lf\n", t, ans);
	}
	fclose(stdout);
	return 0;
}
