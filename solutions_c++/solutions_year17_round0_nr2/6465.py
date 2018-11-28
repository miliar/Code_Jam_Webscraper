#include <iostream>
#include <fstream>
using namespace std;

string str;

void makeTidy(int u,int v) {
    if(u-v == 0)
        return;

    makeTidy(u+1,v);

    int i = str[u]-'0';
    int j = str[u+1]-'0';

    if(i > j) {
        for(int z = u+1;z<=v;z++) {
            str[z] = 9 + '0';
        }
        i = i-1;
        str[u] = (char)i + '0';
    }
}

int main() {
    ifstream fin;
    fin.open("input.txt");

    ofstream fout;
    fout.open("output.txt");


    int testCase=0;
    fin >> testCase;
    for(int t=0;t<testCase;t++) {
        str  = "";
        fin >> str;
        int len = str.length();
        makeTidy(0,len-1);
        str.erase(0, min(str.find_first_not_of('0'), str.size()-1));
        fout << "Case #"<< t+1 << ": " << str << endl;
    }



    fin.close();
    fout.close();
    return 0;
}