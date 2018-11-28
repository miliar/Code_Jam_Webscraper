#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N,K;
		cin >> N >> K;
		vector<int> list;
		list.push_back(N);
		int c;
		for (int x = 0; x < K; ++x)
		{	
			if (N > 0)
			{
				if (N % 2 == 0)
				{	
					list.push_back(N/2 - 1);
					list.push_back(N/2);
				}

				else
				{
					list.push_back(N/2);
					list.push_back(N/2);
				}
			}
			
			list.erase(max_element(list.begin(), list.end()));
			N = *max_element(list.begin(), list.end()) ;
		}

		cout << "Case #" << i+1 <<": " << list[list.size()-1] << " " << list[list.size()-2] << endl;
	}

	return 0;
}
