#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t){
        int D, N;
        std::cin >> D >> N;
        std::vector<int> K(N), S(N);
        for (int i=0; i < N; ++i) {
            std::cin >> K[i] >> S[i];
        }
        /* 
        std::cout << "D: " << D << ", N: " << N << std::endl;
        for (int i=0; i < N; ++i) {
            std::cout << "K: " <<  K[i] << ", S: " << S[i] << std::endl;
        }
        //*/

        double min_speed = -1;
        bool have_min_speed = false;
        for (int i=0; i < N; ++i) {
            double cur_time = 1.0 * (D - K[i]) / S[i];
            double cur_speed = 1.0 * D / cur_time;
            if (!have_min_speed || cur_speed < min_speed) {
                min_speed = cur_speed;
                have_min_speed = true;
            }
        }
        std::cout << std::fixed << std::setprecision(7) <<  "Case #" << t << ": " << min_speed << std::endl;

    }

    // std::cout << "Finished!" << std::endl;
    return 0;
}
