#include <bits/stdc++.h>
#define eps 1e-9
using namespace std;

vector < pair < int ,int > > vet;

bool testa(double vel, double val, int d)
{
	double times = ((double)d/vel);
	if(times >= val) return true;
	return false;
}

int main()
{
	int t, z=0;
	cin >> t;
	while (t--)
	{
		int d, n;
		cin >> d >> n;
		double ans = 0.;
		for (int i=0; i<n; i++)
		{
			int a, b;
			cin >> a >> b;
			vet.push_back(make_pair(a, b));
			ans = fmax(ans, (d-a)/(double)b);
		}
		double ini = 0.000000, fim = 10000000000000.0000000;
		double resp = 0.0;
		int x = 0;
		while (ini <= fim && x <= 777)
		{
			double meio = (ini+fim)/2.0;
			if(testa(meio, ans, d)){
				resp = meio;
				ini = meio + 0.000001;
			}	
			else {
				fim = meio - 0.000001;
			}
			x++;
		}
		printf("Case #%d: %.6lf\n", ++z, resp);
	}	
}
