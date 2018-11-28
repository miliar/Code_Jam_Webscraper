#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long long ll;


ll f1(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - (k - numRepeats / 2)) / numRepeats;
}

ll f2(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - k) / numRepeats;
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");
	output << std::fixed;
	output << std::setprecision(10);
	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	string s;
	int n, r, o, y, g, b, v;

	vector<pair<long long, long long>> horses;

	for (int t = 0; t < T; ++t)
	{
		input >> n>> r>>o>> y>> g>> b>> v;
		
		output << "Case #" << t + 1 << ": ";
		
		if (r  > y + b
			|| y > r + b
			|| b > r + y) {
			s = "IMPOSSIBLE";
		}
		else {
			s.resize(n);
			if (r >= y && r >= b) {
				s[0] = 'R';
				--r;
			} else if (y >= r && y >= b) {
				s[0] = 'Y';
				--y;
			} else {
				s[0] = 'B';
				--b;
			}
			for (int i = 1; i < n; ++i){
				if (r >= y && r >= b) {
					if (s[i - 1] == 'R'){
						if (y>b){
							--y;
							s[i] = 'Y';
						}
						else {
							--b;
							s[i] = 'B';
						}
					} else {
						s[i] = 'R';
						--r;
					}
					
				}
				else if (y >= r && y >= b) {
					if (s[i - 1] == 'Y'){
						if (r>b){
							--r;
							s[i] = 'R';
						}
						else {
							--b;
							s[i] = 'B';
						}
					}
					else {
						s[i] = 'Y';
						--y;
					}
				}
				else {
					if (s[i - 1] == 'B'){
						if (y>r){
							--y;
							s[i] = 'Y';
						}
						else {
							--r;
							s[i] = 'R';
						}
					}
					else {
						s[i] = 'B';
						--b;
					}
				}
			}

			if (s[0] == s[n - 1]){
				char tmp = s[n-2];
				s[n-2] = s[n - 1];
				s[n - 1] = tmp;
			}

			for (int i = 1; i < n; ++i){
				if (s[i] == s[i - 1])
				{
					cout << "cyka";
				}
			}
			if (s[0] == s[n - 1])
				cout << "cyka";
		}
		

		output << s << endl;
		



	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
