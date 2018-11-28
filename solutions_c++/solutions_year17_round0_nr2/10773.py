#include <iostream>

using namespace std;

int main(){
	int num;
	int min;
	int temp;
	int digit;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		int number;
		cin >> number;
		temp = number;
		min = temp % 10;
		temp = temp / 10;
		while (temp >0)
		{
			if (temp > 0)
			{
				digit = temp % 10;
				temp = temp / 10;
				if (digit > min || (digit == 0 && min == 1))
				{
					temp = number - 1;
					number--;
					min = temp % 10;
					temp = temp / 10;
				}
				else
				{
					min = digit;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << number << endl;

		
	}
}