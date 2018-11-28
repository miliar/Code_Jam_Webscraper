
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

double get_max_vel(std::vector<std::pair<double,double>> &horses,
				   const double end) {
	std::vector<double> times;

	std::vector<std::pair<double,double>>::iterator it;
	for (it = horses.begin(); it != horses.end(); it++) {
		times.push_back((end - it->first)/it->second);
	}

	std::sort(times.begin(), times.end());
	if (0 == times.size()) return end;
	return end/times.back();
}


int main() {
	unsigned int T, N;
	std::pair<double,double> horse;
	std::vector<std::pair<double,double>> horses;
	double end;
	std::cout << std::setprecision(7) << std::fixed;	

	std::cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		std::cin >> end;
		std::cin >> N;
		for (unsigned int j = 0; j < N; j++) {
			std::cin >> horse.first;
			std::cin >> horse.second;
			horses.push_back(horse);
		}
		std::cout << "Case #" << i + 1 << ": " <<
			get_max_vel(horses, end) << std::endl;
		horses.clear();
	}
	
	return 0;
}
