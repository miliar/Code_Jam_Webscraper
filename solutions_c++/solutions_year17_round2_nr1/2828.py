#include <iostream>
#include <iomanip>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 0; t < T; t ++) {
        double D;
        std::cin >> D;
        int N;
        std::cin >> N;

        double total_time = 0;
        for (int i = 0; i < N; i ++) {
            double Ki, Si;
            std::cin >> Ki;
            std::cin >> Si;

            double time = (D - Ki) / Si;
            if (total_time < time) total_time = time;
        }
        double answer = D / total_time;

        std::cout << "Case #" << (t + 1) << ": " << std::fixed
                  << std::setprecision(6) << answer << std::endl;
    }
}
