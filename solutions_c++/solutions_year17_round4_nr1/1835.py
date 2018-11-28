#include <fstream>
#include <assert.h>
#include <vector>
#include <array>


double process(int T, std::istream & in, std::ostream & out)
{
    size_t N, P;
    in >> N >> P;

    size_t res = 0;

    std::array<size_t, 3> rests = {0, 0, 0};
    for (size_t i = 0; i != N; ++i)
    {
        size_t g;
        in >> g;
        if (g % P == 0)
            ++res;
        else
            rests[g % P - 1]++;
    }

    if (P == 2)
    {
        res += rests[0] % 2 + rests[0] / 2;
    }
    else if (P == 3)
    {
        size_t m = std::min(rests[0], rests[1]);
        res += m;
        rests[0] -= m;
        rests[1] -= m;

        res += rests[0] / 3 + rests[1] / 3 + (rests[0] % 3 ? 1 : 0) + (rests[1] % 3 ? 1 : 0);
    }
    else if (P == 4)
    {

    }

    out << "Case #" << T << ": " << res << std::endl;
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
        process(i + 1, in, out);
}
