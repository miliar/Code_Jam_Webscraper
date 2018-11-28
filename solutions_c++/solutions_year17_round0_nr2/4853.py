#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() 
{

	int T;
	cin >> T;

	for(int t=1;t<=T;t++) 
	{
		string tmpN;
		cin >> tmpN;
		vector<char> N(tmpN.begin(), tmpN.end());
		
		int lenN = N.size();
		for(int i=0; i<lenN; i++) 
		{
			N[i] -= '0';
		}

		for(int i=1; i<lenN; i++)
		{
			if(N[i] >= N[i-1])
			{
				continue;
			}

			N[i-1]--;
			for(int j=i; j<lenN; j++)
			{
				N[j] = 9;
			}

			i = 0;
		}

		cout << "Case #" << t << ": ";

		bool skip = true;
		for(int i=0; i<lenN; i++)
		{
			if(skip && N[i] == 0)
			{
				continue;
			}
			skip = false;

			cout << (int)N[i];
		}

		cout << endl;
	}

	return 0;
}
