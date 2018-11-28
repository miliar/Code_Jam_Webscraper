#include<iostream>
#include<string>
#include<vector>

using namespace std;

bool nonDecreasing = true;

string largestTidyNumber(string input){
   int len=input.length();
   char mustNotLess='0';
   for(int i=0;i<len-1;++i){
	if(input[i]>input[i+1]){
	   nonDecreasing = false;
	   input[i]-=1;
	   input=input.substr(0,i+1);
           string filler;
	   for(int j=1;j<=len-(i+1);++j){
		filler+="9";
           }
           input+=filler;
           if(input[0]=='0') input=input.substr(1);
	   break;
	}
        nonDecreasing = true;
   }	
  if(nonDecreasing) {return input;}
  else {return largestTidyNumber(input);}
}


int main(){
   int caseCount;
   string inputNumStr;
   cin >> caseCount;
   for(int i=1;i<=caseCount;++i){
     cin >> inputNumStr;
     cout << "Case #" << i << ": "
          << largestTidyNumber(inputNumStr) << endl;
   }
}
