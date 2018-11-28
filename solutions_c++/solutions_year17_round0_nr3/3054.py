#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

void run();

int main()
{
	long T;
	cin >> T;

	for (int c = 1; c <= T; ++c)
	{
		cout << "Case #" << c << ": ";
		run();
	}
}

void run()
{
	unsigned long long N;
	cin >> N;

	unsigned long long K;
	cin >> K;
	
	std::map<unsigned long long, unsigned long long> block_counts;
	std::set<unsigned long long> block_sizes;
	block_sizes.insert(N);
	block_counts[N] = 1;

	unsigned long long newLeftBlock;
	unsigned long long newRightBlock;
	while (K > 0)
	{
		unsigned long long largest = *(block_sizes.rbegin());
		unsigned long long largest_count = block_counts[largest];
		block_sizes.erase(largest);

		newLeftBlock = (largest - 1) / 2;
		newRightBlock = newLeftBlock + ((largest - 1) % 2);

		if (K <= largest_count)
			break;

		K -= largest_count;

		block_sizes.insert(newLeftBlock);
		block_sizes.insert(newRightBlock);
		block_counts[newLeftBlock] += largest_count;
		block_counts[newRightBlock] += largest_count;
	}

	cout << newRightBlock << " " << newLeftBlock << endl;
}