#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream stream;
	stream.open(".//A-large.in");
	ofstream ostream("./A-large.out");

	int T, K;
	stream >> T;

	string input;
	for(int t=0; t<T; ++t)
	{
		int cnt = 0; 
		stream >> input >> K;		
		/*cout << "string : " << input << endl;
		cout << "K : " << K << endl;*/
		

		for (int i = 0; i < input.length(); ++i)
		{
			if (input[i] == '-')
			{
				if (i + K <= input.length())
				{
					++cnt;
					for (int j = i; j < i + K; ++j)
					{
						input[j] = input[j] == '+' ? '-' : '+';
					}
					//cout << "string : " << input << endl;
				}
				

			}
		}


		for (int i = input.length() - K; i < input.length(); ++i)
		{
			if (input[i] == '-')
				cnt = -1;
		}
		
		if (cnt < 0)
			ostream << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		else
			ostream << "Case #" << t + 1 << ": " << cnt << endl;

		
	
		
	}

	stream.close();
	ostream.close();
	return 0;
}