#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int t, counter = 0;
	cin >> t;

	while(t--)
	{
		counter++;
		unsigned long long n;
		cin >> n;

		for(unsigned long long i = n; i >= 0;)
		{		
			int f = 0, d, count = 1;
			unsigned long long m = i;
			unsigned long long save = m % 10;
			m = m / 10;
			while(m > 0)
			{
				count++;
				d = m % 10;
				m = m / 10;
				//cout << m << " " << d << endl;
				if(d <= save)
					save = d;
				else
				{
					//cout << d << " " << save << endl;
					f = 1;
					break;
				}
			}

			if(f != 1)
			{
				cout << "Case #" << counter << ": " << i << endl;
				break;
			}
			else
			{
				save = 9;
				d--;
				i = m*(int)pow(10, count) + (d*(int)pow(10, count-1)) + (save*(int)pow(10, count-2));
				//cout << i << "."<< endl;
				//cout << count-3 << endl;
				for(int j = count-3; j >= 0; j--)
					i += (9*(int)pow(10, j));
				//cout << i << ";"<<endl;
				
				//cout << d << " " << save << " " << count << endl;
			}
		}

	}

	return 0;
}