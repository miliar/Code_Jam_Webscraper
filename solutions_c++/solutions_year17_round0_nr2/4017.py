#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>

using namespace std;

int mismatchIndex(string &s, int length)
{
    for(int i=1;i<length;i++)
    {
        if(s[i-1] > s[i]) return i-1;
    }
}

int correctIndex(string &s,int index)
{
    int i;
    for(i=index;i>0;i--)
    {
        if(s[i] != s[i-1]) break;
    }
    return i;
}

long long int atoi(string s,int length)
{
    long long int x = 0;
    for(int i=0;i<length;i++) x = x*10 + s[i] - 48;
    return x;
}

int main()
{
    int t;
    ifstream in;
    ofstream out;
    in.open("inputLarge.txt");
    out.open("outputLarge.txt");
    int cases = 0;
    in>>t;
    while(t--)
    {
        cases++;
        string s;
        in>>s;
        int length = s.length();
        int index = mismatchIndex(s,length);
        index = correctIndex(s,index);
        s[index]--;
        for(int i=index+1;i<length;i++)
        {
            s[i] = '9';
        }
        long long int ans = atoi(s,length);
        out<<"Case #"<<cases<<": "<<ans<<endl;
    }
    return 0;
}
