
#include <bits/stdc++.h>
#include <algorithm>
//#include <ctype.h>
#include <iostream>
#include <cmath>
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





int main(int argc, char *argv[])
{

    vector<unsigned long long> pw2(65,0);
    pw2[0] = 1;

    for(int i = 0; i < 63; ++i)
    {
        pw2[i+1] = pw2[i] + pw2[i];
    }
   int T;
   cin >> T;
   for (int j = 0;j< T; ++j)
   {
       long long N,K;
       cin >> N >> K;

       long long v1, v2;
       if (K < N)
       {

           long long p = 0;
           //int i = 0;
           v1 = N;
           //v2 = 0;
           while(K > pw2[int(p)])
           {
               K-= pw2[int(p)];

               ++p;
           }

           v1 = N/pw2[p];
           v2 = v1 - 1;
            //long long tmp = N + 1 - pw2[p];
           long long spn = v1 * pw2[p] + pw2[p] - N - 1;
           long long spl = pw2[p] - spn;

           if (K <= spl)
           {
               v2 = (v1 -1) - (v1-1)/2;
               v1 = (v1-1)/2;
           }
           else
           {
               v1 = (v2 -1) - (v2-1)/2;
               v2 = (v2-1)/2;
           }
          //v1 = N/((unsigned long long)std::pow(2,p));
          //v2 = N/((unsigned long long)std::pow(2,p-1)) - v1-1;
       }
       else
       {
           v1 = 0;
           v2 = 0;
       }

       cout << "Case #" << std::to_string(j+1) << ": " << max(v1,v2) << " "  << min(v1, v2) << std::endl;
   }
   return 0;
}
