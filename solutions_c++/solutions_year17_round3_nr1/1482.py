#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <iomanip>

struct E {
    int r;
    int h;
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cout<<std::setprecision(12)<<std::fixed;
    int T;
    std::cin>>T;

    for (int testCase=1; testCase<=T; ++testCase) {
        int n, k;
        std::cin>>n>>k;

        std::vector<std::vector<double>> table(n, std::vector<double>(k, 0));
        std::vector<E> data(n);

        for (int i=0; i<n; ++i) std::cin>>data.at(i).r>>data.at(i).h;

        std::sort(data.begin(), data.end(), [](const auto& l, const auto& r){
            if (l.r != r.r) return l.r > r.r;
            return l.h > r.h;
        });

        table.at(0).at(0) = M_PI*data.at(0).r*data.at(0).r + 2*M_PI*data.at(0).r*data.at(0).h;
        for (int i=1; i<n; ++i) {
            table.at(i).at(0) = M_PI*data.at(i).r*data.at(i).r + 2*M_PI*data.at(i).r*data.at(i).h;
            table.at(i).at(0) = std::max(table.at(i-1).at(0), table.at(i).at(0));
        }

        for (int i=1; i<n; ++i) for (int h=1; h<k; ++h) {
            table.at(i).at(h) = table.at(i-1).at(h-1) + 2*M_PI*data.at(i).r*data.at(i).h;
            table.at(i).at(h) = std::max(table.at(i-1).at(h), table.at(i).at(h));
        }

        std::cout<<"Case #"<<testCase<<": "<<table.at(n-1).at(k-1)<<std::endl;
    }

    return 0;
}
