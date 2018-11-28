#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <set>
#include <algorithm>
#include <memory>
using namespace std;

struct test_result
{
	uint64_t max;
	uint64_t min;
};

struct empty_info
{
	uint64_t m_position;
	uint64_t m_empty_count_left;
	uint64_t m_empty_count_right;

	empty_info(uint64_t position, uint64_t empty_count_left, uint64_t empty_count_right)
		: m_position(position),
		m_empty_count_left(empty_count_left),
		m_empty_count_right(empty_count_right)
	{
	}

	uint64_t less_min_distance() const
	{
		return std::min(m_empty_count_left, m_empty_count_right);
	}

	uint64_t more_min_distance() const
	{
		return std::max(m_empty_count_left, m_empty_count_right);
	}

	bool operator<(const empty_info& other) const
	{
		if (less_min_distance() < other.less_min_distance())
			return true;
		
		if (less_min_distance() > other.less_min_distance())
			return false;

		if (more_min_distance() < other.more_min_distance())
			return true;

		if (more_min_distance() > other.more_min_distance())
			return false;

		return m_position < other.m_position;
	}

	bool operator>(const empty_info& other) const
	{
		if (less_min_distance() > other.less_min_distance())
			return true;

		if (less_min_distance() < other.less_min_distance())
			return false;

		if (more_min_distance() > other.more_min_distance())
			return true;

		if (more_min_distance() < other.more_min_distance())
			return false;

		return m_position < other.m_position;
	}
};

test_result run_test(int n, int k)
{
	set<uint64_t> occupied_stalls;

	occupied_stalls.insert(0);
	occupied_stalls.insert(n + 1);

	unique_ptr<empty_info> best_place;

	for (int i = 0; i < k; i++)
	{
		set<uint64_t>::const_iterator occupied_iter = occupied_stalls.begin();
		uint64_t left_position = *occupied_iter;
		uint64_t right_position = 0;
		best_place = nullptr;

		while (true)
		{
			occupied_iter++;
			if (occupied_iter == occupied_stalls.end())
				break;

			right_position = *occupied_iter;

			int64_t distance = right_position - left_position;
			if (distance > 1) // 1 means one stall is next to the other, so there is no empty stall between
			{
				uint64_t mid_point = (left_position + right_position) / 2;
				empty_info empty(mid_point, mid_point - left_position - 1, right_position - mid_point - 1);

				if (best_place == nullptr)
					best_place = make_unique<empty_info>(empty);
				else if (empty > *best_place)
					best_place = make_unique<empty_info>(empty);
			}

			left_position = right_position;
		}

		//cout << "best place: pos=" << best_place->m_position
		//	<< ", min: " << best_place->less_min_distance()
		//	<< ", max: " << best_place->more_min_distance()
		//	<< endl;

		occupied_stalls.insert(best_place->m_position);
	}

	test_result result;
	result.min = best_place->less_min_distance();
	result.max = best_place->more_min_distance();

	return result;
}

int main()
{
	ifstream is("input.txt");
	int test_cases = 0;
	is >> test_cases;
	for (int i = 0; i < test_cases; i++)
	{
		int N;
		int K;
		is >> N;
		is >> K;
		test_result result = run_test(N, K);
		cout << "Case #" << (i + 1) << ": " << result.max << " " << result.min << endl;
	}

	return 0;
}