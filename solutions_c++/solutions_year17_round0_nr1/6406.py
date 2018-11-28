#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fin;
    ofstream fout;
    int T,K, count;
    string S;
    fin.open("test.txt");
    fout.open("out.txt");

    fin>>T;
    for(int l=0;l<T;l++)
    {
        count = 0;
        fin>>S;
        fin>>K;

        for(unsigned int i = 0; i <= S.length() - K; ++i) {
            if(S[i] == '-') {
//                cout<<"Before "<< S << endl;
                count++;
                for(unsigned int j = i; j < i + K; ++j) {
                    if(S[j] == '+')
                        S[j] = '-';
                    else
                        S[j] = '+';
                }
//                cout<<"After "<< S << endl;
            }
        }
        bool flag = true;
        for(unsigned int i = S.length() - K; i < S.length(); ++i) {
            if(S[i] == '-') {
                flag = false;
                break;
            }
        }
        if(flag)
            fout<<"Case #"<<l+1<<": " << count << endl;
        else
            fout<<"Case #"<<l+1<<": " << "IMPOSSIBLE" <<endl;
    }
    return 0;
}
