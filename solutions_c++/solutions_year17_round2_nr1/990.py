#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <time.h>       /* time */
#include <algorithm>
#include <list>
#include <utility>
#include <stack>
#include <math.h>
#include <iomanip>

using namespace std;


int main() {
    ofstream outfile;
    outfile.open("solution.out");
    std::ifstream infile;
    infile.open("data.in", std::ifstream::in);
    std::string line;
    getline(infile, line);
    std::stringstream lineStream(line);
    int T;
    lineStream >> T;
    for (int caseNr = 1; caseNr <= T; caseNr++) {
        cout << "Solving case number " << caseNr << endl;
        long long int D, N;
        getline(infile, line);
        std::stringstream Stream1(line);
        Stream1 >> D >> N;
        double maxtime=0;
        for (int j = 0; j < N; j++) {
            long long int buffer1, buffer2;
            getline(infile, line);
            std::stringstream Stream2(line);
            Stream2 >> buffer1 >> buffer2;
            double time=((double) D-buffer1)/((double) buffer2);
            if(time>maxtime) maxtime=time;
        }
        outfile << "Case #" << caseNr << ": " ;
        outfile << std::fixed;
        outfile << setprecision(9) << ((double) D)/maxtime;
        outfile << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}


