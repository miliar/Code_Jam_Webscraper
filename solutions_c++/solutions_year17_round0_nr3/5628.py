#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


uint64_t minAvailable = 0;
uint64_t maxAvailable = 0;

void findRange(uint64_t numStalls, uint64_t numPersons)
{
    vector<uint64_t> Stalls;
    Stalls.push_back(numStalls);
    make_heap(Stalls.begin(), Stalls.end());

    while(numPersons > 0)
    {
        int availableStalls = Stalls.front();
        pop_heap(Stalls.begin(), Stalls.end());
        Stalls.pop_back();

        if(availableStalls%2 == 0)
        {
           minAvailable = (availableStalls/2) -1;
           maxAvailable = availableStalls/2;

        }
        else
        {
           minAvailable = availableStalls/2;
           maxAvailable = availableStalls/2;
        }

          Stalls.push_back(minAvailable);
          Stalls.push_back(maxAvailable);
        std::push_heap (Stalls.begin(),Stalls.end());

        numPersons--;
    }
}


int main()
{

    std::ifstream in("C-small-2-attempt0.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    int testcases;
    uint64_t numStalls = 0;
    uint64_t numPersons = 0;
    cin>>testcases;
    for(int i = 1 ; i <= testcases; ++i)
    {
        cin>>numStalls>>numPersons;
        findRange(numStalls, numPersons);
        cout<< "Case #"<<i<<": "<<maxAvailable << " " << minAvailable<<endl;
    }

    return 0;
}
