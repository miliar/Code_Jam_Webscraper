#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

int s2n(string input)
{
    int out=0;
    int neg=1;
    if (input.length()>=1)
    {
        if (input[0]=='-')
        {
            neg=-1;
            input=input.substr(1,input.length()-1);
        }
    }
    for (int i=0;i<input.length();i++)
    {
        out*=10;
        out+=input[i]-'0';
    }
    out*=neg;
    return out;
}

bool finished(string input, int size){
    for (int i=0;i<size;i++){
        if (input[i]=='-')
            return false;
    }
    return true;
}

int main(void)
{
    ifstream ifile;
    ofstream ofile;
    ofile.open("tidyOUT.txt");
    ifile.open("tidy.in");
    string input="";
    getline(ifile,input);
    int sets = s2n(input);
    for (int set=0;set<sets;set++)
    {
        ofile<<"Case #"<<set+1<<": ";
        cout<<"Case #"<<set+1<<": ";
        
        getline(ifile,input);
        if (input.size()==1){
            ofile<<input<<endl;
            cout<<input<<endl; continue;
        }
        int lastNine = input.size();
        for (int j=input.size()-1; j>0; j--){
            if (input[j]<input[j-1]){
                input[j-1]-=1;
                for (int i=j;i<lastNine;i++){
                    input[i]='9';
                }
                lastNine=j;
            }
        }
        if (input[0]=='0'){
            input=input.substr(1);
        }
        ofile<<input<<endl;
        cout<<input<<endl;
    }
    ofile.close();
    return 0;
}































