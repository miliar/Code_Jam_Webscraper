#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>


std::pair<size_t, size_t> process(size_t N, size_t K)
{
    --K;
    std::map<size_t, size_t, std::greater<size_t>> queue = {{ {N, 1} }};
    while (K)
    {
        auto b = queue.begin();
        if (K < b->second)
        {
            K = 0;
        }
        else
        {
            K -= b->second;
            queue[(b->first - 1) / 2] += b->second;
            queue[(b->first - 1) / 2 + (b->first - 1) % 2] += b->second;

            queue.erase(queue.begin());
        }
    }

    auto b = queue.begin();
    return {(b->first - 1) / 2 + (b->first - 1) % 2, (b->first - 1) / 2};
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_c.txt");
    std::ofstream out("out_c.txt");

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t N, K;

        in >> N >> K;

        auto res = process(N, K);
        out << "Case #" << i + 1 << ": " << res.first << " " << res.second << std::endl;
    }
}
