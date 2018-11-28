//Call the program like this:
//g++ -std=c++11 -g -O0 -Wall -Wextra -Werror -Wno-error=unused-parameter -pedantic **.cpp && ./a.out < **-practice.in > **.output

#include <bits/stdc++.h>

#define FOREACH(it,a) for ( auto it=(a).begin();it!=(a).end();++it)
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define PRINTALLIN(M,C) cout << #C << ": " << endl; for(auto (M):(C)) cout << (M) << endl;
#define PRINTMAT(MAT, N, M) cout << #MAT << ": " << endl; REP((I),(N)){ REP((J),(M)){ cout << (MAT[I][J]) << " ";} cout << endl;}

//TAGS

using namespace std;

int main()
{
    uint t;                          //number of test cases
    cin >> t;
    for(uint z = 0; z<t; ++z){
        int n;
        double r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        //reduction to r,g,b


        if( r > n/2 || b > n/2 || y  > n/2){

            cout << "Case #" << z+1 << ": "<< "IMPOSSIBLE" << endl ;
            continue;
        }
        string solution = "";

        list<pair<double, char>> m;
        m.push_back(make_pair(r, 'R'));
        m.push_back(make_pair(y, 'Y'));
        m.push_back(make_pair(b, 'B'));

        m.sort( [](pair<double, char> first, pair<double, char> second)
            {return first.first<second.first;});
        auto rb = m.rbegin();
            solution.push_back(rb->second);
            (rb->first) -= 0.5;


        while (((int) solution.length()) < n){
            m.sort( [](pair<double, char> first, pair<double, char> second)
                {return first.first<second.first;});
            auto rb = m.rbegin();
            if(rb->second != solution.back()){
                solution.push_back(rb->second);
                --(rb->first);
            }
            else{
                ++rb;
                if(rb->second != solution.back()){
                    solution.push_back(rb->second);
                    --(rb->first);
                }
            }
        }

        //cout.precision(10);
        cout << "Case #" << z+1 << ": "<< solution << endl ;
    }
    return 0;
}
