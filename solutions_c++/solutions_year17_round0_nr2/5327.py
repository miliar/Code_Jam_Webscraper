#include <iostream>
#include <fstream>
#include<stack>
#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
unsigned long long int stringToInt(char Digit){
    return Digit - '0';
}


int writeFile ()
{
    
    ofstream myfile;
    ifstream myfile2;
    myfile2.open ("/Users/mac1/Desktop/anime/input.txt");
    myfile.open ("/Users/mac1/Desktop/anime/example.txt");
    unsigned long long t;
    string n;
    myfile2>>t;
    for(unsigned long long k=0;k<t;k++){
        myfile2>>n;
        for(unsigned long long int i=n.length()-1;i!=-1;i--){
            //cout<<i<<" "<<n<<endl;
            if(i-1>=0){
                if(n[i]<n[i-1]){
                    unsigned long long int digit = stringToInt(n[i-1]);
                    n[i] = '9';
                    char digit2 = '0' + (digit - 1);
                    n[i-1] = digit2;
                    for(unsigned long long int j=i;j<n.length();j++){
                        n[j] = '9';
                    }
                }
            }
        }
        if( n[0] == '0' ){
            n = n.substr(1, n.length());
        }
        myfile<<"Case #"<<k+1<<": "<<n<<endl;
    }
    myfile2.close();
    myfile.close();
    return 0;
}


int main(int argc, const char * argv[])
{
    writeFile();
    cout<<"meh";
    
}