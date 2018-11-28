#include <iostream>
#include <vector>
#include <map>
#include <map>
#include <fstream>
#include <cstring>
#include <stdio.h>

#define LL long long
#define in cin
#define out cout

using namespace std;

bool Compare(char ch1 , char ch2){
    int n1 = ch1-'0';
    int n2 = ch2-'0';

    return n1 >= n2 ;
}

char decrement(char ch){
    int num = ch-'0';
    num--;
//    cout<<"Enter"<<endl<<num <<endl;
    ch = (char)(num+'0');
//    cout<< str[i] <<endl;

}

string CheekTidy(string str){
    int len  = str.length();

    for ( int i = 1 ; i < len ; i++ ){

        if(!Compare(str[i],str[i-1])){

            str[i-1] = decrement(str[i-1]);
            if(i > 1 &&  !Compare(str[i-1],str[i-2])){
                i -= 3;
                continue;
            }
            for ( int j = i ; j < len ; j++ ){
                str[j]='9';
            }
            if(str[0]=='0')
                return str.substr(1,len);
            return str;
        }
    }

    return str;
}

int main(){

    ifstream in("B-large.in");
    ofstream out("Output.txt");



    int t;in>>t;



    for(int kase = 1 ; kase <= t ; kase++ ){


        string str; in>>str;
        out<<"Case #"<<kase<<": "<<CheekTidy(str)<<endl;
    }
    return 0;
}

