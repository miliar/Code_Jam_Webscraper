//Call the program like this:
//g++ -std=c++11 -g -O0 -Wall -Wextra -Werror -Wno-error=unused-parameter -pedantic **.cpp && ./a.out < **-practice.in > **.output

#include <bits/stdc++.h>

#define FOREACH(it,a) for ( auto it=(a).begin();it!=(a).end();++it)
#define FOREACHREV(it,a) for ( auto it=(a).end();it!=(a).begin();++it)
#define FOR(I,A,B) for(size_t I = (A); I < (B); ++I)
#define FORREV(I,A,B) for(int I = (A); I > (B); --I)
#define REP(I,N)   FOR(I,0,N)
#define PRINTALLIN(M,C) cout << #C << ": " << endl; for(auto (M):(C)) cout << (M) << endl;
#define PRINTMAT(MAT, N, M) cout << #MAT << ": " << endl; REP((I),(N)){ REP((J),(M)){ cout << (MAT[I][J]) << " ";} cout << endl;}
#define VECTOSTRING(V) \
    stringstream stringst;\
    for(auto entry : V)\
    {stringst << entry;} \
    string s = stringst.str();

//TAGS

using namespace std;

int main()
{
    uint t;                          //number of test cases
    cin >> t;
    for(uint z = 0; z<t; ++z){
        unsigned long long ull;
        cin >> ull;
        std::stringstream ss;
        ss << ull;
        std::string str = ss.str();
        vector<short> digits;
        for (auto c : str)
        {
            digits.push_back(c - '0');
        }

        FORREV(i,digits.size()-2,-1)
        {
            if (digits[i] > digits[i+1]){
                --digits[i];
                FOR(j,i+1,digits.size())
                    digits[j] = 9;
            }
        }
        while(digits.size()>1 && digits.front()==0)
            digits.erase(digits.begin());

        VECTOSTRING(digits)

        //cout.precision(10);
        cout << "Case #" << z+1 << ": "<< s << endl ;
    }
    return 0;
}
