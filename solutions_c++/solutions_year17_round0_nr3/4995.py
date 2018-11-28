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
        long int n, k;
        cin >> n >> k;
        --k;
        long int largerHalf = 0;
        long int smallerHalf = 0;
        long int val = 0;

        long int evenK = 1;
        while (evenK <= k){
            evenK <<= 1;
            ++evenK;
        }
        evenK >>= 1;

        long int lenStallRows = (n - evenK)/(evenK + 1);
        long int leftovers = (n - evenK)%(evenK + 1);

        val = lenStallRows -1;

        if(leftovers > (k - evenK)){
            ++val;
        }

        largerHalf = val/2;
        smallerHalf = val/2;
        if(val%2==1)
            ++largerHalf;

        cout << "Case #" << z+1 << ": "<< largerHalf << " " << smallerHalf << endl ;
    }
    return 0;
}
