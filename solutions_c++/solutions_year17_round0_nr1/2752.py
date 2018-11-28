#include <iostream>
#include <string>

#define SIZE(x) (int)x.size()

using namespace std;

class problem
{
private:
	string S;
	int K;

	void flip(int poz)
	{
		if (S[poz]=='+') S[poz]='-';
		else S[poz]='+';
	}

	int solve()
	{	
		int licznik=0;

		for (int i=0; i<=SIZE(S)-K; ++i)
		{
			if (S[i]=='+') continue;
			for (int j=0; j<K; ++j) flip(i+j);
			++licznik;
		}

		bool udaloSie = true;
		for (int i=SIZE(S)-K+1; i<SIZE(S); ++i)
		{
			if (S[i]=='-') udaloSie=false;
		}
		if (!udaloSie) return -1;
		
		return licznik;
	}
public:
	void czytaj()
	{
		cin>>S>>K;
	}
	void wypiszWynik()
	{
		int wynik=solve();
		if (wynik==-1) cout<<"IMPOSSIBLE";
		else cout<<wynik;
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