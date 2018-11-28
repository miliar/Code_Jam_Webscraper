#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>

class Gap
{
public:
	unsigned long long L;
	unsigned long long R;

	unsigned long long min;
	unsigned long long max;

	unsigned long long left;

	Gap(const unsigned long long length, const unsigned long long left)
		:left(left)
	{
		L = (unsigned long long)floor((float)(length - 1) / 2.0f);
		R = (unsigned long long)ceil((float)(length - 1) / 2.0f);

		if (L < R)
		{
			min = L;
			max = R;
		}
		else
		{
			min = R;
			max = L;
		}
	}

	bool operator <(const Gap &rhs) const
	{
		if (min < rhs.min)
			return true;
		else if (min > rhs.min)
			return false;
		else
		{
			if (max < rhs.max)
				return true;
			else if (max > rhs.max)
				return false;
			else
				return left < rhs.left;
		}
	}
};

int main(int argc, char *argv[])
{
	std::ifstream in("in.txt");
	std::ofstream out("out.txt");

	unsigned int T;
	in >> T;
	for (unsigned int t = 0; t < T; t++)
	{
		unsigned long long N;
		unsigned long long K;
		in >> N >> K;

		std::priority_queue<Gap> gaps;
		gaps.push(Gap(N, 0));

		Gap best = gaps.top();
		for (unsigned int k = 0; k < K; k++)
		{
			best = gaps.top();
			gaps.pop();

			if (best.L != 0)
				gaps.push(Gap(best.L, best.left));
			if (best.R != 0)
				gaps.push(Gap(best.R, best.left + best.L + 1));

		}

		out << "Case #" << t + 1 << ": " << best.max << " " << best.min << std::endl;
//#ifdef _DEBUG
		std::cout << "Case #" << t + 1 << ": " << best.max << " " << best.min << std::endl;
//#endif
	}

	in.close();
	out.close();

	return 0;
}