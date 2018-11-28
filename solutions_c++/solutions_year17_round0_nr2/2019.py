#include <iostream>
#include <cstdint>
using namespace std;

uint64_t r[19], limit;

void break_down(uint64_t n1, int i)
{
	if( n1 > 0 )
	{
		r[i] = n1 % 10;
		break_down(n1 / 10, i + 1);
	}
	else
		limit = i;
}

void chain_reaction(int j)
{
	if(r[j] < r[j + 1] && j >= 0)
	{
		r[j] = 9;
		chain_reaction(j - 1);
	}
}

uint64_t combine(int i)
{
	if(i < limit)
		return combine(i + 1) * 10 + r[i];
	else
		return 0;
}

int main() {
	int t;
	uint64_t n;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cin >> n;
		break_down(n, 0);
		cout << "Case #" << i + 1 << ": ";

		if(limit == 1)
			cout << n << "\n";
		else
		{
			for(int j = 0; j < limit - 1; j++)
			{
				if(r[j] < r[j + 1])
				{
					chain_reaction(j);
					r[j + 1]--;
				}
			}
			if(r[limit - 2] < r[limit - 1])
				r[limit - 1] = r[limit - 2];
			cout << combine(0) << "\n";
		}
	}
	return 0;
}
