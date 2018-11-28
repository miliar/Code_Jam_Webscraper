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
    ofile.open("pancakeOUT.txt");
    ifile.open("pancake.in");
    string input="";
    getline(ifile,input);
    int sets = s2n(input);
    for (int set=0;set<sets;set++)
    {
        string grill = "";
        ofile<<"Case #"<<set+1<<": ";
        getline(ifile,grill);
        int grillSize = 0;
        while (grill[grillSize]!=' '){grillSize++;}
        int flipper = s2n(grill.substr(grillSize+1));
        if (flipper<0 || flipper>grillSize){
            if (finished(grill,grillSize)){
                ofile<<"0"<<endl;
            } else {
                ofile<<"IMPOSSIBLE"<<endl;
            }
            continue;
        }
        int count = 0;
        for (int i=0;i<=grillSize-flipper;i++){
            if (grill[i]=='-'){
                for (int j=i;j<i+flipper;j++){
                    grill[j] = grill[j]=='-' ? '+' : '-';
                }
                count++;
            }
        }
        if (finished(grill,grillSize)){
            ofile<<count<<endl;
        } else {
            ofile<<"IMPOSSIBLE"<<endl;
        }
    }
    ofile.close();
    return 0;
}































