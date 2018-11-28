#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <fstream>

using namespace std;


int isvalid(vector<string> input, int r, int c){

	map<char, char> chars;

	for (int i = 0; i < r; ++i){
		for (int j = 0; j < c; ++j){

			if (input[i][j] == '?')continue;

			if (i == 0 & j > 0){
				if (input[i][j - 1] != '?' && input[i][j - 1] != input[i][j] && chars.find(input[i][j]) != chars.end())
					return -1;
			}

			if (i > 0 && input[i - 1][j] == input[i][j]){
				if (j > 0 && input[i - 1][j - 1] == input[i][j] && input[i][j - 1] != input[i][j] && input[i][j - 1] != '?')
					return -1;
				if (j > 0 && input[i][j - 1] == input[i][j] && input[i - 1][j - 1] != input[i][j] && input[i - 1][j - 1] != '?')
					return -1;

				if ((j < c - 1) && input[i - 1][j + 1] == input[i][j] && input[i][j + 1] != input[i][j] && input[i][j + 1] != '?')
					return -1;
				if ((j < c - 1) && input[i][j + 1] == input[i][j] && input[i - 1][j + 1] != input[i][j] && input[i - 1][j + 1] != '?')
					return -1;
			}
			
			if ((i > 0 && input[i - 1][j] != '?' && input[i - 1][j] != input[i][j]) || (j > 0 && input[i][j - 1] != '?' && input[i][j - 1] != input[i][j])){
				if ((i > 0 && input[i - 1][j] == input[i][j]) || (j > 0 && input[i][j - 1] == input[i][j])){
					chars[input[i][j]] = input[i][j];
					continue;
				}
				if (!((i > 0 && input[i - 1][j] == '?') || (j > 0 && input[i][j - 1] == '?'))){
					if (chars.find(input[i][j]) != chars.end())
						return -1;

				}
			}

			chars[input[i][j]] = input[i][j];

		}
	}
	return 0;
}

int cake(vector<string>& input, int r, int c, int si, int sj, list<char> chars){

	if (si >= r)
		return isvalid(input, r, c);

	if (input[si][sj] != '?'){
		if (sj == (c-1))
			return cake(input, r, c, si+1, 0, chars);
		else
			return cake(input, r, c, si, sj+1, chars);
	}

	int check = 0;
	for (std::list<char>::iterator it = chars.begin(); it != chars.end(); ++it){
		input[si][sj] = *it;
		if (isvalid(input, r, c) == -1){
			input[si][sj] = '?';
			continue;
		}
		if (sj == (c - 1))
			check = cake(input, r, c, si + 1, 0, chars);
		else
			check = cake(input, r, c, si, sj + 1, chars);
		if (check == 0)
			return 0;
	}
	input[si][sj] = '?';
	return -1;
}

int main(int argc, char**argv)
{
	int t, r, c, ind = 1;
	long long n, res;
	char test[4];

	FILE *fout;
	ifstream myfile;
	myfile.open(argv[1]);
	myfile >> t;

	fopen_s(&fout, "output.txt", "w");

	while (ind <= t){
		myfile >> r >> c;
		string inp;
		list<char> chars;
		vector<string> input;
		for (int i = 0; i < r; ++i){
			myfile >> inp;
			for (int k = 0; k < inp.size(); ++k){
				if (inp[k] != '?')
					chars.push_back(inp[k]);
			}
			input.push_back(inp);
		}

		 chars.unique();

		cake(input, r, c, 0, 0, chars);


		string result = "Case #";
		result.append(to_string(ind));
		result.append(": ");
		for (int i = 0; i < r; ++i){
			result.append("\n");
			result.append(input[i]);
		}

//		result.append(to_string(res));		

		result.append("\n");
		fputs(result.c_str(), fout);

		++ind;
	}

	myfile.close();
	fclose(fout);
	return 0;
}