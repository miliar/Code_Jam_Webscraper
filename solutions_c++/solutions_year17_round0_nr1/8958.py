//============================================================================
// Name        : my2.cpp
// Author      : andrew
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<algorithm>
#include<list>
#include <vector>
#include <stack>
#include <fstream>
#include <sstream>
using namespace std;

char flip(char c){
	if (c=='+'){return '-';}
	else return '+';
}
int main() {
	ifstream infile("/home/andrew/Downloads/A-large.in");
    ofstream ofile("/home/andrew/Desktop/sub-1.out");
	int t,k;
	string s,s1;
	//cin>>s;cin>>k;
    getline(infile,s1);
    stringstream geek(s1);
    geek>>t;
    for (int x=1 ;x<=t;x++){
		ofile<<"Case #"<<x<<": ";
		unsigned int i=0,time=0;
	getline(infile,s1);
	s=s1.substr(0,s1.find(" "));
	s1=s1.substr(s1.find(" "),s1.length())	;
	stringstream geek(s1);
	geek>>k;
	//cout<<s<<" "<<k<<endl;
    while(i<=s.length()-k){
      if(s.at(i)=='-'){
		  //cout<<"i="<<i<<"\n";
    	  for(int j=0;j<k;j++){s.at(i+j)=flip(s.at(i+j));}
    	  time+=1;
    	  //cout<<time<<endl;
      }
      while(s.at(i)!='-'){
		  if(i<s.length()-1){i++;}
		  else break;}
    }
    if(i==s.length()-1 and s.at(i)!='-'){ofile<<time<<endl;}
    else{ofile<<"IMPOSSIBLE\n";}
    
}
	return 0;
}
