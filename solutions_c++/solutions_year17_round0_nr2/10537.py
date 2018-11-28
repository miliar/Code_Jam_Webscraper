#include <iostream>
#include <fstream>
using namespace std;

bool is_tidy(unsigned long long int n)
{
	bool ans = true;
	while(n > 0)
	{
		int last = n % 10;
		int before_last = (n/10) % 10;
		
		if(last < before_last)
		{
			ans = false;
		}
		
		n /= 10;
	}
	return ans;
}

int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("B-small.txt");
	int T;
	cin>>T;
	unsigned long long int numbers[T];
	
	int i = 0;
	
	while(i < T)
	{
		cin>>numbers[i];
		i++;
	}
	
	for(int i = 0; i < T; i++)
	{
		bool found = true;
		while(numbers[i] > 0 && found)
		{
			if(is_tidy(numbers[i]))
			{
				found = false;
				cout<<"Case #"<<i+1<<": "<<numbers[i]<<endl;
			}	
			numbers[i]--;
		}
	}
}
