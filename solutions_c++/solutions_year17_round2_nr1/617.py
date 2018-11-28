#include <fstream>
#include <assert.h>
#include <vector>


double process(size_t D, auto ks)
{
    double max_time = 0;
    for (auto p: ks)
        max_time = std::max(max_time, double(D - p.first) / p.second);

    return D / max_time;
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_a.txt");
    std::ofstream out("out_a.txt");

    out.setf(std::ios_base::fixed);
    out.precision(10);

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t D, N;

        in >> D >> N;

        std::vector<std::pair<size_t, size_t>> ks(N);
        for (size_t k = 0; k != N; ++k)
            in >> ks[k].first >> ks[k].second;

        auto res = process(D, ks);
        out << "Case #" << i + 1 << ": " << res << std::endl;
    }
}
