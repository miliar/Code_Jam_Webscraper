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
        int N, R, O, Y, G, B, V;
        fin >> N >> R >> O >> Y >> G >> B >> V;
        bool possible=0;
        string output;
        char c1,c2,c3;
        if ((O==0)&&(G==0)&&(V==0))
        {
            if ((R>=Y)&&(R>=B))
            {
                c1='R';
                if (Y>=B)
                {
                    c2='Y';
                    c3='B';
                }
                else
                {
                    c2='B';
                    c3='Y';
                }
            }
            else if ((Y>=R)&&(Y>=B))
            {
                c1='Y';
                if (R>=B)
                {
                    c2='R';
                    c3='B';
                }
                else
                {
                    c2='B';
                    c3='R';
                }
            }
            else
            {
                c1='B';
                if (R>=Y)
                {
                    c2='R';
                    c3='Y';
                }
                else
                {
                    c2='Y';
                    c3='R';
                }
            }
            if (max((max(R,Y)),B)>(N/2))
            {
                possible=0;
            }
            else
            {
                possible=1;
                int d1=max((max(R,Y)),B);
                int d2=min(min(max(R,Y),max(R,B)),max(Y,B));
                int d3=min((min(R,Y)),B);
                for (int j=0; j<(d3-(d1-d2)); ++j)
                {
                    output.push_back(c1);
                    output.push_back(c2);
                    output.push_back(c3);
                }
                for (int j=0; j<(d1-d3); ++j)
                {
                    output.push_back(c1);
                    output.push_back(c2);
                }
                for (int j=0; j<(d1-d2); ++j)
                {
                    output.push_back(c1);
                    output.push_back(c3);
                }
            }
        }
        else
        {
            possible=1;
            output = "OOPS LOL";
        }
        if (possible)
        {
            fout << "Case #" << i+1 << ": " << output << endl;
        }
        else
        {
            fout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
