#include <fstream>
#include <vector>
#include <map>
#include <functional>
#include <iomanip>

typedef unsigned long long ull;
typedef long long ll;

using namespace std;

int main()
{
    ifstream ifs("A-large.in");
    ofstream ofs("A-large.out");

    int T;
    ifs >> T;


    for(int i=0; i<T; i++)
    {
        ll D, N;
        ifs >> D >> N;

        ll K[N], S[N];

        for(int j=0; j<N; j++)
        {
            ifs >> K[j] >> S[j];
        }

        double slowest = 0;
        for(int j=0; j<N; j++)
        {
            double t = (double)(D-K[j])/(double)S[j];
            if(t > slowest)
            {
                slowest = t;
            }
        }

        double res = (double)D / slowest;

        ofs << setprecision(20);

        ofs << "Case #" << i+1 << ": " << res << endl;
    }
}
