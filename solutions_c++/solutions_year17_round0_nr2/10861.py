#include <iostream>
#include <sstream>
using namespace std;

bool tidy(int N)
{
	bool res = true;
	stringstream ss;
	ss << N;
	for(unsigned int i=0; i<ss.str().length()-1; i++)
	{
		if(ss.str()[i] > ss.str()[i+1])
		{
			res = false;
			break;
		}
	}
	return res;
}

int main()
{
	int T,N;
	stringstream ss;

	cin >> T;
	for(int i=1; i<=T; i++)
	{
		cin >> N;
		for(int k=N; k>=1; k--)
		{
			if(tidy(k))
			{
				ss << "Case #" << i << ": " << k << "\n";
				break;
			}
		}
	}

	cout << ss.str();

	return 0;
}
