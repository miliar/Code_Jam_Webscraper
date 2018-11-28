#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

class Cake{
public:
    ull r;
    ull h;
};


int main()
{
    ifstream ifs("A-large.in");
    ofstream ofs("A-large.out");

    int T;
    ifs >> T;


    for(int i=0; i<T; i++)
    {
        cout << i << endl;
        int N, K;
        ifs >> N >> K;

        vector<Cake> cakes(N);
        for(int j=0; j<N; j++)
        {
            ifs >> cakes[j].r >> cakes[j].h;
        }

        sort(cakes.begin(), cakes.end(), [&](Cake &lhs, Cake &rhs){
            return (double)2.0*M_PI*(double)lhs.r*(double)lhs.h >
                   (double)2.0*M_PI*(double)rhs.r*(double)rhs.h;
        });

        double largestSurface = 0;

        for(int j=0; j<N; j++)
        {
            vector<Cake> tmp(K);
            tmp[0] = cakes[j];

            int count = 1;
            int index = 0;
            cout << "c1" << endl;
            for(; count<K; index++)
            {
                if(index!=j)
                {
                    tmp[count] = cakes[index];
                    count++;
                }
            }

            sort(tmp.begin(), tmp.end(), [&](Cake &lhs, Cake &rhs){
                return lhs.r>rhs.r;
            });

            //cout << tmp[0].r << ", " << tmp[0].h << endl;
            double surface = M_PI*(double)tmp[0].r*(double)tmp[0].r + (double)2.0*M_PI*(double)tmp[0].r*(double)tmp[0].h;
            for(int k=1; k<K; k++)
            {
                surface += (double)2.0*M_PI*(double)tmp[k].r*(double)tmp[k].h;
            }

            if(surface>largestSurface)
            {
                largestSurface = surface;
            }
        }

        ofs << fixed << setprecision(20);
        ofs << "Case #" << i+1 << ": " << largestSurface << endl;
    }
}
