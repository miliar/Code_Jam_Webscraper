 #include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int  main() {
  int t,k,count,count1,count2;
  string s;
  cin >> t;  
  for (int i = 1; i <= t; i++) {
    cin >> s >> k;  // read s and then k.
    count = 0;
    char *cstr = new char[s.length() + 1];
    strcpy(cstr,s.c_str());
    for(int j=0; j < s.length(); j++) {
    if(cstr[j] == '+') count++;
    }
    if(count == s.length()) cout << "Case #" << i << ": " << '0' << endl;
    else {
    count1 = 0;
    for(int j=0; j < s.length(); j++) {
        if(cstr[j] == '-' && (j+k) <= s.length()){
             for(int p =0; p < k ; p++){
             if(cstr[j+p] == '+') cstr[j+p] = '-';
             else cstr[j+p] = '+';
             }
         count1++;
         } 
    }
    count2 = 0;
    for(int j= s.length()-k; j < s.length(); j++) {
    if(cstr[j] == '+') count2++;
    }
    if(count2 == k) cout << "Case #" << i << ": " << count1  << endl; 
    else cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl; 
    }
    
 }
 return 0;
} 
