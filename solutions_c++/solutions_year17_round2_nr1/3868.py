#include <iostream>
#include <iomanip>
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
#include <queue>

using namespace std;

#define DEBUG 0

#define REP(i, a, b) for (int i = a; i < b; i++)
#define REPE(i, a, b) for (int i = a; i <= b; i++)
#define REPD(i, a, b) for (int i = a; i >= b; i--)
#define ll long long
#define vl vector<long long>
#define vll vector<vector<long long>>
#define vi vector<int>
#define vii vector<vector<int>>
#define pii pair<int, int>

#if DEBUG == 0
#define cout outfile
#endif

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
#if DEBUG == 1
        cout << "*********TESTCASE" << testcase << "**********" << endl;
#endif
    
    double d,n;
    infile>>d>>n;
    vector<pair<double,double>> horse(n);
    REP(i,0,n)
    {
        double k,s;
        infile>>k>>s;
        horse[i] = make_pair(k,s);
    }
    sort(horse.begin(),horse.end());
    double mt=0;
    vector<double> time_taken(n);
    REP(i,0,n)
    {
        time_taken[i] = max((d-horse[i].first)/horse[i].second,mt);
        mt = max(mt,time_taken[i]);
    };



    cout << "Case #" << testcase << ": ";
    cout<<setprecision(6);
    cout<<fixed<<d/mt<<endl;


   
#if DEBUG == 1
#endif



#if DEBUG == 1
#endif
    }
    return 0;
};