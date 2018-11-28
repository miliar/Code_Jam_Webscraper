/**
* KagreTheBarbarian
* CodeJam 2017
* Compiles with Borland 5.5.1
* 
* program frame coppied from the standard example on the google quick start guide.
* 
* Compile
*  c:\bcc32 pancake.cpp
* Run
*  c:\pancake < in.txt > out.txt
*/

#include <iostream>
using namespace std;
void main() {
   int t=0,k,j,at,count;
   char *str=new char[1001];
   bool chk;

   cin >> t;cin.ignore(1001,'\n');
   for (int i = 1; i <= t; ++i) {
      count=0;
      cin.getline(str,1001,' ');
      j=cin.gcount();
      cin >> k;cin.ignore(1001,'\n');

//      cout << str << "|" <<k <<"|"<<j<<endl; //debug

      for(at=0;at+k<j;at++){
         if(str[at]=='-'){
            count++;
            for(int l=0;l<k;l++)str[at+l]=(str[at+l]=='-')?'+':'-';
         }
      }

      chk=true;
      while(chk && str[at]!='\0'){
         chk = (str[at]=='+');
         at++;
      }

      cout << "Case #" << i << ": ";
      if(chk) cout << count;
      else cout << "IMPOSSIBLE";
      cout << endl;
   }
   delete [] str;
}