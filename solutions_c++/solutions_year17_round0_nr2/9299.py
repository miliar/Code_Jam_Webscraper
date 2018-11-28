#include<iostream>
#include <string> 
#include <stdlib.h> 
#include <fstream>
using namespace std;
int main(){
ofstream output;
ifstream input;
input.open ("B-large.in");
output.open ("output.txt");
int t,n;
input>>t;
string is,fs;
for(int k=0;k<t;k++){
  input>>is;
  fs="";
 
  fs = is[is.length()-1];
  for(int i=is.length()-2;i>=0;i--){
    if(fs[0]>=is[i])
        fs = is[i]+fs;
    else{
      n = fs.length();
      fs = "";
      for(int j=0;j<n;j++)
        fs+="9";
      fs = char(is[i]-1)+fs;
    }
  }
  if(fs[0]=='0')
    fs = fs.substr(1);
  output<<"Case #"<<k+1<<": "<<fs<<endl;
} 
input.close();
output.close();
return 0;
}
