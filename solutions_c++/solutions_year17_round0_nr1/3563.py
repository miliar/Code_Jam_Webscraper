#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

int decide(vector<char> &linestr, int &psize){
    int count = 0;
    for (int i = 0; i < linestr.size(); ++i){
        if (linestr[i] == '-'){
            for (int j = 0; j < psize; ++j){
                if (i + j >= linestr.size()){
                    return -1;
                }
                if (linestr[i+j] == '+'){
                    linestr[i+j] = '-';
                }
                else {
                    linestr[i+j] = '+';
                }
            }
            count ++;
        }
        
    }
    return count;
}



int main(){

    ifstream infile("A-large.in");
    ofstream outfile("f1.out");

    int n;

    infile >> n;

    for (int acase = 0; acase < n; ++acase){
        string line_of_pank;
        int psize;
        infile >> line_of_pank >> psize;

        vector<char> linestr(line_of_pank.c_str(), line_of_pank.c_str() + line_of_pank.size());
        outfile << "Case #" << acase+1 << ": ";
        int result = decide(linestr, psize);
        if (result == -1) {
            outfile << "IMPOSSIBLE" << endl;
        } else {
            outfile << result << endl;
        }


    }


}