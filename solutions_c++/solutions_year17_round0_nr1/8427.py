#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int count0(string s)
{
	int i = 0, j;
	for(j=0; j<s.length(); j++)
		if(s[j] == 45)
			i++;
	return i;
}

int solve(string S, int K)
{
	string inS = S;
	int steps = 0;
	while(1)
	{
		int c0 = count0(inS);
		if(c0 == 0)
			return steps;
		string s = inS.substr(inS.length()-K, K);
		int cs = count0(s);
		if(c0 == cs)
			if(cs<K)
				return -1;
		size_t pos = inS.find("-");
		s = inS.substr(pos, K);
		if(s.length() < K)
			return -1;
		for(c0 = pos; c0<pos+K; c0++)
		{
			if(inS[c0] == 45)
				inS[c0] = '+';
			else if(inS[c0] == 43)
				inS[c0] = '-';
		}
		steps++;
	}

	return -1;
}

int main(int argc, char* argv[])
{
	string line;
	getline(cin, line);

	istringstream ss(line);

	int T;
	ss >> T;

	for(int i=0; i<T; i++)
	{
		getline(cin, line);
		istringstream iss(line);

		string S;
		int K;
		iss >> S;
		iss >> K;

		cout << "Case #" << i+1 << ": ";
		int c = solve(S, K);
		if(c<0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << c << endl;
	}

	return 0;
}
