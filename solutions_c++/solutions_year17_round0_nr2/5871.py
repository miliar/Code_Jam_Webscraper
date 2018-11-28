#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


long long tidy(long long n){
	string s = to_string(n);
	int len = s.length();

	int i = 0;
	for (; i < len-1; ++i){
		if (s[i] > s[i+1]){
			int k = i;
			while(k > 0 && s[k-1] == s[k]){
				--k;
			}
			s[k] = s[k] - 1;
			for (int j = k + 1; j < len; ++j)
				s[j] = '9';
			break;
		}
	}

	return stoll(s);
}

int main(int argc, char**argv)
{
	int t, ind = 1;
	long long n, res;
	string s, input;
	char test[4];

	FILE *fout;

	ifstream myfile;
	myfile.open(argv[1]);

	myfile >> t;

	fopen_s(&fout, "output.txt", "w");

	while (ind <= t){
		myfile >> input;
		cout << input << endl;
		n = stoll(input);

		if (n < 10)
			res = n;
		else
			res = tidy(n);

		string result = "Case #";
		result.append(to_string(ind));
		result.append(": ");

		result.append(to_string(res));

		result.append("\n");
		fputs(result.c_str(), fout);

		++ind;
	}

	myfile.close();
	fclose(fout);
	return 0;
}