#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int main()
{
	ofstream outfile("Hashem.txt");
	int t;
	cin >> t;
	for (int l = 0; l < t; l++)
	{
		outfile << "Case #" << l+1 << ": ";
		map<long long, long long>map1;
		long long n, k, a, b;
		map<long long, long long>::iterator iterator;
		cin >> n;
		map1.insert(make_pair(n, 1));
		cin >> k;
		while (k != 0)
		{
			iterator = map1.end();
			iterator--;
			if (iterator->second >= k)
			{
				a = iterator->first;
				b = a / 2;
				if (a % 2 == 0)
				{
					a /= 2;
					a--;
				}
				else
				{
					a /= 2;
				}
				break;
			}
			else
			{
				k -= iterator->second;
				a = iterator->first;
				b = a / 2;
				if (a % 2 == 0)
				{
					a /= 2;
					a--;
				}
				else
				{
					a /= 2;
				}
				long long u = iterator->second;
				map1.erase(iterator);
				iterator = map1.find(a);
				if (iterator == map1.end()){
					map1.insert(make_pair(a, u));
				}
				else
				{
					iterator->second += u;
				}
				iterator = map1.find(b);
				if (iterator == map1.end()){
					map1.insert(make_pair(b, u));
				}
				else
				{
					iterator->second += u;
				}
			}
		}
		outfile << b << " " << a << endl;
	}
	return 0;
}