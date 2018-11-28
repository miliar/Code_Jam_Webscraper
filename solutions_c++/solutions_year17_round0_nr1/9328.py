#include <iostream>
#include <fstream>
#include <sstream>
#include <stdint.h>
#include <string>
#include <stdio.h>

using namespace std;



void writeLineIntoFile(char * filename,int caseID ,int  lastTidy){
  ofstream myfile;
  myfile.open (filename,ofstream::app);
  if(lastTidy==-1) {
      myfile << "Case #"<<caseID<<": "<<"IMPOSSIBLE"<<"\n";
  }
  else {
  myfile << "Case #"<<caseID<<": "<<lastTidy<<"\n";

  }
  myfile.close();
}
// string to int
int stringToInt(string intAsString){
int  result;
istringstream convert(intAsString);
convert >> result;
return result;
}

string intToString(int  number){
stringstream ss;
ss << number;
string str = ss.str();
return str;

}


bool isHappy(string line){

 int l=line.size();
 for(int i=0;i<l;i++){
    if(line[i]=='-') {
            return false;
 }
 }
 return true;

}

int  toHappy(string lin,int b){

    string line=lin;
    int n=0;
  if(isHappy(line)){
    return 0;
  }
  else {
 int l=line.size();
 for(int i=0;i<l-b+1;i++){
   if(line[i]=='-'){
        for(int j=0;j<b;j++){
       if( line[i+j]=='+'){
        line[i+j]='-';
       }
       else if(line[i+j]=='-'){
       line[i+j]='+';
       }


        }
   n++;
   }
 }

   if(isHappy(line)){
    return n;

   }
    else {
        return -1;
    }

  }
}
int main()
{




 int i=0;
  ifstream infile("A-large.in");
  string line;


  while (getline(infile, line)) {
        if(i!=0){
    string str1(line);
   istringstream iss(str1);
   string s1[2];
   iss>>s1[0];
   iss>>s1[1];
         writeLineIntoFile("output.txt",i,toHappy(s1[0],stringToInt(s1[1])));
        }
        i++;
  }


     return 0;
}
