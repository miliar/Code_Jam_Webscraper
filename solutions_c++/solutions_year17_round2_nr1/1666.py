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
        long double slowTime = 0;
        int n;
        long double d;
        cin >> d >> n;
        for(int j = 0; j<n ; ++j){
            long double k, s, time;
            cin >> k >> s;
            time = (d-k)/s;
            if (time > slowTime)
                slowTime = time;
        }
        cout.precision(10);
        cout << "Case #" << z+1 << ": "<< d/slowTime << endl ;
    }
    return 0;
}
