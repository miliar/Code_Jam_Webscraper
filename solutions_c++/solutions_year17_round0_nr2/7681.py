#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>

using namespace std;

int main(){

	ifstream cin("datain.txt");
	ofstream cout("dataout.txt");


	int t, n;
	string s, result;
	cin >> t;

	for (size_t i = 1; i <= t; i++)
	{
		cin >> s;
		n = s.length();

		for (size_t j = n - 1; j > 0; j--)
		{
			if (s[j - 1] > s[j]){
					for (size_t l = j; l < n; l++)
					{
						if (s[l] == '9') {
							break;
						}
						s[l] = '9';
					}
					s[j - 1]--;
			}
		}
		if (s[0] <= '0') s = s.substr(1);
		cout << "Case #" << i << ": " << s << endl;
	}


	return 0;
}