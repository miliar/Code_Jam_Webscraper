#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<cmath>
#include<climits>
#include<fstream>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define forv(it,v,type) for(vector<type>::iterator it=v.begin();it!=v.end();it++)

using namespace std;
ifstream fin ("input.in");
ofstream fout ("output.out");

char flip(char t){
    if(t=='+')return '-';
    else return '+';
}
int main(){
int T;
fin >> T;
forn(i,T){
         string s;
         int K;
         fin >> s >> K;
         int c=0;
         bool feasible=true;
         for(int j=0;j<=s.length()-K;j++)
         {
            if(s[j]=='-')
            {
                c++;
                for(int idx = j;idx<j+K;idx++)
                    {
                    s[idx] = flip(s[idx]);
                    }
            }
         }
         for(int j=s.length()-K+1;j<s.length();j++)
         {
          if(s[j]=='-')feasible = false;
         }
         if(feasible)
         {
         fout << "Case #" << i+1 << ": " << c << endl;
         }
         else{ fout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;}
         }
}
