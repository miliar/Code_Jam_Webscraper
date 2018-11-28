#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int i;
	cin >> i;
	string num;
	int c=0;
	while (cin >> num)
	{
		++c;
		while (true)
		{
			auto i = adjacent_find(begin(num), end(num), [](auto c1, auto c2){return c2 < c1;});
			if (i==end(num))
			{
				cout << "Case #" << c << ": " << num << endl;
				break;
			}
			--*i;
			fill(next(i), end(num), '9');
			if (num[0] == '0')
				num.erase(begin(num));
		}
	}
}
