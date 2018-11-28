#include <iostream>
#include <fstream>
#include <string>

bool tidy(const std::string &s);
std::string prev(std::string s);

int main(int argc, char *argv[])
{
	std::ifstream in("in.txt");
	std::ofstream out("out.txt");

	unsigned int T;
	in >> T;
	for (unsigned int t = 0; t < T; t++)
	{
		std::string s;
		in >> s;

		while (!tidy(s))
			s = prev(s);

		out << "Case #" << t + 1 << ": " << s << std::endl;
	}

	in.close();
	out.close();

	return 0;
}

bool tidy(const std::string &s)
{
	for (unsigned int x = 0; x < s.size() - 1; x++)
	{
		if (s[x] > s[x + 1])
			return false;
	}
	return true;
}
std::string prev(std::string s)
{
	unsigned int x;
	for (x = s.size() - 1; x > 0; x--)
	{
		if (s[x] > s[x - 1])
		{
			s[x]--;
			break;
		}
		else // Borrow from next place
		{
			s[x] = '9';
		}
	}
	if (x == 0)
	{
		if (s[x] > '1')
			s[x]--;
		else
			s.erase(s.begin());
	}

	return s;
}