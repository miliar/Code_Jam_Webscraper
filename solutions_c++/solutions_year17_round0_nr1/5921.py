#include<iostream>
#include<string>
#include<vector>
#include<sstream>

using namespace std;

void flip(char &c){c=(c=='+')?'-':'+';}

string flipCounter(string pancakeStr, int flipperSize){
   int len=pancakeStr.length(), pos=0, flipCount=0;
   while(pos<(len-flipperSize)){
      char cur=pancakeStr[pos];
      if(cur=='-'){
         for(int i=pos;i<(pos+flipperSize);++i)flip(pancakeStr[i]);
	 ++flipCount;	   
      }
      ++pos;
   }	
   char firstOfLastFlip = pancakeStr[pos];
   for(int i=pos;i<len;++i){
      if(pancakeStr[i]!=firstOfLastFlip) return "IMPOSSIBLE";
   }
   if(firstOfLastFlip=='-') ++flipCount;
   ostringstream oss;
   oss << flipCount;
   return oss.str();
}


int main(){
   int caseCount, flipperSize;
   string pancakeStr;
   cin >> caseCount;
   for(int i=1;i<=caseCount;++i){
      cin >> pancakeStr;
      cin >> flipperSize;
      cout << "Case #" << i << ": " 
           << flipCounter(pancakeStr,flipperSize) << endl;
   }
}
