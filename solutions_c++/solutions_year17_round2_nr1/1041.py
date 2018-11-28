#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

vector<int> K, S;

int main()
{
    string file_name = "A-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        int N, D;
        f1 >> D >> N;
        K.resize(N);
        S.resize(N);
        for(int i = 0; i < N; ++i)
        {
            f1 >> K[i] >> S[i];
        }
        long double a = -1, b;
        for(int i = 0; i < N; ++i)
        {
            b = (long double)(D-K[i]);
            b /= S[i];
            //cout << b << endl;
            if(b > a)
            {
                a = b;
            }
        }
        long double ans = D;
        ans /= a;
        f2.flags(ios::fixed);
        f2 << setprecision(8) << ans << endl;
    }
    return 0;
}

