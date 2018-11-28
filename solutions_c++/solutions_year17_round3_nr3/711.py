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

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int nrTestu=1; nrTestu<=Testow; ++nrTestu)
	{
		int N,K; //K=N
		cin>>N>>K;

		LD U;
		cin>>U;

		vector<LD> V(N+1);
		for (int i=0; i<N; ++i) cin>>V[i];
		V[N]=1.0L;

		sort(V.begin(),V.end());

		while (true)
		{
			if (U<=0) break;
			if (V[0]>=1.0) break;

			int i=0;
			int j=1;
			while (j<N && V[j]==V[i]) ++j;
			int ile = j-i;
			LD roznica = V[j] - V[i];
			LD suma = ile*roznica;

			LD dyspozycja = min(U,suma);
			LD dodac = dyspozycja/ile;
			for (int k=i; k<j; ++k) V[k]+=dodac;
			U-=dyspozycja;
		}

		LD wynik = 1.0;
		for (int i=0; i<N; ++i) wynik*=V[i];

		printf("Case #%d: %.12Lf\n",nrTestu,wynik);
	}

	return 0;
}