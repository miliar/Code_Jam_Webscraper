#include <iostream>
#include <string>
#include <vector>

using namespace std;


int flips(string s, int k){
	int count = 0;
	int len = s.length();

	int i = 0;
	for (; i <= len - k; ++i){
		if (s[i] == '-'){
			++count;
			for (int j = i; j - i + 1 <= k; ++j){
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
	}
	for (int j = i; j < len; ++j){
		if (s[j] == '-')
			return -1;
	}
	return count;
}

int main(int argc, char**argv)
{
	int t,k,ind = 1,res;
	string s, input;
	char c[1005];

	FILE *fin, *fout;
	fopen_s(&fin, argv[1], "r");
	fgets(c, 1005, fin);
	s = c;
	t = stoi(c);

	fopen_s(&fout, "output.txt", "w");

	while (ind <= t){
		fgets(c, 1010, fin);
		input = c;
		size_t pos = input.find(" ");
		s = input.substr(0, pos);
		k = stoi(input.substr(pos + 1));

		res = flips(s, k);

		string result = "Case #";
		result.append(to_string(ind));
		result.append(": ");
		if (res == -1)
			result.append("IMPOSSIBLE");
		else
			result.append(to_string(res));

		result.append("\n");
		fputs(result.c_str(), fout);

		++ind;
	}

	fclose(fin);
	fclose(fout);
	return 0;
}