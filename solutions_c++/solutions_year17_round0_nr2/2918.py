// CodeJump.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <string>
#include <iostream>

#define toDigit(c) (c-'0')


using namespace std;

int max_tidy_number(int N)
{
	string n_string = to_string(N);
	while (N > 0)
	{
		bool tidy = true;
		for (int i = n_string.length() - 1; i > 0; i--)
		{
			char temp = n_string[i];
			int current = atoi(&temp);// (int)n_string[i];
			temp = n_string[i - 1];
			int previus = atoi(&temp); // (int)n_string[i - 1];
			//cout << "n_string[i]: " << current << "  n_string[i-1]: " << previus << endl;
			if (current < previus)
			{

				tidy = false;
				break;
			}
		}
		if (tidy) return N;
		else
		{
			N -= 1;
			n_string = to_string(N);
			//cout << "not tidy " << n_string << endl;
		}
	}
}
int main() {
	int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n.
		cout << "Case #" << i << ": " << max_tidy_number(n) << endl;
	}
	//system("pause");
}

