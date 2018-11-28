#include<iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <stdlib.h>
using namespace std;


char flip(char c){
	if(c == '+')
	   return '-';
	   else return '+';
	}

int main(){
   ifstream fin ("A-large.in");
   ofstream fout ("oout.out");
   int test, t = 0, new_s;
   fin >> test;
   while(test--){
	    t++;
		string s;
		int k;
		fin >> s;
		fin >> k;
		bool imp = false;
		int i = 0, f = 0;
		while(i < s.size()){
			while(i < s.size() && s[ i ] == '+')
			   i++;
			if(i >= s.size())
			   break;
			f++;
			if(s[ i ] == '-'){
				if(i + k - 1 >= s.size()){
				   imp = true;
				   break;
			   }
			   new_s = -1;
			   for(int j = 0; j < k; j++ ){
			       s[ j + i ] = flip(s[ j + i ]);
			       if(s[ j + i ] == '-' && new_s == -1)
			            new_s = j + i;
			   }
			}
			if(new_s == -1)
			    i += k;
	}
	if(!imp)
     fout << "Case #"<< t <<": "<<f<<endl;
     else
       fout << "Case #"<< t <<": IMPOSSIBLE"<<endl;
    
   // cout << *A << endl;
}
}
