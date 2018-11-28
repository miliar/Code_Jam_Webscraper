#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
bool cmp (pair<int,int> v1,pair<int,int> v2)
{
    return (v1.first<v2.first);
}
int testcase,test;
void f()
{
    int D,N;
    vector < pair<int,int> > q;
    cin >> D >> N;
    for (int i = 0; i < N; i++)
    {
        int k,s;
        cin >> k >> s;
        q.push_back( make_pair(k,s) );
    }
    sort(q.begin(), q.end());
    double minhour = -1;
    for (int i = 0; i < N; i++)
    {
        double tmp = (double(D) - double(q[i].first)) / double(q[i].second);
        minhour = max(minhour,tmp);
    }
    double res = double(D) / minhour;
    printf("Case #%d: %.6f\n",test, res);
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> testcase;
    for (test = 1; test <= testcase; test++)
        f();
    return 0;
}
