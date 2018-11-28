#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <cassert>
#include <stack>
#include <string>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

#define DEBUG 10

#define REP(i, a, b) for (int i = a; i < b; i++)
#define REPE(i, a, b) for (int i = a; i <= b; i++)
#define REPD(i, a, b) for (int i = a; i >= b; i--)
#define ll long long
#define vl vector<long long>
#define vll vector<vector<long long>>
#define vi vector<int>
#define vii vector<vector<int>>

#if DEBUG != 1
#define cout outfile
#endif
// void flip(string &s,int eloc,int k)

int main(void)
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ifstream infile("infile");
    ofstream outfile("outfile.txt");
    long long testcases = 1;
    infile >> testcases;
    REPE(testcase, 1, testcases)
    {
        #if DEBUG==1 
        cout<<"*********TESTCASE"<<testcase<<"**********"<<endl;
        #endif
        string s;
        infile>>s;
        int k,slen=s.length(),e,count=0;
        infile>>k;
        e=k-1;
        REPD(i,slen-1,e)
        {
            if(s[i]=='-')
            {
                REPD(j,i,i-k+1)
                {
                    s[j] = (s[j] =='+')? '-':'+';
                };
                count++;
            };
            #if DEBUG==1
            cout<<s<<endl;
            #endif
        };
        bool flag = true;
        REP(i,0,k) if(s[i]=='-') flag = false;
        if(flag)
            cout<<"Case #"<<testcase<<": "<<count<<endl;
        else
            cout<<"Case #"<<testcase<<": IMPOSSIBLE"<<endl;


#if DEBUG == 1
#endif
    }
    return 0;
};