
#include <bits/stdc++.h>
#include <algorithm>
//#include <ctype.h>
#include <iostream>
//#include <stdio.h>
using namespace std;

// my tricks to systemmmmm

#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define For(i, a, b) for (long i=(a); i<(b); ++i)
#define D(x) cout << #x " is " << x << endl

//bool idg[55];
//string ans[55];
////int nfig[150005];
//long long data[100005];
//long long mi[100005];
//long long bes[100005][2];



bool tiny(string num)
{
    int l = -1;
    for(int i = 0; i < num.size() - 1; ++i)
    {
        if (num[i] > num[i+1])
        {
            l = i;
            break;
        }
    }
    return (l == -1);
}

string solve(long long value)
{

    if(value == 0) return "";
    if(value < 10 || tiny(std::to_string(value))) return std::to_string(value);

    long long ld = value % 10;
    while(ld>0)
    {
        value--;
        if(tiny(std::to_string(value)))
            return std::to_string(value);
        ld--;
    }

    string ans = "";

    ans = solve(value/10 - 1) + "9";
    return ans;
}



int main(int argc, char *argv[])
{

   int T;
   cin >> T;
   for (int j = 0;j< T; ++j)
   {
       long long t;
       cin >> t;
       cout << "Case #" << std::to_string(j+1) << ": " << solve(t) << std::endl;
   }
   return 0;
}
