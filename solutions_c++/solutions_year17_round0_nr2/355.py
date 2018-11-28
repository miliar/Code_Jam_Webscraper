#include <iostream>
#include <algorithm>

#define MAX_N 100

bool is_tidy(int i) {
    int n = 10;
    for (;;) {
	int new_n = i % 10;
	if (new_n > n) return false;
	i /= 10;
	if (i == 0) return true;
	n = new_n;
    }
}

void test(int t) {

    int N;
    std::cin >> N;

    int last_tidy = 0;
    for (int i = 0; i <= N; i++) {
	if (is_tidy(i)) {
	    last_tidy = i;
	}
    }


    std::cout << "Case #" << t + 1 << ": ";

    std::cout << last_tidy;

    std::cout << std::endl;

}

int main(int argc, char **argv) {

    // std::cout << is_tidy(8) << std::endl;
    // std::cout << is_tidy(123) << std::endl;
    // std::cout << is_tidy(555) << std::endl;
    // std::cout << is_tidy(224488) << std::endl;

    // std::cout << is_tidy(20) << std::endl;
    // std::cout << is_tidy(321) << std::endl;
    // std::cout << is_tidy(495) << std::endl;
    // std::cout << is_tidy(99990) << std::endl;


    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++) {
    	test(t);
    }


    return 0;
}
