#include <iostream>
#include <fstream>
#include <string>


using namespace std;


bool tidyCheck(string, int);

int main()
{
	ofstream outFile("output.out");
	ifstream inFile("B-small-attempt0.in");


	int t;
	//cin >> t;
	inFile >> t;
	for (int tc = 0; tc < t; tc++)
	{

		long long num;
		//cin >> num;
		inFile >> num;

		long long temp = num;
		string str_num = to_string(temp);
		int len = str_num.length()-1;

		for (int i=num; i>0; i--)
		{
			if (!tidyCheck(str_num, len))
			{
				temp--;
				str_num = to_string(temp);
				len = str_num.length() - 1;
			}
			else
			{
				break;
			}
		}

		cout << "Case #" << tc + 1 << ":" << " " << temp << endl;
		outFile << "Case #" << tc + 1 << ":" << " " << temp << endl;






		//cout << "Case #" << tc+1 << ":" << " " << count << endl;
		//outFile << "Case #" << tc + 1 << ":" << " " << count << endl;
	}

	inFile.close();
	outFile.close();
	return 0;	
}


bool tidyCheck(string str_num, int len)
{
	bool stat = true;

	for (int i=0; i <= len - 1; i++)
	{

		if (str_num[i] > str_num[i+1])
		{
			stat = false;
		}
	}


	return stat;
}