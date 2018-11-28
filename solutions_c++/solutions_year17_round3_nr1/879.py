#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <functional>

#define SIZE(x) (int)x.size()
#define st first
#define nd second

using namespace std;
typedef long double LD;
const LD PI = 3.14159265358979323846L;

struct placek
{
	LD R,H;
	LD powBezPi() const { return R*R; }
	LD powBoczBezPi() const { return 2*R*H; }
	bool operator>(const placek& other) const
	{
		return powBoczBezPi()>other.powBoczBezPi();
	}
};

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int nrTestu=1; nrTestu<=Testow; ++nrTestu)
	{
		int N,K;
		cin>>N>>K;

		vector<placek> placki(N);
		for (int i=0; i<N; ++i) cin>>placki[i].R>>placki[i].H;
		sort(placki.begin(),placki.end(),greater<placek>());
		
		LD maxWynikBezPi = 0.0L;
		for (int i=0; i<N; ++i)
		{
			placek Pierwszy = placki[i];
			LD sumaBocznych = Pierwszy.powBoczBezPi();
			LD maxR = placki[i].R;

			int licznik = 1;
			for (int j=0; j<N; ++j)
			{
				if (licznik==K) break;

				if (j==i) continue;
				if (placki[j].R>maxR) continue;

				++licznik;
				sumaBocznych += placki[j].powBoczBezPi();
			}

			LD wynikBezPi = sumaBocznych + Pierwszy.powBezPi();
			maxWynikBezPi = max(maxWynikBezPi,wynikBezPi);
		}

		LD wynik = maxWynikBezPi * PI;
		printf("Case #%d: %.9Lf\n",nrTestu,wynik);
	}

	return 0;
}