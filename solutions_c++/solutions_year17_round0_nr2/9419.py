#include <iostream>
#include <string>

using namespace std;

bool numberCorrect(unsigned long long int number)
{
	bool correct = true;
	int prevdigit = number%10;
	while(number)
	{
		if(number%10 > prevdigit) {
			correct =false;
			break;
		}

		prevdigit = number%10;
		number /= 10;
	}

	return correct;
}

int main()
{
	int T;
	int tc = 1;
	unsigned long long int number;

	cin>>T;
	while(T)
	{
		cin>>number;

		unsigned long long int ans = number;
		unsigned long long int divisor = 1;
		while(!numberCorrect(ans))
		{
			divisor *= 10;
			ans = number - (number%divisor) - 1;
		}

		cout<<"Case #"<<tc<<": "<<ans<<endl;
		tc++;
		T--;
	}
}
