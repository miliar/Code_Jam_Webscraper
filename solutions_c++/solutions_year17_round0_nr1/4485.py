#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string tries(string line, int k){
    int linesize = line.size();
    int iter = 0;
    for(int i = 0; i < linesize; i++){
        if(line[i] != '-')
            continue;
        if(i + k > linesize)
            return "IMPOSSIBLE";
        for(int j = i; j < i + k; j++){
            if(line[j] == '-')
                line[j] = '+';
            else
                line[j] = '-';
        }
        iter++;
    }
    return to_string(iter);
}

int main()
{
    string inname = "A-large.in";
    string outname = "A-large.out";
    ifstream infile(inname);
    ofstream outfile(outname);

    int T;
    infile >> T;
    string line;
    int K;
    string res;
    for(int i = 1; i <= T; i++){
        infile >> line;
        infile >> K;
        outfile << "Case #" << i <<": " << tries(line,K);
        if(i < T)
            outfile << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
