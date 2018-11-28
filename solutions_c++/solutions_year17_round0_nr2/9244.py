//============================================================================
// Name        : my1.cpp
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
#include<string>
#include<fstream>
#include<sstream>
using namespace std;
bool isTidy(int n){
	int next_digit = n%10;
    int n1= n/10;
    while (n1)
    {
        int digit = n1%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n1 = n1/10;
    }
 
    return true;
}

int main() {
	ifstream infile("/home/andrew/Downloads/B-small-attempt0.in");
	    ofstream ofile("/home/andrew/Desktop/sub-1.out");
		int t,num;
		string s,s1;
		//cin>>s;cin>>k;
	    getline(infile,s1);
	    stringstream geek(s1);
	    geek>>t;
	    cout<<t<<endl;
	    for (int x=1 ;x<=t;x++){
	    	ofile<<"Case #"<<x<<": ";
	    	getline(infile,s1);
	        stringstream geek(s1);
	        geek>>num;
	        cout<<num<<endl;
            while(num>=0){
            if(!isTidy(num)){num-=1;}
            else break;
            }
            ofile<<num<<endl;
	}
	return 0;
}
