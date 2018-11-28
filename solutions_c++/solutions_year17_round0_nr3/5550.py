#include <iostream>
#include <fstream>
#include<stack>
#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

unsigned long long int m, counter;

unsigned long long int findMaxIndex(unordered_map<int,unsigned long long int> a){
    unsigned long long int max = a[0], myIndex = 0;
    for(unsigned long long int i=1;i<a.size();i++){
        if(a[i]>max){
            max = a[i];
            myIndex = i;
        }
    }
    return myIndex;
}

void Baths(unsigned long long int k, unsigned long long int t, unordered_map<int,unsigned long long int> &a, ofstream &myfile){
    unsigned long long int ls, rs;
    for(unsigned long long int i=0;i<k;i++){
        unsigned long long int ourIndex = findMaxIndex(a);
        if( a[ourIndex]%2 == 0 ){
            ls = (a[ourIndex]/2)-1;
            rs = a[ourIndex] - (a[ourIndex]/2);
            
        }else{
            ls = (a[ourIndex]/2);
            rs = a[ourIndex] - ((a[ourIndex]/2)+1);
        }
        a[ourIndex] = ls;
        a[a.size()] = rs;
    }
    if(rs>ls){
        unsigned long long int temp = ls;
        ls = rs;
        rs = temp;
    }
    myfile<<"Case #"<<t<<": "<<ls<<" "<<rs<<endl;
}


int writeFile ()
{
    unordered_map<int,int> a;
    ofstream myfile;
    ifstream myfile2;
    myfile2.open ("/Users/mac1/Desktop/anime/input.txt");
    myfile.open ("/Users/mac1/Desktop/anime/example.txt");
    
    //
    unsigned long long int n, k, t, ls, rs;
    myfile2>>t;
    for(unsigned long long int i=0;i<t;i++){
        myfile2>>n>>k;
        unordered_map<int,unsigned long long int> a;
        a[0] = n;
        Baths(k, i+1, a, myfile);
    }    //
   
    myfile2.close();
    myfile.close();
    return 0;
}


int main(int argc, const char * argv[])
{
    writeFile();
    cout<<"meh";
    
}