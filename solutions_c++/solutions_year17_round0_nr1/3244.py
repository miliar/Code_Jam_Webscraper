#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <list>
#include <set>


size_t groupHeight(const std::string& str)
{
	size_t height = 1;

	size_t nPos = str.find("+-", 0);
	while (nPos != std::string::npos)
	{
		height++;
		nPos = str.find("+-", nPos + 1);
	}

	nPos = str.find("-+", 0);
	while (nPos != std::string::npos)
	{
		height++;
		nPos = str.find("-+", nPos + 1);
	}

	return height;
}


size_t bfs(std::string state, std::set<std::string>& pathsChecked, size_t k, size_t cur = 0)
{
	size_t s = state.size() - k + 1;
	size_t height = groupHeight(state);
	std::list<std::string> possibleChildren;

	if (height == 1)
	{
		if (state.find('-') == std::string::npos)
		{
			return cur;
		}
	}

	for (size_t i = 0; i < s; i++)
	{
		std::string newstate = state;
		size_t end = i + k;
		for (size_t j = i; j < end; j++)
		{
			switch (newstate[j])
			{
			case '+':
				newstate[j] = '-';
				break;
			case '-':
				newstate[j] = '+';
				break;
			}
		}
		size_t newHeight = groupHeight(newstate);
		if ((newHeight <= height || newHeight == 1 || height == 1) && pathsChecked.find(newstate) == pathsChecked.end())
		{
			if (newHeight == 1 && newstate.find('-') == std::string::npos)
			{
				return cur + 1;
			}
			else
			{
				possibleChildren.push_back(newstate);
			}
			pathsChecked.insert(newstate);
		}
	}
	size_t bestPath = -1;
	for each(const std::string& newstate in possibleChildren)
	{
		size_t path = bfs(newstate, pathsChecked, k, cur + 1);
		if (path < bestPath)
			bestPath = path;
	}
	return bestPath;
}


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	unsigned int numCases = 0;
	in >> numCases;
	for (unsigned int i = 1; i <= numCases; i++)
	{
		out << "Case #" << i << ": ";

		std::string state;
		size_t k;

		in >> state >> k;

		std::set<std::string> pathsChecked;
		pathsChecked.insert(state);

		size_t path = bfs(state, pathsChecked, k);

		if (path == -1)
		{
			out << "IMPOSSIBLE" << std::endl;
		}
		else
		{
			out << path << std::endl;
		}
	}

	return 0;
}


