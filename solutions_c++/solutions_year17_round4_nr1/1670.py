#include <iostream>
#include <vector>
#include <string>


int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int N, P;
        std::cin >> N >> P;
        std::vector<int> G(N);
        for (int i=0; i < N; ++i) {
            std::cin >> G[i];
        }
        /* 
        std::cout << "N: " << N << ", P: " << P << std::endl;
        std::cout << "G: ";
        for (int i=0; i < G.size(); ++i) {
            std::cout << G[i] << " ";
        }
        std::cout << std::endl;
        */


        std::vector<int> Gmod(4, 0);
        for (int i=0; i < G.size(); ++i) {
            int gModP = G[i] % P;
            Gmod[gModP]++;
        }

        int result = 0;
        result += Gmod[0];
        Gmod[0] = 0;
        // std::cout << "result 0: " << result << std::endl;


        for (int i=1; 2 * i < P ; ++i) {
            int ipair = P - i;
            int minPair = Gmod[i] > Gmod[ipair] ? ipair : i;
            int minVal = Gmod[minPair];
            Gmod[i] -= minVal;
            Gmod[ipair] -= minVal;
            result += minVal;
        }

        // std::cout << "result 1: " << result << std::endl;


        if (P % 2 == 0) {
            int i = P / 2;
            result += Gmod[i] / 2;
            Gmod[i] = Gmod[i] % 2;
        }

        // std::cout << "result 2: " << result << std::endl;

        //Use the left over
        if (P == 2) {
            result += Gmod[1];
        }
        else if (P == 3) {
            for (int i=1; i < 3; ++i) {
                if (Gmod[i] > 0) {
                    result += (Gmod[i]+2) / 3;
                    break;
                }
            }
        }
        else if (P == 4) {
            if (Gmod[2] > 0) {
                int sum13 = Gmod[1] + Gmod[3];
                if (sum13 >= 2) {
                    result += 1;
                    Gmod[2]--;
                    result += (sum13 + 3) / 4;
                }
            }
            else {
                int sum13 = Gmod[1] + Gmod[3];
                result += (sum13 + 3) / 4;
            }
        }
        std::cout << "Case #" << t << ": " << result << std::endl;
    }


    return 0;
}
