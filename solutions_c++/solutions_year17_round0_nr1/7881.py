#include <iostream>

using namespace std;
int main()
{
	int T, K;
	string S;
	int i, j, l;
	bool FLAG;
	int count;

	cin>>T;
	for(i=1; i<=T; i++)
	{
		cin>>S>>K;

		//cout<<"Current case :: S = "<<S<<" and K ="<<K<<"\n";
		count = 0;
		//cout<<"string now :: "<<S<<"\n";
		for(j=0; j<S.size(); j++)
		{
			if (S[j] == '-')
			{
				if ( j+K > S.size() )
					break;

				for(l=j; l<j+K; l++)
				{
					if (S[l] == '-')
						S[l] = '+';
					else
						S[l] = '-';
				}
				count = count + 1;
				//cout<<"string now :: "<<S<<"\n";
			}
		}

		FLAG = false;
		for(j=0; j<S.size(); j++)
		{
			if ( S[j] != '+' )
			{
				cout<<"Case #"<<i<<": IMPOSSIBLE\n";
				FLAG = true;
				break;
			}
		}

		if (FLAG == false)
			cout<<"Case #"<<i<<": "<<count<<"\n";
	}

	return 0;
}
