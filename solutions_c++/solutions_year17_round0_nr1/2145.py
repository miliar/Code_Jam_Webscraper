#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

typedef unsigned long long uint64;
typedef unsigned int uint32;
typedef uint64 uint;


template<class R, class T>
print_result(uint n, R res, T res2)
{
	cout << "Case #" << n << ": " ;
	if (res)
	{
		cout << res2 << endl;
	}
	else
	{
		cout << "IMPOSSIBLE" << endl;
	}
}

int main()
{
	uint T;
	string S, Sref;
	uint K;
	uint i,j,k;
	
	cin >> T;
	
	for (i=1; i<=T; ++i)
	{
		cin >> S >> K;
		
		uint count = 0;
		bool status = true;
		
		for (j=0; j <= S.length()-K; ++j)
		{
			//cout << "S : " << S << endl;
			if (S[j] == '-')
			{
				for (k=j; k<j+K; ++k) 
				{
					S[k] = S[k] == '+' ? '-' : '+';
				}
				++count;
			}
		}
		
		if (S.find('-') != string::npos)
		{
			status = false;
		}
		
		print_result(i, status, count);
	}
}

