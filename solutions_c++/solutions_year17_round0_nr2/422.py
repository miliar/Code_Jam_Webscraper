#include <cstdlib>
#include <iostream>
#include <string.h>
using namespace std;

int check_ok(char* str){
   int breakpoint = -1;
   for(int i=0;i<strlen(str)-1;i++){
      if(str[i]>str[i+1]) {
	    breakpoint = i;
	    break;
	  }
   }
   return breakpoint;
}

int main(){
   int T;
   cin >> T;
   for(int t=0;t<T;t++){
      char str[30];
      cin >> str;
      while(1){
	     int bp = check_ok(str);
	     if(bp==-1) break;
	     str[bp]--;
	     for(int i=bp+1; i<strlen(str);i++){
		    str[i] = '9';
		 }
	  }
	  int first_nonzero = 0;
	  while(str[first_nonzero]=='0') first_nonzero++;
	  cout << "Case #" << t+1 << ": ";
	  for(int i=first_nonzero; i<strlen(str);i++){
	     cout << str[i];
	  }
	  cout << "\n";
   }
}
