#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

typedef unsigned long long uint64;
typedef unsigned int uint32;
typedef uint64 uint;

using namespace std;

template<class T>
print_result(uint n, T res)
{
	stringstream ss;
	uint nres;
	ss << res; ss >> nres;
	cout << "Case #" << n <<": " << nres << endl;
}

int main()
{
	uint T;
	string N;
	uint i,j,k;
	
	cin >> T;
	
	for (i=1; i<=T; ++i)
	{		
		bool flag = true;
		
		cin >> N;
		
		for (j=1; j<N.length(); ++j)
		{
			if (N[j] < N[j-1])
			{
				flag = false;
				break;	
			}		 
		}
		
		if (!flag)
		{
			for (k=j+1; k<N.length(); ++k)
			{
				N[k]='9';
			}
			for (k=j; k>0 && N[k] < N[k-1]; --k)
			{
				N[k] = '9';
				N[k-1]--;
			}
		}
		
		print_result(i, N);
	}	
}

