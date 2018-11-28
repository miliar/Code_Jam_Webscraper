#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		string N;
		cin >> N;
		int k;
		string prev = "";
		while( prev != N )
		{
			prev = N;
			for ( k = 0; k < N.length() -1; ++k )
			{
				if ( N[k] > N[k+1])
				{
					N[k] = N[k] - 1;
					break;
				}

			}	
			
			for (int j = k + 1; j < N.length(); ++j)
			{
				N[j] = '9';
			}


		}
		for (int l = 0; l < N.length() ; ++l)
		{
			if (N[l] == '0')
			{
				N.erase(l,1);
			}
		}
		cout << "Case #" << i+1 <<": " << N << endl;
	}
	return 0;
}