#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string fabuliser(string N)
{
    string ret;
    int length = N.size();
    int j = 0;
    while(length > 1 && N[j] <= N[j+1])
    {
        ret += N[j];
        length--;
        j++;
    }
    if(length != 1)
    {
        char stopped = N[j] - 1;
        ret += stopped;
        for(int x=length; x>1; x--)
        {
            ret += '9';
        }
    }
    else ret += N[j];
    length = N.size();
    for(int i=0; i<length-1; i++)
    {
        if(N[i] > N[i+1])
        {
            ret = fabuliser(ret);
            break;
        }
    }
    return ret;
}

string fixZeros(string N)
{
    while(N[0] == '0') N.erase(0,1);
    return N;
}

int main(int argc, char *argv[])
{
    ifstream infile;
    infile.open (argv[1]);
    ofstream outfile;
    outfile.open (argv[2]);
    int T;
    string N;
    infile >> T;
    //cin >> T;
    for(int i=0; i<T; i++)
    {
        infile >> N;
        //cin >> N;
        N = fabuliser(N);
        //cout << "returned " << N << endl;
        N = fixZeros(N);
        //cout << "fixed " << N << endl;
        outfile << "Case #" << i + 1 << ": " << N << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
