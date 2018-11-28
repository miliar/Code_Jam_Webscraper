#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>

#define SIZE(x) (int)x.size()
#define st first
#define nd second

using namespace std;
typedef long double LD;
typedef pair<LD,LD> para;
typedef vector<para> VP;

class problem
{
private:
	VP konie;
	int N,D;

	LD solve()
	{
		LD maxTime = 0.0;
		for (int i=0; i<N; ++i)
		{
			LD dist = D-konie[i].st;
			LD time = dist/konie[i].nd;
			maxTime = max(maxTime,time);
		}
		return D/maxTime;
	}
public:
	void czytaj()
	{
		cin>>D>>N;
		konie.resize(N);
		for (int i=0; i<N; ++i) cin>>konie[i].st>>konie[i].nd;
	}
	void wypiszWynik()
	{
		LD wynik=solve();
		cout<<setprecision(9)<<wynik;
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