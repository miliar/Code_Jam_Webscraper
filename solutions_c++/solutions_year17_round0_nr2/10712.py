#include <iostream>

using namespace std;

bool checkIfTidy(unsigned long long int number);

int main()
{
    int tests;
    cin >> tests;

    unsigned long long int numbers[tests], j, number;

    for(int i = 0; i < tests; i++)
    {
	cin >> numbers[i];
    }	

    for(int i = 0; i < tests; i++)
    {
	for(j = 0; j < numbers[i]; j++)
	{
	    number = numbers[i] - j;
	    if(checkIfTidy(number) || number == 0)
	    {
		cout << "Case #" << i + 1 << ": " << number << endl;
		break;
	    }    
	}    
    }
}

bool checkIfTidy(unsigned long long int number)
{
    unsigned long long int iterations = 0, curr = 0, prev = 0;
    do
    {
	curr = number % 10;
	if(iterations == 0)
	{
	    if(curr == 0)		
	    {
		return false;
	    }    
	}	
	else
	{
	    if(curr > prev)
	    {
		return false;	
	    }
	}
	prev = curr;
	number = number / 10;
	iterations++;
    }while(number != 0);

    return true;
} 
