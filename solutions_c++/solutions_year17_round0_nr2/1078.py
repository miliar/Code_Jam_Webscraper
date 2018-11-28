#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
   int test;
   cin >> test;
   int c=1;
   while(test--){
      long long n;
      cin >> n;
      string s = to_string(n);
      string res="";
      int size= s.size();
      res += s[0];
      int i =0;
      bool flag = true;
      for(i=0; i<size-1; i++) {
         if(s[i] > s[i+1]) break;
      }
      if(i == size-1) {
         flag = false;
      }
      while(s[i] == s[i-1] && i>0) {
         i--;
      }
      //cout << i << endl;
      s[i] = s[i]-1;
      i++;
      for(; i<size; i++){
         s[i] = '9';
      }
      //cout << s << endl;
      if(s[0] == '0') {
         s = s.substr(1);
      }
      if(flag) {
         cout << "Case #" << c<<": "<< s << endl;
      } else {
         cout << "Case #" << c<<": "<< n << endl;
      }
      c++;
   }
   return 0;
}
