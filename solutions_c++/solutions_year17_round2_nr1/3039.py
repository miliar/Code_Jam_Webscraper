/*input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <algorithm>
#include <limits>

int main()
{
	int T, n, flip_ct;
	T = 1;
	std::cin >> n;
	
	// Max Size
	int max_arr_size = 1001;
	while (T <= n)
	{
		int N;
		double D, max_time, c_time, Ki, Si;
		
		std::cin >> D;
		std::cin >> N;
		max_time = 0;

		for (int i = 0; i < N; i++) {
			std::cin >> Ki;
			std::cin >> Si;

			c_time = (D-Ki)/Si;
			if (c_time > max_time) {
				max_time = c_time;
			}
		}

		double min_speed = D/max_time;
		//std::cout << "max_size: " << Arr[N].max_size() << "\n";
		std::cout << "Case #" << std::to_string(T++) << ": " << std::to_string(min_speed) << '\n';
	}
}