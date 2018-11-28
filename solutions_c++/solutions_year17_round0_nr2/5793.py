#include<iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <stdlib.h>
using namespace std;

 

int main(){
   ifstream fin ("B-large.in");
   ofstream fout ("oout3.out");
   int test, t = 0;
   fin >> test;
   while(test--){
	   t++;
	   string s;
	   fin >> s;
	   int i = 0;
	   while(i + 1 < s.size() && s[ i ] <= s[ i + 1 ])
	      i++;
	   if(i == s.size() - 1)
           fout << "Case #"<< t <<": "<<s<<endl; 
       else{
       int a = i;
       while(i>= 1 && s[ i - 1 ] == s[ a ])
          i--; 
       s[ i ] -= 1;
 	   for(int j = i + 1; j < s.size(); j++)
 	       s[ j ] = '9';
 	   if(s[ 0 ] == '0')
 	     s = s.substr(1);    
     fout << "Case #"<< t <<": "<<s<<endl; 
	  }
  }
     
}

