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

bool sortcol( const vector<int>& v1,
             const vector<int>& v2 ) {
    return v1[0] < v2[0];
}

int countswitches(vector<VI>& times)
{
    int count=0;
    for (int j=1; j<times.size(); ++j)
    {
        count+=(times[j][2]!=times[j-1][2]);
    }
    count+=(times[times.size()-1][2]!=times[0][2]);
    return count;
}

int main()
{
    int T;
    fin >> T;
    for (int i=0; i<T; ++i)
    {
        int cam, jamie;
        fin >> cam >> jamie;
        vector<VI> times;
        int camtot=0,jamietot=0;
        for (int j=0; j<cam; ++j)
        {
            int s1,s2;
            fin >> s1 >> s2;
            VI temp={s1,s2,0};
            times.push_back(temp);
            camtot+=s2-s1;
        }
        for (int j=0; j<jamie; ++j)
        {
            int s1,s2;
            fin >> s1 >> s2;
            VI temp={s1,s2,1};
            times.push_back(temp);
            jamietot+=s2-s1;
        }
        sort(times.begin(),times.end(),sortcol);
        int switches=0;
        int curstate=times[0][2];
        bool init=(camtot>jamietot);
        VI caminter;
        VI jamieinter;
        VI camadd;
        VI jamieadd;
        for (int j=1; j<(cam+jamie+1); ++j)
        {
            if (j!=(cam+jamie))
            {
                switches+=(times[j][2]!=times[j-1][2]);
                if (times[j][2]==curstate)
                {
                    if (curstate==0)
                    {
                        camtot+=times[j][0]-times[j-1][1];
                        camadd.push_back(times[j][0]-times[j-1][1]);
                    }
                    else
                    {
                        jamietot+=times[j][0]-times[j-1][1];
                        jamieadd.push_back(times[j][0]-times[j-1][1]);
                    }
                }
                else
                {
                    if (camtot>jamietot)
                    {
                        int t1=camtot-jamietot;
                        int t2=times[j][0]-times[j-1][1];
                        if (t2<t1)
                        {
                            jamietot+=t2;
                            jamieinter.push_back(t2);
                        }
                        else
                        {
                            camtot+=floor((t2-t1)/2);
                            caminter.push_back(floor((t2-t1)/2));
                            jamietot+=t2-floor((t2-t1)/2);
                            jamieinter.push_back(t2-floor((t2-t1)/2));
                        }
                    }
                    else
                    {
                        int t1=jamietot-camtot;
                        int t2=times[j][0]-times[j-1][1];
                        if (t2<t1)
                        {
                            camtot+=t2;
                            caminter.push_back(t2);
                        }
                        else
                        {
                            jamietot+=floor((t2-t1)/2);
                            jamieinter.push_back(floor((t2-t1)/2));
                            camtot+=t2-floor((t2-t1)/2);
                            caminter.push_back(t2-floor((t2-t1)/2));
                        }
                    }
                }
                curstate=times[j][2];
            }
            else
            {
                switches+=(times[0][2]!=times[times.size()-1][2]);
                if (times[0][2]==curstate)
                {
                    if (curstate==0)
                    {
                        camtot+=times[0][0]+1440-times[times.size()-1][1];
                        camadd.push_back(times[0][0]+1440-times[times.size()-1][1]);
                    }
                    else
                    {
                        jamietot+=times[0][0]+1440-times[times.size()-1][1];
                        jamieadd.push_back(times[0][0]+1440-times[times.size()-1][1]);
                    }
                }
                else
                {
                    if (camtot>jamietot)
                    {
                        int t1=camtot-jamietot;
                        int t2=times[0][0]+1440-times[times.size()-1][1];
                        if (t2<t1)
                        {
                            jamietot+=t2;
                            jamieinter.push_back(t2);
                        }
                        else
                        {
                            camtot+=floor((t2-t1)/2);
                            caminter.push_back(floor((t2-t1)/2));
                            jamietot+=t2-floor((t2-t1)/2);
                            jamieinter.push_back(t2-floor((t2-t1)/2));
                        }
                    }
                    else
                    {
                        int t1=jamietot-camtot;
                        int t2=times[0][0]+1440-times[times.size()-1][1];
                        if (t2<t1)
                        {
                            camtot+=t2;
                            caminter.push_back(t2);
                        }
                        else
                        {
                            jamietot+=floor((t2-t1)/2);
                            jamieinter.push_back(floor((t2-t1)/2));
                            camtot+=t2-floor((t2-t1)/2);
                            caminter.push_back(t2-floor((t2-t1)/2));
                        }
                    }
                }
            }
        }
        sort(caminter.begin(),caminter.end());
        sort(jamieinter.begin(),jamieinter.end());
        sort(camadd.begin(),camadd.end());
        sort(jamieadd.begin(),jamieadd.end());
        if (jamietot<720)
        {
            int cur=caminter.size()-1;
            while ((jamietot<720)&&(cur>=0))
            {
                jamietot+=caminter[cur];
                //switches+=2;
                cur--;
            }
        }
        else if (camtot < 720)
        {
            int cur=jamieinter.size()-1;
            while ((camtot<720)&&(cur>=0))
            {
                camtot+=jamieinter[cur];
                //switches+=2;
                cur--;
            }
        }
        if (jamietot<720)
        {
            int cur=camadd.size()-1;
            while ((jamietot<720))
            {
                jamietot+=camadd[cur];
                switches+=2;
                cur--;
            }
        }
        else if (camtot<720)
        {
            int cur=jamieadd.size()-1;
            while ((camtot<720))
            {
                camtot+=jamieadd[cur];
                switches+=2;
                cur--;
            }
        }
        fout << "Case #" << i+1 << ": " << switches << endl; //<< " " << camtot << " " << jamietot << endl;
    }
    return 0;
}
