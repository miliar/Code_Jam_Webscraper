
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



int solve(string s, int K, const string& c1, const string& c2)
{
    if(s.length() == K)
    {
        if (s == c1)
        {
            //cout << "see some thing"
            return 1;
        }
        if (s == c2)
            return 0;
        return -1;
    }
    if (s[0] == '+') return solve(s.substr(1), K, c1, c2);
    if (s[s.size() -1] == '+') return solve(s.substr(0,s.size() -1),K,c1,c2);

    string new_s1 = s.substr(K);
    for(int i = K-1; i >= 0; --i)
    {
        new_s1 = (s[i]=='-'? '+': '-') + new_s1;
    }

    int v1 = solve(new_s1,K,c1,c2);

    string new_s2 = s.substr(0,s.size() - K);
    for(int i = 0; i < K; ++i)
    {
        new_s2 = new_s2 + (s[s.size() - K + i]=='-'? '+': '-') ;
    }
    int v2 = solve(new_s2,K,c1,c2);

    if(v1 >= 0 && v2 >= 0)
        return 1 + min(v1,v2);
    if(v1 < 0 && v2 < 0)
        return -1;
    return 1 + max(v1,v2);
}

string rp(char c, int K)
{
    string s = "";
    for(int i = 0; i < K; i++)
    {
        s = s + c;
    }
    return s;
}

int main(int argc, char *argv[])
{
    int T;
       cin >> T;
       for (int j = 0;j< T; ++j)
       {
            string s; int K;
            cin >> s >> K;
            string c1 = rp('-',K);
            string c2 = rp('+', K);
            int ans = solve(s,K,c1,c2);

            if (ans==-1)
                cout << "Case #" << std::to_string(j+1) << ": IMPOSSIBLE"  << std::endl;
            else
                cout << "Case #" << std::to_string(j+1) << ": " << ans << std::endl;

       }
//    vector<unsigned long long> pw2(65,0);
//    pw2[0] = 1;

//    for(int i = 0; i < 63; ++i)
//    {
//        pw2[i+1] = pw2[i] + pw2[i];
//    }
//   int T;
//   cin >> T;
//   for (int j = 0;j< T; ++j)
//   {
//       long long N,K;
//       cin >> N >> K;

//       unsigned long long v1, v2;
//       if (K < N)
//       {

//           unsigned long long p = 0;
//           //int i = 0;
//           v1 = N;
//           v2 = 0;
//           while(K > 0)
//           {
//               K-= pw2[int(p)];
//               v2 = (v1-1) - (v1-1)/2;
//               v1 = (v1-1)/2;
//           }


//          //v1 = N/((unsigned long long)std::pow(2,p));
//          //v2 = N/((unsigned long long)std::pow(2,p-1)) - v1-1;
//       }
//       else
//       {
//           v1 = 0;
//           v2 = 0;
//       }

//       cout << "Case #" << std::to_string(j+1) << ": " << max(v1,v2) << " "  << min(v1, v2) << std::endl;
//   }
   return 0;
}
