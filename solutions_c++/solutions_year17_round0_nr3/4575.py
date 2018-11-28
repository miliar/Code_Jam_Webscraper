#include <iostream>
#include <vector>
#include <string>
#include <istream>
#include <queue>


int main() {
	int n;
	std::cin >> n;

	for (int i = 0; i < n; ++i) {
		std::priority_queue<int> segments;
		int num_baths, num_people;
		std::cin >> num_baths >> num_people;
		segments.push(num_baths);

		int max, min;

		for (int j = 0; j < num_people; ++j) {
			int segment = segments.top();
			segments.pop();

			max = segment / 2;
			min = (segment-1) / 2;

			segments.push(min);
			segments.push(max);
		}

		std::cout << "Case #" << i+1 << ": " << max << ' ' << min << '\n';
	}

	return 0;
}