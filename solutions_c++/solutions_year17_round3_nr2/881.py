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

typedef pair<int,int> para;

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int nrTestu=1; nrTestu<=Testow; ++nrTestu)
	{
		int Ac,Aj;
		cin>>Ac>>Aj;

		int suma=Ac+Aj;
		vector<para> V(suma);
		for (int i=0; i<suma; ++i) cin>>V[i].st>>V[i].nd;
		sort(V.begin(),V.end());

		int wynik = 2;

		if (Ac==2 || Aj==2)
		{
			para A = V[0];
			para B = V[1];
			para C = A; C.st += 1440; C.nd += 1440;

			bool daSie = false;
			if (B.nd - A.st <= 720) daSie = true;
			if (C.nd - B.st <= 720) daSie = true;

			if (!daSie) wynik = 4;	
		}
		printf("Case #%d: %d\n",nrTestu,wynik);
	}

	return 0;
}