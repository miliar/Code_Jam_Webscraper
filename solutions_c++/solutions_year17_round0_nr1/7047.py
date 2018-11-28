#include <iostream>
#include <string>
using namespace std;

class PancakeBuffer
{
public:
	PancakeBuffer(int len) : b_(new char[len / 8u + 1u]()), len_(len) {}

	bool operator[](int i)
	{
		if (i >= len_) return false;
		return b_[i / 8u] & (1u<<(i%8));
	}

	void setDigit(int i, bool v)
	{
		if (v)
		{
			b_[i / 8u] |= (1u << (i % 8u));
		}
		else
		{
			b_[i / 8u] &= ~(1u << (i % 8u));
		}
	}

	~PancakeBuffer() { delete[] b_; }

private:
	char* b_;
	int len_;
};

int main()
{
	int t;
	cin >> t; cin.ignore();

	PancakeBuffer pb(1000); // Large test case <= 1000

	for (int i = 1; i <= t; i++)
	{
		// Each flip makes three changes, consecutively. This leaves three posibilities:
		//  --- => +++ Resolve 3 bad
		//  --+ => ++- Resolve 1 bad (total)
		//  -++ => +-- Create 1 bad
		//  +++ => --- Create 3 bad
		// This will always be an odd number introduced/resolved, so there cannot be an even number of bad cakes
		//  I suspect there cannot be a non-modulo3 number, but I cannot back it up with reason in the amount of effort I'm giving this tonight.
		unsigned int nBad = 0u;
		char c = ' ';
		unsigned int pbi = 0u;
		while (true)
		{
			c = cin.get();
			if (c == ' ') break;
			pb.setDigit(pbi++, c == '+');
			nBad += c == '-';
		}
		int spatulaSize = 0;
		cin >> spatulaSize; cin.ignore();

		// Sweep left to right, setting them positive on the left side as you go.
		// Cases:
		// 0 +++ skip
		// 1 ++- attempt to flip +2
		// 2 -++ flip, repeat
		// 3 +-+ attempt to flip +1
		// 4 +-- attempt to flip +1
		// 5 -+- flip +0
		// 6 --+ flip +0
		// 7 --- flip +0

		unsigned int nFlips = 0u;
		// DEBUG
		//for (int k = 0; k < pbi; k++) cout << pb[k]; cout << endl;
		// END DEBUG
		for (unsigned int j = 0u; j <= pbi-spatulaSize; j++)
		{
			if (!pb[j])
			{
				for (unsigned int k = 0u; k < spatulaSize; k++)
				{
					pb.setDigit(j + k, !pb[j + k]); nBad -= (pb[j + k] * 2u - 1u);
				}

				// DEBUG
				//for (int k = 0; k < pbi; k++) cout << pb[k]; cout << endl;
				// END DEBUG
				nFlips++;
			}
		}

		if (nBad == 0)
		{
			cout << "Case #" << i << ": " << nFlips << endl;
		}
		else
		{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}