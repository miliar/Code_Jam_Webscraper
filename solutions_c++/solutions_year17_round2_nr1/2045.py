#include <iostream>
#include <map>

typedef std::map<double, int> double_int_map;

double calculate_maximum_time_needed(int distance, int number_of_hourse) {
	double_int_map needed_time_of_all_hourses;
	for (int i = 0; i < number_of_hourse; ++i) {
		int start, speed;
		std::cin >> start >> speed;
		needed_time_of_all_hourses[static_cast<double>(distance - start) / speed] = i;
	}
	return needed_time_of_all_hourses.rbegin()->first;
}

double calculate_maximum_speed(int distance, int number_of_hourse) {
	double max_time_needed = calculate_maximum_time_needed(distance, number_of_hourse);
	return static_cast<double>(distance) / max_time_needed;
}

int main(void) {
	int total_test_case;
	std::cin >> total_test_case;
	int count = 0; 
	while (count < total_test_case) {
		int distance, number_of_hourse;
		std::cin >> distance >> number_of_hourse;
		std::cout.precision(6);
		std::cout.setf(std::ios::fixed, std::ios::floatfield);
		std::cout << "Case #" << count + 1 << ": " << calculate_maximum_speed(distance, number_of_hourse) << std::endl;
		++count;
	}
}