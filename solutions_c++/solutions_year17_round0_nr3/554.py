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
//#define max(a,b) ((a)>(b)?:(a):(b))
using namespace std;
long long mx,mn;
map <long long, long long> mp;
set<long long> s;
void solve(long long n,long long k)
{
    mp.clear();
    s.clear();
    mp[n]=1;
    long long temp,cnt;
    s.insert(n);
    while(k>0)
    {
        temp=*(s.rbegin());
        cout<<temp<<endl;
        s.erase(s.find(temp));
        mx=temp/2;
        mn=mx - (temp%2==0?1:0);
        cnt=mp[temp];
        s.insert(mx);
        s.insert(mn);
        mp[mx]+=cnt;
        mp[mn]+=cnt;
        k-=cnt;
    }
    
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,cc=1;
    long long n,k;
    infile>>t;
    while(t--)
    {
        infile>>n>>k;
        solve(n,k);
        outfile<<"Case #"<<cc++<<": "<<mx<<" "<<mn<<endl;
    }
    outfile.close();
    infile.close();

    return 0;
}