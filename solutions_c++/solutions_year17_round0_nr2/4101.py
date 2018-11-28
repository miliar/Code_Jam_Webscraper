#include <cstdio>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>

typedef long long ll;

using namespace std;

string s1;

char dec(char a)
{
    switch(a)
    {
        case '1':
            return '0';
        case '2':
            return '1';
        case '3':
            return '2';
        case '4':
            return '3';
        case '5':
            return '4';
        case '6':
            return '5';
        case '7':
            return '6';
        case '8':
            return '7';
        case '9':
            return '8';
    }
    return '0';
}
ll tidy(ll n)
{
    if(n < 10)
        return n;
    stringstream ss;
    ss << n;
    s1 = ss.str();
    ll res;
    
    char ch0, ch1;
    int sz = s1.length();
    for(int i = sz-1; i >0; --i)
    {
        ch0 = s1[i];
        ch1 = s1[i-1];
        if(ch0 >= ch1)
        {}
        else
        {
            for(int j = i; j < sz; ++j)
                s1[j] = '9';
            s1[i-1] = dec(ch1);
        }
    }
    stringstream ssR(s1);
    ssR >> res;
    return res;
}



int main() {
    int T;
    ll N;
    ifstream cinf;
    cinf.open("A-small.in.txt");
    ofstream coutf;
    coutf.open("A-small.out.txt");
    
    cinf >> T;
    
    for (int ri = 1; ri <= T; ++ri) {
        cinf >> N;
        coutf << "Case #" << ri << ": " << tidy(N) << endl;
        
    }
    
    return 0;
}

