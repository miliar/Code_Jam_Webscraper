#include <fstream>
#include <iostream>
#include <sstream>

#define LOG(MSG) std::cout<<MSG<<std::endl;

void testcase(int n, std::fstream &in, std::fstream &out)
{
    std::string pancakes;
    in>>pancakes;
    LOG(pancakes);
    unsigned fLen;
    in>>fLen;
    LOG(fLen);
    unsigned flips = 0;
    bool success = false;
    unsigned pLen = pancakes.size();
    for (unsigned i = 0; i < pLen; ++i)
    {
        if (pancakes[i] == '-' && i + fLen <= pLen)
        {
            flips += 1;
            for (unsigned j = 0; j < fLen; ++j)
                pancakes[j+i] = pancakes[j+i] == '+' ? '-' : '+';
        }
    }

    success = pancakes.find('-') == std::string::npos ? true : false;
    out<<"Case #"<<n<<": ";
    if (success)
        out<<flips<<std::endl;
    else
        out<<"IMPOSSIBLE"<<std::endl;
}

int main()
{
    std::fstream in, out;
    in.open("flipper.in", std::ios::in);
    out.open("flipper.out", std::ios::out);
    int N;
    in>>N;
    LOG("Testcases: "<<N); 
    for (auto n = 1; n <= N; ++n)
        testcase(n, in, out);

    return 0;
}
