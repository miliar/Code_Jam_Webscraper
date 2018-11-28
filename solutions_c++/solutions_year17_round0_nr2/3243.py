/**
* KagreTheBarbarian
* CodeJam 2017
* Compiles with Borland 5.5.1
* 
* program frame coppied from the standard example on the google quick start guide.
* 
* Compile
*  c:\bcc32 tidy.cpp
* Run
*  c:\tidy.cpp < in.txt > out.txt
*/

#include <iostream>
using namespace std;
void main() {
   int t=0, start=0, at=0, back=0;
   char *str=new char[20];str[0]='\0';

   cin >> t; cin.ignore(20,'\n');
   for (int i = 1; i <= t; ++i) {
      cin.getline(str,20);
      back=0;
      for(at=1;str[at]!='\0' && str[at-1]<=str[at];at++){
//        cout << str[at] << endl; //debug
        if(str[at]!=str[at-1])back=at;
      }
      if(str[at]!='\0'){
         str[back]--;back++;
         while(str[back]!='\0'){str[back]='9';back++;}
      }
      for(start=0;str[start]=='0';start++);
      cout << "Case #" << i << ": " << (str+start) << endl;
   }
   delete [] str;
}