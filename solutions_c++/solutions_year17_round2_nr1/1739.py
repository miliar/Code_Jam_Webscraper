#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <iomanip>

using namespace std;

inline double timeneed(long long pos, long long speed, long long end){
    return double(end - pos) / speed;
}

int main()
{
    string inname = "A-large.in";
    string outname = "A-large.out";
    ifstream infile(inname);
    ofstream outfile(outname);
    outfile << std::setprecision(8);
    outfile << std::fixed;
    int T = 0;
    infile >> T;
    int maxpos = 0, maxspeed = 0;
    for(int k = 1; k <= T; k++)
    {
        long long D = 0, N = 0;
        infile >> D >> N;
        double maxtime = 0;
        for(int i = 0; i < N; i++){
            long long pos = 0, speed = 0;
            infile >> pos >> speed;
            double time = timeneed(pos,speed,D);
            if (time > maxtime){
                maxtime = time;
                maxpos = pos;
                maxspeed = speed;
            }
        }
        double speed = double(D * maxspeed) / double(D - maxpos);

        outfile << "Case #" << k << ": " << speed;
        if(k < T)
            outfile << endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
