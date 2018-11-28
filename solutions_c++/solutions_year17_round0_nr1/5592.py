#include<iostream>
#include<fstream>
#include<string>
using namespace std;


int main(){

    ofstream fo;
    fo.open("A-large-correct.txt");

    ifstream fi;
    fi.open("A-large.in");

    int t;

    fi>>t;
    for(int i = 0; i < t; ++i){

        string str;
        int k;
        int flags=0;
        int sizes,counter = 0;

        fi>>str>>k;

        sizes=str.size();

        for(int j=0;j<sizes;++j){
            if( str[j]=='-'){
                if((j+k)>sizes){

                    flags = 1;

                    break;
                }
                else{

                    ++counter;

                    for(int l = j; l < (j + k); ++l){
                        if(str[l] == '-')
                            str[l] = '+';
                        else
                            str[l] = '-';
                    }
                }
            }
        }
        if(flags == 1){
            fo << "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
            fo << "Case #"<<i+1<<": "<<counter<<endl;

    }
}
