// Created by Leonardo de Oliveira Ramos

#include <iostream>
#include <string>

using namespace std;

int main ()
{
	int num_of_cases;

	cin >> num_of_cases;

	// cout << num_of_cases << endl;

	for (int i = 0; i < num_of_cases; i++)
	{
		string input_str;

		cin >> input_str;

		int last_bigger_digit = -1;	
		for (int j = (input_str.size() - 1); j > 0; j--)
		{
			if (input_str[j-1] > input_str[j])
			{
				input_str[j-1] = (input_str[j-1]) -1;
				for (int k = j; k < input_str.size(); k++)
					input_str[k] = '9';
			}
		}

		int j = 0;
		while (input_str[j] == '0' && j < input_str.size())
		{
			j++;
		}

		cout << "Case #" << i+1 << ": ";
		while (j < input_str.size())
			cout << input_str[j++];
		cout << endl;

	}
}