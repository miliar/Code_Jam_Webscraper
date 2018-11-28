#include <iostream>
#include <string>

#define SIZE(x) (int)x.size()

using namespace std;

class problem
{
private:
	string N;
	int len;
	string solve()
	{	
		for (int i=len-1; i>0; --i)
		{
			for (int j=i-1; j>=0; --j)
			{
				if (N[j]>N[i])
				{
					--N[j];
					while (++j<len) N[j]='9';
					break;
				}
			}
		}
		N.erase(0,N.find_first_not_of('0'));
		return N;
	}
public:
	void czytaj()
	{
		cin>>N;
		len=SIZE(N);
	}
	void wypiszWynik()
	{
		string wynik=solve();
		cout<<wynik;
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