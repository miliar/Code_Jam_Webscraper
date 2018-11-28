#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>

std::string flip(const std::string &s, const unsigned int k, const unsigned int position);
bool goal(const std::string &s);

int main(int argc, char *argv[])
{
	std::ifstream in("in.txt");
	std::ofstream out("out.txt");

	unsigned int T;
	in >> T;
	for (unsigned int t = 0; t < T; t++)
	{
		std::string s;
		unsigned int k;
		in >> s >> k;

		std::queue<std::pair<std::string, unsigned int>> states;
		states.push(std::pair<std::string, unsigned int>(s, 0));
		std::set<std::string> seen;
		seen.insert(s);

		unsigned int depth = 0;
		bool goalFound = false;
		while (!states.empty() && !goalFound)
		{
			std::string state = states.front().first;
			depth = states.front().second;
			states.pop();
			if (goal(state))
			{
				goalFound = true;
				break;
			}


			for (unsigned int x = 0; x <= state.size() - k; x++)
			{
				std::string newstate = flip(state, k, x);
				if (seen.find(newstate) == seen.cend())
				{
					seen.insert(newstate);
					states.push(std::pair<std::string, unsigned int>(newstate, depth + 1));
				}
			}
		}

		out << "Case #" << t + 1 << ": ";
		if (!goalFound)
			out << "IMPOSSIBLE";
		else
			out << depth;
		out << std::endl;
	}

	in.close();
	out.close();

	return 0;
}

std::string flip(const std::string &s, const unsigned int k, const unsigned int position)
{
	std::string result = s;

	for (unsigned int x = 0; x < k; x++)
		result[position + x] = result[position + x] == '+' ? '-' : '+';

	return result;
}
bool goal(const std::string &s)
{
	return s.find('-') == std::string::npos;
}