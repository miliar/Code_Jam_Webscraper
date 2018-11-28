#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;

int main()
{
	int T, currT = 1;
	string number, aux;
	cin >> T;
	while(T--) {
		cin >> number;
		for (int i = number.size() - 1; i >= 0; --i)
		{
			if(i == 0) {
				if(number[i] == '0') {
					number = number.substr(1, number.size());
				}
			} else if( (int)number[i - 1] > (int)number[i] ) {
				number[i - 1] = (char)((int)number[i-1] - 1);
				for (int j = i; j < (int)number.size(); ++j)
				{
					number[j] = '9';
				}
			}
		}

		cout << "Case #" << currT << ": " << number << endl;
		currT++;
	}
	
	return 0;
}