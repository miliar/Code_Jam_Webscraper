#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
    ifstream inf ("in.txt");
    ofstream outfile("output.txt");
    int t;
    inf>>t;
    for(int i = 0; i < t; ++i){
        string str;
        int k, flag = 0, size, counter = 0;
        inf>>str>>k;
        size = str.size();
        for(int j = 0; j < size; ++j){
            if(str[j] == '-'){
                if((j + k) > size){
                    flag = 1;
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
        if(flag == 1){
            outfile<<"Case #"<< i+1<<": IMPOSSIBLE"<<endl;
        }
        else
            outfile<<"Case #"<< i+1<<": "<<counter<<endl;

    }
}
