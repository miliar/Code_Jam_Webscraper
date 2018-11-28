#include <bits/stdc++.h>


using namespace std;
int main() 
{
	std::cin.sync_with_stdio(false);
	cout << fixed << setprecision(7);
	int T;
	cin >> T;
	double pi = 3.14159265359;
	for (int c = 0; c<T; ++c)
	{
		int n, k;
		cin >> n >> k;
		vector<double> r(n), h(n), a(n);
		vector<pair<double, double> > v(n);
		for (int i=0; i<n; ++i)
		{
			cin >> r[i] >> h[i];
			v[i] = {r[i], 2 * r[i] * pi * h[i]};
			
		}
		sort(v.begin(), v.end());
		double Amax = 0;
		for (int b = k-1; b<n; ++b)
		{
			double A = v[b].first*v[b].first*pi + v[b].second;
			std::sort(v.begin(), v.begin()+b, [](auto &left, auto &right) {
    return left.second < right.second;
});

			for (int i = b-1; i>b-k; --i)
				A += v[i].second;

			if (A > Amax)
			{
				Amax = A;
			}
		}

		cout << "Case #" << c+1 << ": "  << Amax << endl;
	
	}

}
