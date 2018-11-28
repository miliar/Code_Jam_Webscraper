#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main()
{
	int T; cin >> T;
	//remove whitespace
	cin.getline(NULL, NULL);
	for(int c=1;c<=T;++c)
	{
		string input;
		cin >> input;
		//cout << input << endl;
		int K = 0;
		cin >> K;
		int len_s = input.length();

		int count = 0;
		
		for(int i=0;i<=len_s-K;++i)
		{
			if(input[i] == '-')
			{
				for(int j=i;j<i+K;++j)
				{
					input[j] = (input[j] == '-'? '+' : '-');
				}
				count++;
			}
		}

		bool impossible = false;
		for(int i=len_s-1;i>len_s-K;--i)
		{
			if(input[i] == '-')
			{
				cout << "Case #" << c << ": IMPOSSIBLE" << endl;
				impossible = true;
				break;
			}
		}

		if(!impossible)
		cout << "Case #" << c << ": " << count << endl;
	}

	return 0;
}


