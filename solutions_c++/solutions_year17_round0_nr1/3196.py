#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int i;
	cin >> i;
	string cakes;
	int c=0;
	while (cin >> cakes >> i)
	{
		int f=0;
		++c;
		for (int j=0; j<=cakes.size()-i; ++j)
		{
			if (cakes[j] == '+')
				continue;
			for (int k=0; k<i; ++k)
				cakes[j+k]=cakes[j+k]=='+'?'-':'+';
			++f;
		}
		cout << "Case #" << c << ": ";
		if (all_of(begin(cakes), end(cakes), [](char c){return c=='+';}))
			cout << f << endl;
		else
			cout << "IMPOSSIBLE\n";
	}
}
