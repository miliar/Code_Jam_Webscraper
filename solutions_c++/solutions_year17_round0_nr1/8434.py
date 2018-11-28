#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

int main()
{
	ofstream outFile("output.out");

	ifstream inFile("A-large.in");



	int t;
	//cin >> t;
	inFile >> t;

	for (int tc = 0; tc < t; tc++)
	{

		int k;
		int count = 0;
		int stat = 1;
		
		vector <int> arr;
		string temp;

		//cin >> temp;
		//cin >> k;
		inFile >> temp;
		inFile >> k;

		for (int i=0; i<temp.length(); i++)
		{
			if (temp[i] == '+')
				arr.push_back(1);
			else
				arr.push_back(-1);
		}

		for (int i=0; i<arr.size(); i++)
		{
			if (arr[i] == -1)
			{
				if (i+k > arr.size())
				{
					break;
				}

				count++;
				for (int j = i; j < i + k; j++)
				{
					arr[j] *= -1;
				}
			}
		}


		stat = 1;
		for (int i=0; i<arr.size(); i++)
		{
			if (arr[i] == -1)
			{
				stat = 0;
				break;
			}
		}



		if (stat == 0)
		{
			//cout << "Case #" << tc+1 << ":" << " " << "IMPOSSIBLE" << endl;
			outFile << "Case #" << tc + 1 << ":" << " " << "IMPOSSIBLE" << endl;
		}
		else
		{
			//cout << "Case #" << tc+1 << ":" << " " << count << endl;
			outFile << "Case #" << tc + 1 << ":" << " " << count << endl;
		}
		
	}

	outFile.close();
	return 0;	
}