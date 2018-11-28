#include <iostream>
#include <cstdio>

using namespace std;

const double PI = 3.141592653589793;

int main(int argc, char const *argv[])
{
	int t, n, cas, k, i, tmp;
	long r[1050], h[1050];
	double ans;

	cin >> t;
	cas = 1;
	while (t) {
		cin >> n >> k;
		i = 0;
		
		for (int i = 0; i < n; ++i)
		{
			cin >> r[i] >> h[i];
		}

		for (int i = 0; i < n; ++i)
			for (int j = i+1; j < n; j++)
				if (2*r[i]*PI*h[i] < 2*r[j]*PI*h[j])
				{
					tmp = h[i];
					h[i] = h[j];
					h[j] = tmp;
					tmp = r[i];
					r[i] = r[j];
					r[j] = tmp;
				}

		long long rx = r[k-1];
		long long hx = h[k-1];

		for (int i = 0; i < k; ++i)
			for (int j = i+1; j < k; j++)
				if (r[i]<r[j])
				{
					tmp = h[i];
					h[i] = h[j];
					h[j] = tmp;
					tmp = r[i];
					r[i] = r[j];
					r[j] = tmp;
				}


		ans = PI*r[0]*r[0];
		bool flag = false;
		long long ry;
		long long hy;
		double maxx = 0;

		for (int i = k; i < n; ++i)
			if (maxx < PI*r[i]*r[i] + 2*PI*r[i]*h[i])
			{
				ry = r[i];
				hy = h[i];
				maxx = PI*r[i]*r[i] + 2*PI*r[i]*h[i];
			}

		/*cout << maxx << endl;*/

		if (ans + 2*PI*rx*hx < maxx)
			flag = true;

		/*cout << flag << endl;		*/

		for (int i = 0; i < k; ++i)
		{
			ans += 2*r[i]*PI*h[i];
			/*cout << r[i] << " " << h[i] << endl;*/
		}

		if (flag) {
			ans = ans - PI*r[0]*r[0] - 2*PI*rx*hx + maxx;
		}
		

		cout << "Case #" << cas++ << ": ";
		printf("%.9lf\n", ans);
		t--;
	}

	return 0;
}