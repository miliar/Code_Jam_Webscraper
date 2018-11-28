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
		input >> s;
		
		len = s.length();

		int br = len;

		for (int i = 0; i < len - 1; ++i)
		{
			if (s[i] > s[i + 1])
			{
				br = i;
				while (br > 0 && s[br] == s[br - 1])
					--br;
				break;
			}
		}


		output << "Case #" << t + 1 << ": ";
		cout << "Case #" << t + 1 << ": ";

		if (br > 0)
		{


			for (int i = 0; i < br; ++i)
			{
				output << s[i];
				//cout << s[i];
			}
			if (br < len)
			{

				output << (char)(s[br] - 1);
				//cout << (char)(s[br] - 1);
				for (int i = br + 1; i < len; ++i)
				{
					output << '9';
					//cout << '9';
				}
			}
		}
		else
		{
			if (s[br] != '1')
			{
				output << (char)(s[br] - 1);
				
			}
			for (int i = br + 1; i < len; ++i)
			{
				output << '9';
				//cout << '9';
			}
		}
		output << endl;
		//cout << endl;

		//cout << ans;

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
