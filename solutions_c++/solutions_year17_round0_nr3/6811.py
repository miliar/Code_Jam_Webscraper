#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C1.txt", "r", stdin);
	freopen ("myfile.txt","w",stdout);
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		vector<int> spaces;
		int N;
		int K;
		cin >> N >> K;
		int max;
		int min;
		int chosenSpace = N;
		for(int j = 0; j < K; j++)
		{
			chosenSpace = chosenSpace - 1;
			if(chosenSpace % 2 == 0)
			{
				max = chosenSpace / 2;
				min = chosenSpace / 2;
				spaces.push_back(max);
				spaces.push_back(min);
			}
			else
			{
				max = (chosenSpace+1) / 2;
				min = (chosenSpace-1) / 2;
				spaces.push_back(max);
				spaces.push_back(min);				
			}
			
			sort(spaces.begin(), spaces.end());
			chosenSpace = spaces.back();
			spaces.pop_back();
		}
		cout << "Case #" << i << ": " << max << " " << min << endl;
	}
	return 0;
}
