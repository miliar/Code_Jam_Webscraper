#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fou("A-large.out");

    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
    {
        double D;
        int N;
        fin>>D>>N;
        double maxTime = 0.0;
        for(int j=0;j<N;j++)
        {
            double K,S;
            fin>>K>>S;
            double time = (D - K)/S;
            if(maxTime < time)
                maxTime = time;
        }
        fou.setf(ios::fixed);
        fou<<"Case #"<<i<<": "<<setprecision(8)<<D/maxTime<<endl;
    }
    return 0;
}
