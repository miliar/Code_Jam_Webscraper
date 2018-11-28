#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		string num;
		bool change = false;
		cin >> num;

		if (num.length() == 1)
		{
			cout << "Case #" << t << ": " << num << '\n';
			continue;
		}

		for (auto it = num.begin() + 1; it != num.end(); ++it)
		{
			char &prev = *(it - 1);
			char &curr = *(it);

			if (curr < prev)
			{
				if (!change)
				{
					prev -= 1;
					change = true;
				}
				curr = '9';
			}
		}

		int z;
		for (z = 0; num[z] == '0' and z < num.length(); ++z);
		num = string(num.begin() + z, num.end());

		for (auto it = num.rbegin() + 1; it != num.rend(); ++it)
		{
			char &prev = *(it - 1);
			char &curr = *(it);

			if (prev < curr or prev == '0') {
				prev = '9';
				if (curr == '0')
					curr = '9';
				else
					curr -= 1;
			}
		}

		for (z = 0; num[z] == '0' and z < num.length(); ++z);
		num = string(num.begin() + z, num.end());


		cout << "Case #" << t << ": " << num << '\n';
	}

	return 0;
}
