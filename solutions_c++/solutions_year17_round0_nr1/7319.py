#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

string check(string ret, int K, int &counter)
{
    int j = ret.size();
    if(j < K) return ret;
    if(ret[0] == '-')
    {
        counter++;
        for(int i=0; i<K; i++)
        {
            if(ret[i] == '-') ret[i] = '+';
            else ret[i] = '-';
        }
    }
    //cout << "0string is " << ret << endl;
    j = ret.size() - 1;
    if(ret[j] == '-')
    {
        counter++;
        for(int i=0; i<K; i++)
        {
            if(ret[j-i] == '-') ret[j-i] = '+';
            else ret[j-i] = '-';
        }
    }
    //cout << "endstring is " << ret << endl;
    //cout << "string is " << ret << endl;
    if(ret.find('-') == string::npos) return ret;
    char temp1 = ret[0];
    char temp2 = ret[j];
    ret.erase(0,1);
    ret.erase(ret.size()-1,1);
    //cout << "string has become " << ret << endl;
    return temp1 + check(ret, K, counter) + temp2;
}

int main(int argc, char *argv[])
{
    ifstream infile;
    infile.open (argv[1]);
    ofstream outfile;
    outfile.open (argv[2]);
    int T;
    string S;
    infile >> T;
    //cin >> T;
    for(int i=0; i<T; i++)
    {
        int K;
        int counter = 0;
        infile >> S >> K;
        //cin >> S >> K;
        string answer = check(S, K, counter);
        //cout << "returned " << answer;
        outfile << "Case #" << i + 1 << ":";
        if(answer.find('-') == string::npos) outfile << " " << counter << endl;
        else outfile << " IMPOSSIBLE" << endl;
        //if(answer.find('-') == string::npos) cout << " " << counter << endl;
        //else cout << " IMPOSSIBLE" << endl;

    }
    infile.close();
    outfile.close();
    return 0;
}
