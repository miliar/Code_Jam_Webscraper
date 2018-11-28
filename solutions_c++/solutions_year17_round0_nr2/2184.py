//#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

ifstream input_file("B-large.in");
ofstream output_file("B-large.out");

std::string smallestTidy(long long N) {
	std::string s = std::to_string(N);
	for (int i = 0; i < s.length() - 1; i++)
	{
		if (s[i] > s[i + 1])
		{
			s[i] -= 1;
			for (int j = i + 1; j < s.length(); j++)
			{
				s[j] = '9';
			}
			for (; i >= 1; i--)
			{
				if (s[i - 1] > s[i])
				{
					s[i - 1] -= 1;
					s[i] = '9';
				}
				else
				{
					break;
				}
			}
			break;
		}
	}
	s.erase(0, min(s.find_first_not_of('0'), s.size() - 1));
	return s;
}

int main(int argc, const char * argv[]) {
	int T;
	input_file >> T;
	for (int t = 0; t < T; t++) {
		long long N;
		input_file >> N;
		output_file << "Case #" << t + 1 << ": " << smallestTidy(N) << endl;
	}
	return 0;
}
