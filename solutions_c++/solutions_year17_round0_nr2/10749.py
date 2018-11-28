#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;
int Tidy(int n){
    int temp=n,prev;
    while(temp>0){
        prev=temp;
        temp=temp/10;
        if(temp%10>prev%10){
            n--;
            temp=n;
        }
    }
    return n;
}
int main(){

    int i,t,n,result;
    ofstream fout;
    ifstream fin;
    fin.open("B-small-attempt1.in");
    fout.open("output.txt");
    fin>>t;
    for(i=1;i<=t;i++){
        fin>>n;
        result=Tidy(n);
        fout<<"Case #"<<i<<": "<<result<<endl;
    }



   return 0;
}
