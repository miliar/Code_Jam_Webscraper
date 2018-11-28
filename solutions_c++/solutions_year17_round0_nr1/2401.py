#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <set>
#include <vector>
using namespace std;

int flip(string s, int no)
{
    if (s.size() < no)
    {
        for (int i = 0; i < s.size(); i++)
            if (s[i] != '+') return -1;

        return 0;
    }

    int n = 0;
    if (s[0] == '-')
    {
        n++;
        for (int i = 0; i < no; i++)
        {
            if (s[i] == '+') s[i] = '-';
            else s[i] = '+';
        }
    }

    size_t found = s.find("-");
    if (found == string::npos) s="";
    else s = s.substr(found);
    //cout<<s<<endl;

    int cnt = flip(s,no);
    if (cnt == -1) return -1;
    else return cnt + n;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    long long T,TT;

    cin>>T;
    for(TT = 1; TT <= T; TT++)
    {
        string s;
        int k;
        cin>>s>>k;
        int result = flip(s,k);
        if (result == -1)
            cout<<"Case #"<<TT<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<TT<<": "<<result<<endl;
        /*string s = "--++--++-+-+---+-++--";
        cout<<flip(s,3)<<endl;
        for (int i = 0; i < s.size()/2; i++)
        {
            char temp = s[i];
            s[i] = s[s.size()-1-i];
            s[s.size()-1-i] = temp;
        }
        cout<<flip(s,3)<<endl;*/
    }

    return 0;
}
