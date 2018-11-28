//Call the program like this:
//g++ -std=c++11 -g -O0 -Wall -Wextra -Werror -Wno-error=unused-parameter -pedantic **.cpp && ./a.out < **-practice.in > **.output

#include <bits/stdc++.h>

#define FOREACH(it,a) for ( auto it=(a).begin();it!=(a).end();++it)
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define PRINTALLIN(M,C) cout << #C << ": " << endl; for(auto (M):(C)) cout << (M) << endl;
#define PRINTMAT(MAT, N, M) cout << #MAT << ": " << endl; REP((I),(N)){ REP((J),(M)){ cout << (MAT[I][J]) << " ";} cout << endl;}
//numeric_limits<long double>::max()

//TAGS

using namespace std;

long double area(long double r, long double h){
    return (r)*r*M_PI + h;
}


int main()
{
    uint t;                          //number of test cases
    cin >> t;
    for(uint z = 0; z<t; ++z){
        long double solution = 0;
        int n, k;
        cin >> n >> k;
        vector<pair<double, double>> pancakes;
        double maxr = 0;
        for(int j = 0; j<n ; ++j){
            double r, h;
            cin >> r >> h;
            h = 2*h*r*M_PI;
            pancakes.push_back(make_pair(r, h));
            if(r> maxr)
                maxr = r;
        }
        sort(pancakes.begin(), pancakes.end(),
             [](pair<double, double> a, pair<double, double> b){
            if(a.second == b.second)
                return a.first > b.first;
            return a.second > b.second;
        });
        //sum up the k largest heights
        auto e = pancakes.begin();
        REP(i, k)
                ++e;
        vector<pair<double, double>> kcakes(pancakes.begin(), e);
        long double hsum = 0.;
        --e;
        double minh = e->second;
        double maxkr = 0;
        FOREACH(it,kcakes){
            hsum += it->second;
            if (it->first > maxkr)
                maxkr = it->first;
        }
        solution = area(maxkr,hsum);
        if(maxkr != maxr){

            sort(pancakes.begin(), pancakes.end(),
                 [](pair<double, double> a, pair<double, double> b){
                if(a.first == b.first)
                    return a.second > b.second;
                return a.first > b.first;
            });
            auto it = pancakes.begin();
            while(it->first > maxkr){
                long double alternsol = area(it->first, (hsum-minh+it->second));
                if(alternsol > solution)
                    solution = alternsol;
                ++it;
            }

        }
        std::cout << std::fixed << std::setprecision(10);
        cout << "Case #" << z+1 << ": "<< solution << endl ;
    }
    return 0;
}
