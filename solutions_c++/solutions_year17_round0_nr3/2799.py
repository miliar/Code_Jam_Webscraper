#include <iostream>
#include <string>
#include <utility>

#define SIZE(x) (int)x.size()
#define st first
#define nd second

using namespace std;
typedef long long LL;
typedef pair<LL,LL> para;

class problem
{
private:
	LL N,K;

	void upgrade(para& noweMini, para& noweMaks, const para& P, bool czyMaks=false)
	{
		LL rozmiar = P.st;
		LL cnt = P.nd;

		if (rozmiar%2==1)
		{
			if (czyMaks) noweMaks.nd += 2*cnt;
			else noweMini.nd += 2*cnt;
		}
		else
		{
			noweMini.nd += cnt;
			noweMaks.nd += cnt;
		}
	}

	para solve()
	{	
		LL step = 0;
		LL dodac = 1;
		para mini(N,1),maks(-1,0);

		while (step+dodac<K)
		{
			step += dodac;

			LL nowyRozmiar = (mini.st-1)/2;
			para noweMini(nowyRozmiar,0),noweMaks(nowyRozmiar+1,0);
			
			upgrade(noweMini,noweMaks,mini);
			upgrade(noweMini,noweMaks,maks,true);
			mini=noweMini; maks=noweMaks;

			dodac<<=1;
		}
		LL zostalo = K-step;
		LL pom;

		if (step==K) pom = (maks.nd>0)? maks.st : mini.st;
		else pom = (zostalo<=maks.nd)? maks.st : mini.st;

		if (pom==0) return para(0,0);
		if (pom%2==0) return para((pom-1)/2+1,(pom-1)/2);
		return para((pom-1)/2,(pom-1)/2);		
	}
public:
	void czytaj()
	{
		cin>>N>>K;
	}
	void wypiszWynik()
	{
		para wynik=solve();
		cout<<wynik.st<<' '<<wynik.nd;
	}
};

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int nrTestu=1; nrTestu<=Testow; ++nrTestu)
	{
		problem Prob;
		Prob.czytaj();
		cout<<"Case #"<<nrTestu<<": ";
		Prob.wypiszWynik();
		cout<<endl;
	}

	return 0;
}