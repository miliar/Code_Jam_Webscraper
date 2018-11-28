#include <fstream>
#include <vector>
#include <functional>

using namespace std;

int main()
{
    ifstream ifs("B-large.in");
    ofstream ofs("B-large.out");

    int T;
    ifs >> T;

    function<unsigned long long(unsigned long long)> solve = [&](unsigned long long N){
        if(N<10)
        {
            return N;
        }
        else
        {
            if(N%10 < (N%100)/10 || N%10 == 0)
            {
                return solve(N/10-1)*10 + 9;
            }
            else
            {
                unsigned long long tmp = solve(N/10);
                if(tmp%10 == 9)
                {
                    return tmp*10 + 9;
                }
                else
                {
                    return tmp*10 + N%10;
                }
            }
        }
    };

    for(int i=0; i<T; i++)
    {
        unsigned long long N;
        ifs >> N;

        ofs << "Case #" << i+1 << ": " << solve(N) << endl;

    }
}
