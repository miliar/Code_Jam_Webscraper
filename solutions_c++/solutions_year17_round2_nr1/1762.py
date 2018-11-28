
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second

#define MOD (1000000007)
using namespace std;
int k[1005],s[1005];
bool valid(double mid,int n,int d)
{
    bool b=true;
    for(int i=0;i<n;i++)
    {
        if(k[i]*mid < d*(mid-s[i]))
            return false;
    }
    return true;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int cc=1;
    int d,n,t;
    infile>>t;
    while(t--)
    {infile>>d>>n;
    for(int i=0;i<n;i++)
    {
        infile>>k[i]>>s[i];
    }
    double r=10e13,l=1;
    double mid;
    while(r-l>0.0000001)
    {
        mid=(r+l)/2;
       // printf("-%lf %lf %lf\n",mid,r,l);
        if(mid==l || mid==r)
            break;
        if(valid(mid,n,d))
            l=mid;
        else
            r=mid;
        
       // printf("%d %lf %lf\n",r,l,cc);
    }
    //    cout<<l<<endl;
        printf("Case #%d: %lf\n",cc,l);
     outfile<<"Case #"<<cc++<<": "<<l<<endl;
    }
    return 0;
}