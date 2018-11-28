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
char flip(char c){
   if(c == '+'){
      return '-';
   }
   else{
      return '+';
   }
}
long long _solve(string& s, int _count){
   long long ans = 0;
   int _size = s.length();
   bool _flip = false;   
   for(int i = 0; i <= _size-_count; ++i){
      char _c = s[i];
      if(_c == '-'){
         ++ans;
         //cout<<i<<": "<<_c<<endl;
         for(int j = i +1; j-i <= (_count - 1); ++j){
            s[j] = flip(s[j]);
            //cout<<j<<": "<<s[j]<<endl;
            
         }
      }
   }
   for(int i = (_size-_count)+1; i < _size; ++i){
      char _c = s[i];
      if(_c == '-'){
         return -1;
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
      string s;
      string _imp = "IMPOSSIBLE";
      int _count = 1;
      data_in >> s;
      data_in >> _count;
      //cout<<s<<endl;
      //cout<<_count<<endl;
      long long ans = 0;
      ans = _solve(s, _count); 
      //ans = -1;
      if(ans >= 0){
         data_out<<"Case #"<<(i+1)<<": "<< ans<<endl;
      }
      else{
         data_out<<"Case #"<<(i+1)<<": "<<_imp<<endl;
      }
   }
   data_in.close();
   
   data_out.close();
}
