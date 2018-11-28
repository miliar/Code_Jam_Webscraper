#include <iostream>
#include <cstdint>
#include <algorithm>
#include <iomanip>
#include <vector>

struct Horse {
    uint64_t pos;
    uint64_t speed;
};

int main() {
    int T;

    std::ios_base::sync_with_stdio(false);
    std::cout<<std::setprecision(9)<<std::fixed;
    std::cin>>T;

    for (int testCase=1; testCase<=T; ++testCase) {
        uint64_t D, N;
        std::vector<Horse> data;

        std::cin>>D>>N;
        data.resize(N);
        for (int i=0; i<N; ++i) std::cin>>data.at(i).pos>>data.at(i).speed;

        int worst = 0;
        for (int i=1; i<N; ++i)
            if ((D-data.at(i).pos)*data.at(worst).speed > (D-data.at(worst).pos)*data.at(i).speed)
                worst = i;

        double time = (D-data.at(worst).pos)/(double)data.at(worst).speed;
        double ans  = D/time;

        std::cout<<"Case #"<<testCase<<": "<<ans<<std::endl;
    }

    return 0;
}
