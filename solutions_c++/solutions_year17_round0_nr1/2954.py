#include <fstream>
#include <assert.h>
#include <vector>


size_t process(size_t N, std::string sconfig)
{
    std::vector<bool> config;
    for (auto c: sconfig)
        config.push_back(c == '+');

    size_t res = 0;
    for (size_t l = 0; l + N < config.size(); ++l)
    {
        if (!config[l])
        {
            ++res;
            for (size_t k = l; k < l + N; ++k)
                config[k] = !config[k];
        }
    }

    bool r = config[config.size() - N];
    if (!r)
        ++res;

    for (size_t l = 1; l != N; ++l)
        if (config[l + config.size() - N] != r)
            return -1;

    return res;
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_a.txt");
    std::ofstream out("out_a.txt");

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t N;
        std::string configuration;

        in >> configuration >> N;

        size_t res = process(N, configuration);
        out << "Case #" << i + 1 << ": ";

        if (res == -1)
            out << "IMPOSSIBLE";
        else
            out << res;

        out << std::endl;
    }
}
