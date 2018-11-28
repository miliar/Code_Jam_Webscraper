#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main()
{
	fstream in("in.in"), out("out.txt");
	int T;
	in >> T;

	char c;
	in.get(c);

	for (int t = 1; t <= T; ++t)
	{
		vector<char> num;

		while (in.get(c))
		{
			if (c == '\n')
				break;

			num.push_back(c);
		}

		for (vector<char>::iterator i = num.begin(); i != num.end(); ++i)
		{
			if ((i + 1) != num.end() && *i > *(i + 1))
			{
				*i = ((*i - '0') - 1) + '0';

				for (vector<char>::iterator j = i + 1; j != num.end(); ++j)
					*j = '9';

				while (i != num.begin())
				{
					if (*i < *(i - 1))
					{
						*i = '9';
						*(i - 1) = ((*(i - 1) - '0') - 1) + '0';

						--i;
					}
					else
						break;
				}

				break;
			}
		}

		vector<char>::iterator iter;
		bool zero = true;

		for (iter = num.begin(); iter != num.end(); ++iter)
		{
			if (*iter != '0')
			{
				zero = false;
				break;
			}
		}

		out << "Case #" << t << ": ";

		if (zero)
			out << 0 << "\n";
		else
		{
			for (; iter != num.end(); ++iter)
				out << *iter;

			out << "\n";
		}
	}

	in.close();
	out.close();

	system("pause");
	return 0;
}