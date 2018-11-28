#include<iostream>
#include<fstream>
#include<string>
//#include<sstream>
#include<vector>
#include <stdlib.h>     /* atoi */
#include<algorithm>
#include<cassert>
#include<climits>
using namespace std;
#define MYMOD 1000000007
int num_ins(int c){
   int t = c;
   
   return c;
}
int num_ins(int c, int _r, int _c){
   return (_r - c)*(_c - c)*num_ins(c);
}
long long _mul(long long a, long long b){
   a%=MYMOD;
   b%=MYMOD;
   return (a*b)%MYMOD;
}
long long _solve(string s){
   long long ans = 0;
   long long ans_bak = 0;
   ans = s[0] - '0';
   int _r = ans;
   int idx = 0;
   ans_bak = ans;
   for(int i = 1; i < s.length(); ++i){
      ans = ans *10;
      ans_bak = ans_bak * 10;
      char _c = s[i];
      int test_r = _c - '0';
      if(test_r < _r){
          for(int j = i+1; j < s.length(); ++j){
             ans_bak = ans_bak * 10;
          }
          return ans_bak-1;
      }
      else if(test_r > _r){
          ans += test_r;
          _r = test_r;
          idx = i;
          ans_bak = ans;
      }
      else{
          ans += test_r;
      }
   }
   return ans;
}
int main(int argc, char* argv[]){
   ifstream data_in;
   ofstream data_out;
   data_in.open(argv[1]);
   data_out.open(argv[2]);
   int num_c = 0;
   data_in >> num_c;
   
   for(int i = 0; i < num_c;++i){
      long long _r;
      long long ans = 0;
      string s;
      data_in >> s;
      ans = _solve(s);
      data_out<<"Case #"<<(i+1)<<": "<< ans<<endl;
   }
   data_in.close();
   
   data_out.close();
}
