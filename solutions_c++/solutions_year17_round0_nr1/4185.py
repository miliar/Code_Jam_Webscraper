#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	string s;
	int k;
	
	bool ar[1000];

	int ans;
	int len;
	for (int t = 0; t < T; ++t)
	{
		input >> s >> k;

		ans = 0;

		len = s.length();

		for (int i = 0; i < len; ++i)
		{
			if (s[i] == '+')
			{
				ar[i] = 1;
			}
			else
			{
				ar[i] = 0;
			}
		}
		
		for (int i = 0; i <= len - k; ++i)
		{
			if (!ar[i])
			{
				for (int j = 0; j < k; ++j)
				{
					ar[i + j] = !ar[i + j];
				}
				++ans;
			}
		}

		for (int i = len - k + 1; i < len; ++i)
		{
			if (!ar[i])
			{
				ans = -1;
				break;
			}
		}

		output << "Case #" << t + 1 << ": ";
		if (ans == -1)
			output << "IMPOSSIBLE";
		else
			output << ans;
		output << endl;

		//cout << ans;

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
