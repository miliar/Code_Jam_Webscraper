#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <iomanip>

using namespace std;

double solve(int N, int K, vector<double>& R, vector<double>& H);

int main(int argc, char** argv)
{
    ifstream file(argv[1]);
    ofstream output(argv[2]);
    srand(time(NULL));

    if(!file)
        return -1;

    int T = 0;

    file >> T;

    for(int i = 0 ; i < T ; i++)
    {
        int N, K;

        file >> N >> K;

        vector<double> R, H;
        double Ri, Hi;

        for (int j = 0 ; j < N ; j++)
        {
            file >> Ri >> Hi;
            R.push_back(Ri);
            H.push_back(Hi);
        }
        
        double area = solve(N, K, R, H);

        output << "Case #" << setprecision(24) << i+1 << ": " << area << endl;
    }

    file.close();
    output.close();

    return 0;
}

double solve(int N, int K, vector<double>& R, vector<double>& H)
{
    double maxVal = 0;

    vector<double> RH;

    for (int i = 0 ; i < R.size() ; i++)
    {
        RH.push_back(R[i]*H[i]);
    }

    for (int i = 0 ; i < R.size() ; i++)
    {
        double val = R[i]*R[i];
        vector<double> copyRH = RH;
        double tmpRH = RH[i];
        val += RH[i]*2;
        copyRH[i] = 0;

        sort(copyRH.begin(), copyRH.end());
        reverse(copyRH.begin(), copyRH.end());

        for (int j = 0 ; j < K-1 ; j++)
        {
            val += 2*copyRH[j];
        }

        if (val > maxVal)
            maxVal = val;
    }

    return maxVal * M_PI;


}