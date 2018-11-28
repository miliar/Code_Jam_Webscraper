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
    Helper help;
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
        vector<Lint> radii;
        vector<Lint> heights;
        vector<pair<Lint, Lint> > both;
        for (int j = 0; j < N; j++) {
            Lint buffer1, buffer2;
            getline(infile, line);
            std::stringstream Stream2(line);
            Stream2 >> buffer1 >> buffer2;
            radii.push_back(buffer1);
            heights.push_back(buffer2);
            both.push_back(make_pair(buffer1, buffer2));
        }
        sort(both.begin(),both.end());
        //for(int i=0; i<both.size();i++){
        //    cout<<both[i].first<<"\t"<<both[i].second<<endl;
        //}
        double maxSurface=0;
        vector<double> area;
        for(int j=0;j<N;j++){
            area.push_back(2*M_PI*((double) both[j].first)*((double) both[j].second));
        }
        for(int i=K-1;i<N;i++){
            Lint cutoff=both[i].first;
            double surface=(M_PI*((double) both[i].first)*((double) both[i].first)+2*M_PI*((double) both[i].first)*((double) both[i].second));
            vector<double> sort_area(area.begin(),area.begin()+i);
            sort(sort_area.begin(),sort_area.end());
            for(int j=0;j<K-1;j++){
                surface+=sort_area[sort_area.size()-1-j];
            }
            if(surface>maxSurface) maxSurface=surface;
        }


        outfile << "Case #" << caseNr << ": " ;
        outfile << fixed << setprecision(9) <<maxSurface;
        outfile << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}






