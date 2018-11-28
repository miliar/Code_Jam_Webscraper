#include <iostream>
#include <vector>

using namespace std;

vector<int> vectorize(long long unsigned int tidy)
{
	long long unsigned int thisTidy = tidy;
	vector<int> tidyVector;

	
	while (thisTidy > 0)
	{
		tidyVector.insert(tidyVector.begin(), thisTidy % 10);
		thisTidy /= 10;
	}
	return tidyVector;
}

int main()
{
	int T;
	cin >> T;
	vector<long long unsigned int> tidies(T);
	for (int i = 0; i < T; i++)
		cin >> tidies[i];
	
	for (int k = 0; k < T; k++)
	{
		vector<int> tidyVector = vectorize(tidies[k]);	
		for (size_t i = 1; i < tidyVector.size(); )
		{
			if (tidyVector[i] >= tidyVector[i-1])
			{
				i++;
			}
			else
			{
				tidyVector[i - 1] -= 1;
				for (size_t j = i; j < tidyVector.size(); j++)
				{
					tidyVector[j] = 9;
				}
				i = 0;
			}
		}
		
		cout << "Case #" << k + 1 << ": ";
		for (size_t i = 0; i < tidyVector.size(); i++)
		{
			if (tidyVector[i] != 0)
				cout << tidyVector[i];
		}
		cout << endl;
	}
	
}
