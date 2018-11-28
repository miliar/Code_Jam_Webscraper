#include <fstream>
#include <iostream>

using namespace std;

int main(void)
{
	ifstream in("C-large.in");
	ofstream out("C-large.out");
	
	int t;
	in >> t;
	for(int index = 0; index < t; index++)
	{
		long long int N, K;
		in >> N >> K;
		
		int counter_gruppo = 1;
		long long int x = 1;
		for(;;)
		{
			if(K <= x)
			{
				break;
			}
			else
			{
				K -= x;
				x *= 2;
				counter_gruppo++;
			}
		}
		
		long long int a, b, counter_a, counter_b;
		a = N;
		counter_a = 1;
		counter_b = 0;
		for(int i = 1; i < counter_gruppo; i++)
		{
			if(counter_b == 0)
			{
				if(a % 2 == 0)
				{
					a = a / 2;
					b = a - 1;
					counter_b = counter_a;
				}
				else
				{
					a = (a-1) / 2;
					counter_a *= 2;
				}
			}
			else
			{
				if(a % 2 == 0)
				{
					a = a / 2;
					b = a - 1;
					counter_b = counter_a + 2*counter_b;
				}
				else
				{
					a = (a-1) / 2;
					b = a - 1;
					counter_a = 2*counter_a + counter_b;
				}
			}
		}
		
		if(counter_a >= K)
		{
			if(a % 2 == 0)
			{
				out << "Case #" << index+1 << ": " << (a/2) << " " << (a/2)-1 << endl;
			}
			else
			{
				out << "Case #" << index+1 << ": " << (a-1)/2 << " " << (a-1)/2 << endl;
			}
		}
		else
		{
			if(b % 2 == 0)
			{
				out << "Case #" << index+1 << ": " << (b/2) << " " << (b/2)-1 << endl;
			}
			else
			{
				out << "Case #" << index+1 << ": " << (b-1)/2 << " " << (b-1)/2 << endl;
			}
		}
	}
	
	return 0;
}
