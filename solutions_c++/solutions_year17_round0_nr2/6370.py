#include <fstream>
#include <iostream>

using namespace std;

void work(string&N, uint i) {
    if(i == N.length())
        return;
    if(i == 0)
        ;
    else if(N[i] == '0') {
        N[i-1]--;
        for(uint j = i; j<N.length(); ++j)
            N[j] = '9';
        i = i-2;

    }
    else if(N[i-1] > N[i]) {
        N[i-1] = N[i-1] - 1;
        for(uint j = i; j<N.length(); ++j)
            N[j] = '9';
        i = i-2;
    }
    work(N, i+1);
}

int main(int argc, char *argv[])
{
    ifstream fin;
    ofstream fout;
    int T;
    fin.open("test.txt");
    fout.open("out.txt");

    string N;

    fin>>T;
    for(int l=0;l<T;l++)
    {
        fin>>N;
        if(N.length() == 1) {
            fout<<"Case #"<<l+1<<": " << N << endl;
            continue;
        }
        work(N, 1);
        if(N[0] == '0')
            N.erase(0, 1);
        fout<<"Case #"<<l+1<<": " << N << endl;
    }
    return 0;
}
