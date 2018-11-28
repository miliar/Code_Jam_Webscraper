#include<iostream>
#include<string>
#include<cstring>
#include<map>
using namespace std;


int main()
{
	long long t = 0;
	long long n = 0;
	long long k = 0;
	long long j = 0;
	long long temp;
	long long tempnum = 0;

	cin >> t;
	for (long long i = 1; i <= t; ++i)
	{
		map<long long, long long> m;
		map<long long, long long>::iterator it;
		map<long long, long long>::iterator lastit;

		cin >> n >> k;

		m.insert(pair<long long, long long>(n, 1));
		for (j = 0; j < k-1; ++j)
		{
			if (m.empty())
				break;

			temp = (m.rbegin())->first;
			tempnum = (m.rbegin())->second;
			if (tempnum != 1)
			{
				if(tempnum < (k - 1 - j))
				{
					lastit = m.end();
					--lastit;
					m.erase(lastit);
				}
				else
				{
					(m.rbegin())->second -= 1;
				}
			}
			else
			{
				lastit = m.end();
				--lastit;
				m.erase(lastit);
			}
			if ((temp % 2) == 0)
			{
				it = m.find(temp / 2);
				if (it != m.end())
				{
					if (tempnum < (k - 1 - j))
					{
						it->second += tempnum;
					}
					else
					{
						it->second += 1;
					}
				}
				else
				{
					if (tempnum < (k - 1 - j))
					{
						m.insert(pair<long long, long long>(temp / 2, tempnum));
					}
					else
					{
						m.insert(pair<long long, long long>(temp / 2, 1));
					}
				}
				it = m.find((temp / 2)-1);
				if (it != m.end())
				{
					if (tempnum < (k - 1 - j))
					{
						it->second += tempnum;
					}
					else
					{
						it->second += 1;
					}
				}
				else
				{

					if (tempnum < (k - 1 - j))
					{
						m.insert(pair<long long, long long>(((temp / 2) - 1), tempnum));
					}
					else
					{
						m.insert(pair<long long, long long>(((temp / 2) - 1), 1));
					}
				}
			}
			else
			{
				it = m.find((temp-1) / 2);
				if (it != m.end())
				{
					if (tempnum < (k - 1 - j))
					{
						it->second += 2 * tempnum;
					}
					else
					{
						it->second += 2;
					}
				}
				else
				{
					if (tempnum < (k - 1 - j))
					{
						m.insert(pair<long long, long long>((temp - 1) / 2, (2 * tempnum)));
					}
					else
					{
						m.insert(pair<long long, long long>((temp - 1) / 2, 2));
					}
				}
			}
			if (tempnum < (k - 1 - j))
			{
				j += (tempnum-1);
			}
		}
		if (j == k - 1)
		{
			temp = (m.rbegin())->first;
			tempnum = (m.rbegin())->second;
			if ((temp % 2) == 0)
			{
				cout << "Case #" << i << ": " << (temp / 2) << " " << ((temp / 2) - 1)<<endl;
			}
			else
			{
				cout << "Case #" << i << ": " << ((temp - 1) / 2) << " " << ((temp - 1) / 2) << endl;
			}
		}
	}
	return 1;
}