#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>

using namespace std;

int main(){

	ifstream cin("datain.txt");
	ofstream cout("dataout.txt");

	int t, k, n, res;
	string s, negans = "IMPOSSIBLE", result;
	cin >> t;

	for (size_t i = 1; i <= t ; i++)
	{
		cin >> s >> k;
		n = s.length();
		res = 0;
		//algo
		for (size_t j = 0; j <= n-k; j++)
		{
			if (s[j] == '-'){
				for (size_t h = 0; h < k; h++)
				{
					s[j+h] = (s[j+h] == '+' ? '-' : '+');
				}
				res++;
			}
		}
		result = to_string(res);

		for (size_t h = 0; h < k; h++)
		{
			if (s[n - 1 - h] == '-') {
				result = negans;
				continue;
			}
		}

		//result
		cout << "Case #" << i << ": " << result << endl;
	}


	return 0;
}