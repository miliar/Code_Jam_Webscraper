#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char* argv[])
{
    assert(argc == 3);
    std::ifstream in (argv[1]);
    std::ofstream out (argv[2]);
    int T = 0;
    
    in >> T;

    for (int i = 0; i < T; i++)
    {
        out << "Case #" << i + 1 << ": ";
        unsigned long long N;
        in >> N;
        unsigned long long j = N;
        std::cout << j << std::endl;
        for (j = N; j >= 0; j--)
        {
            std::cout << j << std::endl;
            std::string sorted = std::to_string(j);
            std::sort(sorted.begin(), sorted.end());
            std::string original = std::to_string(j);

            if (original.compare(sorted) == 0)
                break;
        }
        out << j << std::endl;
    }

    return 0;
}

