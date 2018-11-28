#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <iomanip>

using namespace std;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<_b;++i)
#define ROF(i,b,a) for(int _a=(a),i=(b);i>_a;--i)
#define FORI(i,a,b) for(auto _b=(b),i=(a);i!=_b;++i)
#define ROFI(i,b,a) for(auto _a=(a),i=(b);i!=_a;--i)

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i;
    string col,colp;

    FOR(i,0,numCase)
    {
        long long D = 0;
        int N = 0;
        int b [10] = {};
        fin >> D >> N;
        double ans = 0;
        long long K;
        long long Kmin;
        double ti = 0;
        double S;
        int Smin = INT_MAX;
        for(int j = 0 ; j < N ;j++){
            fin >> K >> S;
            if(double((D-K)/S)>ti) ti =(double(D-K)/S);
        }
        ans = D/ti;

        fout << "Case #" << (i + 1) << ": "<<setprecision(15)<<ans<<endl;


    }
    fin.close();
    fout.close();
    return 0;
}
