#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <mach/mach_time.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <iomanip>
#include <string>
#include <queue>
#include <math.h>
using std::list;
using std::cout;
using std::cin;
using std::vector;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::fstream;
using std::sort;
using std::min;
using std::max;
using std::string;
using std::queue;
using std::fixed;

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<long long> VLL;
#define MAXINT 2147483647

double time()
{
    return 1E-9*mach_absolute_time();
}

ifstream fin("/Users/jlee/Desktop/CodeJam/CodeJamPrep20161BA/SamIn1.txt");
ofstream fout("/Users/jlee/Desktop/CodeJam/CodeJamPrep20161BA/SamOut1.txt");

int main()
{
    int T;
    fin >> T;
    for (int i=0; i<T; ++i)
    {
        int N;
        long long D;
        fin >> D >> N;
        vector<VLL> horses;
        VD times;
        for (int j=0; j<N; ++j)
        {
            long long t1;
            long long t2;
            fin >> t1 >> t2;
            horses.push_back({t1,t2});
            long long temp1 = D-t1;
            double temp2 = (temp1*1.0)/t2;
            times.push_back(temp2);
        }
        double answer;
        double time;
        
        if (N==1)
        {
            long long t=D-horses[0][0];
            time = (t*1.0)/(horses[0][1]);
        }
        else if (N==2)
        {
            long long t1 = D-horses[1][0];
            double time1 = (t1*1.0)/(horses[1][1]);
            if (((time1*horses[0][1])+horses[0][0])>D)
            {
                time = time1;
            }
            else
            {
                long long t2 = D-horses[0][0];
                time = (t2*1.0)/(horses[0][1]);
            }
        }
        else
        {
            double maxx=0;
            for (int k=0; k<N; ++k)
            {
                maxx=max(maxx,times[k]);
            }
            time=maxx;
        }
        answer = (D*1.0)/(time);
        fout.precision(6);
        fout << fixed << "Case #" << i+1 << ": " << answer << endl;
    }
    return 0;
}
