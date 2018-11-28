#include <iostream>
#include <string>
using namespace std;

int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		
		string N;
		cin >> N;
		
		int len = N.size();
		
		if(len == 1)
		{
			cout << N << '\n';
			continue;
		}
		
		for(int k = len -1; k >= 1; k--)
		{
			if(N[k] < N[k -1])
			{
				N[k -1]--;
				for(int j = k; j < len; j++)
					N[j] = '9'; 
			}
		}
		
		bool flag = 0;
		for(int i = 0; i < len; i++)
		{
			if(N[i] != '0' || flag)
			{
				cout << N[i];
				flag = 1;
			}
		}
		cout << endl;
	}
	
	return 0;
}
