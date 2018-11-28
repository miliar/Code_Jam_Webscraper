#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
   ifstream is("B.in");
   ofstream os("B.out");
   int T;
   is >> T;
   string s;
   int ind = -1;
   for(int Case = 1; Case <= T; Case++){
      ind = -1;
      is >> s;
      if(s.length()==1){
	 os << "Case #" << Case << ": " << s <<'\n';
	 continue;
      }
      for(int i=1;i<s.length();i++){
	 if(s[i] < s[i-1]){
	    ind = i;
	    break;
	 }
      }
      if(ind == -1){
	 os << "Case #" << Case << ": " << s <<'\n';
 continue;	 
      }
      for(int i=ind + 1;i<s.length();i++){
	 s[i] = '9';
      }
      for(int i=ind;i>0;i--){
	 if(s[i] < s[i-1]){
	    s[i] = '9';
	    s[i-1]--;
	 }
      }
      unsigned long long ans = stoull(s);
      os << "Case #" << Case << ": " << ans <<'\n';

   }
   is.close();
   os.close();
}
