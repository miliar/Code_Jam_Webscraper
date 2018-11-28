#include <stdio.h>
#include <iostream>

using namespace std;

int main(void)
{
	int t;
	string input, result;
	string::iterator start, end;
	unsigned long long int j, k, len;

  freopen( "B-large.in", "r", stdin );
  freopen( "B-large.out", "w", stdout );
	cin >> t;

	for(int i = 1; i <= t; i++)
	{
		cin >> input;
		len = input.length();

		for(j = len-1ull; j > 0ull; j--) {
			if(input[j-1ull] > input[j]) {
				for(k = j; k < len && input[k] != '9'; k++)
					input[k] = '9';

				input[j-1ull] = input[j-1ull]-1;
			}
		}

		start = input.begin();

		while((*start) == '0')
			start++;

		end = input.end();

		result.assign(start, end);

		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
