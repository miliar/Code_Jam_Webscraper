#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int N;

int Solve(string str, int x)
{
	int cnt = 0;
	for(int i=0; i < str.length(); i++)
	{
		if(str[i] == '-')
		{
			if(i+x-1 >= str.length())
				return -1;
			cnt++;
			for(int j=i; j < i+x; j++)
				if(str[j] == '-')
					str[j] = '+';
				else
					str[j] = '-';
		}
	}
	return cnt;
}

int main()
{
	ofstream output;
	output.open("output.txt");
	cin >> N;
	for(int i=0; i < N; i++)
	{
		string str;
		int x;
		cin >> str >> x;
		int y = Solve(str, x);
		output << "Case #" << i+1 << ": ";
		if(y == -1)
			output << "IMPOSSIBLE" << endl;
		else
			output << y << endl;
	}
	output.close();
	return 0;
}
