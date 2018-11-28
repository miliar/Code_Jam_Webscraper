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
#include "boost/graph/adj_list_serialize.hpp"
#include "/home/simon/ClionProjects/CodeJamBasics/Graph.h"
#include "/home/simon/ClionProjects/CodeJamBasics/Helper.h"


// int foo [5]={1,1,1,1,1};
using namespace std;

typedef long long int Lint;
typedef long double Ldouble;


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
        int N, K;
        getline(infile, line);
        std::stringstream Stream1(line);
        Stream1 >> N >> K;
        double U;
        getline(infile, line);
        std::stringstream Stream2(line);
        Stream2 >> U;
        vector<double> vect;
        getline(infile, line);
        std::stringstream Stream3(line);
        for (int j = 0; j < N; j++) {
            double buffer;
            Stream3>> buffer;
            vect.push_back(buffer);
        }
        sort(vect.begin(),vect.end());
        bool check=true;
        int pos=0;
        double sum=0;
        double lowprob=0;
        while(check) {
            sum += vect[pos];
            pos++;
            lowprob=(sum + U) / ((double) pos);
            if (pos < N) {
                if ((sum + U) / ((double) pos) <= vect[pos]) {
                    check = false;
                }
            } else {
                check = false;
            }
        }
        for(int i=0;i<pos;i++){
            vect[i]=lowprob;
        }
        for(int i=0;i<vect.size();i++){
            cout<<vect[i]<<endl;
        }
        double finalprob=1;
        for(int i=0;i<N;i++){
            finalprob*=(vect[i]);
        }

        outfile << "Case #" << caseNr << ": " ;
        outfile << fixed<< setprecision(9)<<finalprob;
        outfile << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}






