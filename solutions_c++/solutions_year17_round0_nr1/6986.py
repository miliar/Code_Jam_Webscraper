#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
    ifstream fin ;
    fin.open("A-large.in.txt");
    ofstream fout;
    fout.open("A-large.out.txt");
    int n ;
    while (fin>> n) {

        for (int caseId = 1 ; caseId <= n ; caseId ++ ) {

            string str;
            int changeLen;
            fin >> str >> changeLen;
            int len = str.size();


            if (changeLen > len || changeLen == 0) {
                bool isSuccess = true;
                for (int i = 0; i < len; i++) {
                    if (str[i] == '-') {
                        isSuccess = false;
                        break;
                    }
                }
                if (isSuccess) fout << "Case #"<<caseId<<": " << 0 << endl;
                else fout << "Case #"<<caseId<<": IMPOSSIBLE" << endl;
            } else {
                int i;
                int result = 0;
                for ( i = 0; i < len; i++) {
                    if (i + changeLen > len ) break;
                    if (str[i] == '-') {
                        for (int j = 0 ; j < changeLen ; j++){
                            str[i+j] = (str[i+j] == '+') ? '-' : '+';
                        }
                        result++;
                    }
                }
                int tmpIndex = i;
                bool isSuccess = true;
                for (i = tmpIndex ; i < len ; i++){
                    if (str[i] == '-'){
                        isSuccess = false;
                        break;
                    }
                }
                if (isSuccess) fout<<"Case #"<<caseId<<": " << result << endl;
                else fout << "Case #"<<caseId<<": IMPOSSIBLE" << endl;
            }


        }
    }
    return 0;
}