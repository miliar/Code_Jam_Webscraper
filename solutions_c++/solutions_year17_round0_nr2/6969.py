#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
    ifstream fin ;
    fin.open("B-large.in.txt");
    ofstream fout;
    fout.open("B-large.out.txt");
    int n ;
    while (fin >> n){
        for (int caseId = 1 ; caseId <= n ; caseId ++){
            string str;
            fin >> str;
            int len = str.size();
            int tmpIndex = -1;
            for (int i = 1 ; i < len ; i++){
                if ((str[i]  - str[i-1]) < 0){
                    tmpIndex = i -1;
                    break;
                }
            }
            if (tmpIndex != -1){
                int i = tmpIndex;
                for ( ; i >0 ; i--){
                    if (str[i] != str[i-1]) break;
                }
                str[i] = str[i] -1;
                for (int j = i + 1 ; j < len ; j++) str[j] = '9';
                if (str[0] == '0') str=str.substr(1,len -1);
            }

            fout <<"Case #"<<caseId<<": "<<str << endl;
        }
    }
    return 0;
}