#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;
#define MAX 1000000000000000000


std::string decr(std::string num, int faultyDigit){
    switch(num[faultyDigit]){
        case '0':
            decr(num,faultyDigit-1);
            num[faultyDigit]= '9';
            break;
        case '1':
            num[faultyDigit]= '0';
            break;
        case '2':
            num[faultyDigit]= '1';
            break;
        case '3':
            num[faultyDigit]= '2';
            break;
        case '4':
            num[faultyDigit]= '3';
            break;
        case '5':
            num[faultyDigit]= '4';
            break;
        case '6':
            num[faultyDigit]= '5';
            break;
        case '7':
            num[faultyDigit]= '6';
            break;
        case '8':
            num[faultyDigit]= '7';
            break;
        case '9':
            num[faultyDigit]= '8';
            break;
    }
    return num;
}


int main() {
	// your code goes here

	int t;
	long long n;
	long long z;
	std::string num;
	vector<int> tidy;
	bool flag;
	int faultyDigit;

	cin>>t;

	for(int k = 1; k <= t; k++){
	    cin>>n;
	    std::stringstream ss;
        ss << n;
        num = ss.str();
	    do{
            flag = true;
            for(int j = 1; j < num.length(); j++){
                if(num[j] < num[j-1]){
                    faultyDigit = j-1;
                    flag = false;
                    break;
                }
            }
            if(!flag){
                num = decr(num,faultyDigit);
                for(int i = faultyDigit + 1; i < num.length(); i++){
                    num[i] = '9';
                }
            }
	    }while(!flag);
        //discard all zeroes from the start
        for(int i = 0; i < num.length();i++){
            if(num[0] == '0'){
                num.erase (num.begin()+0);
            }
        }
        cout<<"Case #"<<k<<": "<<num<<endl;
	}
	return 0;
}
