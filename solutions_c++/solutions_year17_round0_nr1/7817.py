#include <fstream>
#include <string>
#include <vector>

int solve(const std::string& str, const size_t k)
{
	std::vector<bool> arr;

	for (auto ch: str)
	{
		if ('+' == ch)
		{
			arr.push_back(true);
		}
		else
		{
			arr.push_back(false);
		}
	}

	int res = 0;
	for (size_t i = 0; i < arr.size(); ++i)
	{
		if (!arr[i])
		{
			for (size_t j = i; j < i + k; ++j)
			{
				if (arr.size() == j)
				{
					res = -1;
					break;
				}
				arr[j] = !arr[j];
			}
			if (res == -1) 
			{
				break;
			}
			++res;
		}
	}
	return res;
}

void main()
{
	std::ifstream in("d:\\GoogleCodeJam2017\\Qualification\\input.txt");
	std::ofstream out("d:\\GoogleCodeJam2017\\Qualification\\output.txt");

	size_t count = 0;
	in >> count;
	if (0 > count)
	{
		count = 0;
	}

	size_t number;
	for (size_t i = 0; i < count && !in.eof(); ++i)
	{
		std::string str;
		in >> str;
		size_t k;
		in >> k;

		const int res = solve(str, k);

		out << "Case #" << i + 1 << ": ";
		if (0 <= res)
		{
			out << res;
		}
		else
		{
			out << "IMPOSSIBLE";
		}
		out << std::endl;
	}

	in.close();
	out.close();
}