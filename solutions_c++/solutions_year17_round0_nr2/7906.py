#include <iostream>
#include <string>

using namespace std;

void makeTidy(string &);
void print(const string &);

int main()
{
    unsigned int T; // Number of test cases
    cin >> T;
    for(unsigned int i = 1; i <= T; ++i)
    {
        //unsigned int N; // Max number
        string N; // Max number
        cin >> N;
        makeTidy(N);
        cout << "Case #" << i << ": ";
        print(N);
    }
    return 0;
}

void makeTidy(string &str)
{
    int memento = -1; // keeps track of trailing equalities
    for(unsigned int i = 1; i < str.length(); ++i)
    {
        if(str[i] < str[i-1]) // first instance of untidiness
        {
            int ind = memento < 0 ? i-1 : memento;
            --str[ind];
            for(unsigned int j = ind + 1; j < str.length(); ++j)
                str[j] = '9';
            return;
        }
        if(str[i] == str[i-1])
        {
            if(memento < 0 || str[i] != str[memento])
                memento = i-1;
        }
    }
}

void print(const string &N)
{
    unsigned int i = 0;
    while(N[i] == '0')
        ++i;
    for(; i < N.length(); ++i)
        cout << N[i];
    cout << '\n';
}
