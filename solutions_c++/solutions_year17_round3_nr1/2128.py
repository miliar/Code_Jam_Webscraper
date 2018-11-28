//
// Created by Snehil Vishwakarma on 4/30/17.
//

#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <numeric>
#include <iomanip>

using namespace std;

struct compare
{
    bool operator()(const std::pair<long,long> &l, const std::pair<long,long> &r)
    {
        return l.first > r.first;
    }
};

void findmax(vector < pair < long , long  > > dim,vector < double > sides,int j,int K,int N,double sum,double &mx,bool chk)
{
    if(j==N)
        if(K==0)
            if(sum > mx)
                mx = sum;
    if(j<N)
    {
        if(K==0)
        {
            if (sum > mx)
                mx = sum;
        }
        else
        {
            if(chk==false)
                findmax(dim,sides, j + 1, K - 1, N, sum + sides[j] + pow(dim[j].first,2), mx,true);
            else
                findmax(dim,sides, j + 1, K - 1, N, sum + sides[j], mx,chk);
            findmax(dim,sides, j + 1, K, N, sum, mx,chk);
        }
    }
}

int main() {
    int T,N,K,r,h;
    cin>>T;
    double mx,tmx;
    for(int i=0; i<T; ++i)
    {
        cin >> N >> K;
        tmx = 0;
        vector < pair < long , long  > > dim;
        for(int j=0; j<N; j++)
        {
            cin >> r >> h;
            dim.push_back(make_pair(r,h));
        }
        sort(dim.begin(),dim.end(),compare());
        vector < double > sides;
        for(int j=0; j<N; j++)
            sides.push_back(2*dim[j].first*dim[j].second);
        //for(int j=0; j<(N-K+1); j++)
        //{
            mx = 0;
            findmax(dim,sides,0,K,N,0,mx,false);
            mx = M_PI * mx;
            if(mx > tmx)
                tmx = mx;
        //}
        cout << fixed;
        cout << setprecision(9);
        cout << "Case #" << (i+1) << ": " << tmx;
        if(i!=(T-1))
            cout << endl;
    }
    return 0;
}