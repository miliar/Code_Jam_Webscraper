#include <iostream>
#include <fstream>

using namespace std;

int T;

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("data.in");
    outfile.open("data.out");
    infile >> T;
    string N;
    char M[20];
    int drop, limit;
    for(int i = 0; i < T; i++) {
        infile >> N;
        int len = N.length();
        int j = 0;
        drop = len;
        while(j < len) {
            int jj = j;
            while(j < len && N[j] == N[jj]) j++;
            if(j != len){
                if(N[j] < N[jj]) {drop = jj; limit = j; j = len;}
            }
        }
        for(int j = 0; j < drop; j++) M[j] = N[j];
        for(int j = drop; j < drop + 1; j++) M[j] = N[j] - 1;
        for(int j = drop + 1; j < len; j++)M[j] = '9';
        outfile <<"Case #" << i + 1 << ": ";
        if(M[0] != '0') outfile << M[0];
        for(int j = 1; j < len; j++) outfile << M[j];
        outfile << endl;
    }
    return 0;
}
