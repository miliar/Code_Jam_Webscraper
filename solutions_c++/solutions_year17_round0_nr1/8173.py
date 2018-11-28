#include<iostream>
#include<cstdio>
#include<string>
using namespace std;


void alterarPanqueques(string panqueques, int posicionPanquequeTriste,int tamañoPala)
{
	for(int i = 0;i<tamañoPala;i++)
	{
		if(panqueques.at(posicionPanquequeTriste+i)=='-')
		{
			panqueques.at(posicionPanquequeTriste+i)='+';
		}else{
			panqueques.at(posicionPanquequeTriste+i)='-';
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;

	cin >> t;

	string panqueques;
	int tamañoPala;

	for(int i = 1;i<=t;i++)
	{
		cin >> panqueques;
		cin >> tamañoPala;
		bool imposible = false;
		int contadorVueltas = 0;
	

		for(int j = 0;j<panqueques.size();j++)
		{
			if(panqueques.at(j)== '-')
			{
				if(j>panqueques.size()-tamañoPala)
				{
					imposible = true;
				}else{
					for(int i = 0;i<tamañoPala;i++)
					{
						if(panqueques.at(j+i)=='-')
						{
							panqueques.at(j+i)='+';
						}else{
							panqueques.at(j+i)='-';
						}
					}
				
					contadorVueltas++;
				}
			}
		}
		if(imposible)
		{
			cout << "Case #" << i << ": IMPOSSIBLE"  << endl;
		}else{
			cout << "Case #" << i << ": " << contadorVueltas << endl;
	
		}
		
	}

	
	return 0;
}
