#include <bits/stdc++.h>

using namespace std;



char pocz, last;

int N;
int R, O, Y, G, B, V;





int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	cout.precision(10);

	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		cin>>N;		
		cin>>R>>O>>Y>>G>>B>>V;
		last = '0';
		cout<<"Case #"<<t<<": ";
		int maks = max(R, max(Y, B));

		if(maks == R)
			pocz = 'R';
		else
			if( maks == Y)
				pocz = 'Y';
			else
				pocz = 'B';

		if(pocz == 'R')
		{
			
			if(R-- > Y + B)
			{
				cout<<"IMPOSSIBLE\n";
				continue;
			}

		}
		if(pocz == 'Y')
		{
			
			if(Y-- > R + B)
			{
				cout<<"IMPOSSIBLE\n";
				continue;
			}



		}
		if(pocz == 'B')
		{
			
			if(B-- > Y + R)
			{
				cout<<"IMPOSSIBLE\n";
				continue;
			}

		}


		cout<<pocz;

		last = pocz;
		for (int i = 1; i < N; ++i)
		{
			if(last == 'R')
			{
				if(Y ==  B)
				{
					if( pocz == 'Y')
					{
						cout<<'Y';
						last = 'Y';
						Y--;
					}
					else
					{
						cout<<'B';
						last = 'B';
						B--;	
					}
				}
			
			else
				if( Y > B)
				{
					cout<<'Y';
					last = 'Y';
					Y--;
				}
				else
				{
					cout<<'B';
					last = 'B';
					B--;	
				}			
			}
			else
			if(last == 'B')
			{
				if(Y ==  R)
				{
					if( pocz == 'Y')
					{
						cout<<'Y';
						last = 'Y';
						Y--;
					}
					else
					{
						cout<<'R';
						last = 'R';
						R--;	
					}
				}
			
			else
				if( Y > R)
				{
					cout<<'Y';
					last = 'Y';
					Y--;
				}
				else
				{
					cout<<'R';
					last = 'R';
					R--;	
				}				
			}
			else
			if(last == 'Y')
			{
				if(R ==  B)
				{
					if( pocz == 'R')
					{
						cout<<'R';
						last = 'R';
						R--;
					}
					else
					{
						cout<<'B';
						last = 'B';
						B--;	
					}
				}
			
			else
				if( R > B)
				{
					cout<<'R';
					last = 'R';
					R--;
				}
				else
				{
					cout<<'B';
					last = 'B';
					B--;	
				}			
			}
 
		}
		
		cout<<"\n";



	}


	return 0;
}