#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    std::ifstream in("B-large.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    uint64_t num = 10e18;
    bool isfound = false;
    int testcases;
    cin>>testcases;
    for(int i = 1 ; i <= testcases; ++i)
    {

        cin>>num;
        while(num > 0)
        {
            uint64_t x = num;
            //uint64_t x = num;
            int digit = 10;
            int numDigit = 0;
            isfound = true;
            while(x > 0)
            {
                int d = x - (x/10) * 10;
                numDigit++;
                if(digit - d > -1)
                    digit = d;
                else
                {
                    isfound = false;
                    while(numDigit > 1)
                    {
                        x = x * 10;
                        numDigit--;
                    }
                    num = x;
                    break;
                }
                x = x / 10;

            }
            if(isfound)
            {
                cout<< "Case #"<<i<<": "<<num<<endl;
                break;
            }
            num--;
        }
    }


    return 0;
}
