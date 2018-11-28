#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long ll;

const int maxn = 200005;
const double eps = 1e-8;

double d,n;

double k[maxn],m[maxn];

double solve(double x)
{
	for(int i=1;i<=n;i++)
	{
		if(x > m[i])
		{
			double t = k[i]/(x-m[i]);
			if(t * x < d)
				return 0;
		}
	}
	return 1;
}
int main()
{
	cout << setprecision(8); 
	cout <<setiosflags(ios::fixed);
	int t,cs = 0;
	cin>>t;
	while(t--)
	{
		cin >> d >> n;
		double ma = 0;
		for(int i=1;i<=n;i++)
		{
			cin >> k[i] >> m[i];
			ma = max(ma,d*m[i]/(d-k[i]));
		}
		double l = 0,r = ma + eps,res;
		//printf("ma= %f\n",ma);
		int cnt = 0;
		while(r-l>eps)
		{
			cnt++;
			if(cnt>140000)
				break;
			double mid = (l+r)/2;
			//printf("mid=%lf\n",mid);
			if(solve(mid))
			{
				res = mid;
				l = mid;
			}
			else
				r = mid;
		}
		printf("Case #%d: %.7f\n",++cs,(l+r)/2);
		//cout << "Case #" << ++cs << ": " << res << endl;
	}
}