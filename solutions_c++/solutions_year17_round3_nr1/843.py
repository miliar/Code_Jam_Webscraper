#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <array>
#include <set>
#include <stack>
#include <cmath>

using namespace std;

struct pancake {
	long double radius;
	long double height;
	long double square;
	long double side;
};

template<typename T>
void print_answer(const T& answer) {
  static int case_idx = 1;
  stringstream ss;
  ss.precision(10);
  ss << std::fixed;
  ss << "Case #" << case_idx << ": " << answer << endl;
  cout << ss.str();
  cerr << ss.str();
  ++case_idx;
}

long double process_task() {
	int n, k;
	cin >> n >> k;
	vector<pancake> cakes(n);
	for (int i = 0; i < n; ++i) {
		cin >> cakes[i].radius >> cakes[i].height;
		cakes[i].square = M_PI * cakes[i].radius * cakes[i].radius;
		cakes[i].side = 2.0 * M_PI * cakes[i].radius * cakes[i].height;
	}

	sort(cakes.begin(), cakes.end(), [](const pancake& left, const pancake& right)
	{
		if (left.radius != right.radius) {
			return left.radius > right.radius;
		} else {
			return left.height < right.height;
		}
	});
	long double result = 0.0;
	for (int i = 0; i < n - k + 1; ++i) {
		const auto& refcake = cakes[i];
		vector<pancake> topcakes(cakes.begin() + i + 1, cakes.end());
		sort(topcakes.begin(), topcakes.end(), [](const pancake& left, const pancake& right)
		{
			return left.side > right.side;
		});

		long double curr_sum = refcake.square + refcake.side;
		// cerr << "init_curr sum = " << curr_sum <<endl << refcake.square << " " << refcake.side << endl;
		for (int i = 0; i < (k - 1); ++i) {
			curr_sum += topcakes[i].side;
		}

		result = max(result, curr_sum);
	}

	return result;
}


int main() {
    int task_count = 0;

    cin >> task_count;
    std::cerr << task_count << " <- task_count" << std::endl;

    for (int iter = 0; iter < task_count; ++iter) {
        auto result = process_task();
        print_answer(result);
    }

    return 0;
}