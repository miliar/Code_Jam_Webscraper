#include <cstdio>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>

typedef long long ll;

using namespace std;

ifstream cinf;
ofstream coutf;

char rev(char a)
{
    if(a=='+')
        return '-';
    else
        return '+';
}
void flipCount(string s, int K)
{
    int sz = s.length();
    int res = 0;
    int cnt = 0;
    
    int strcnt = 0;
    
    bool start = false;
    int i = 0;
    for(i = 0; i < sz; ++i)
    {
        if(s[i]=='+' && !start)
        {
        }
        else
        {
            if(!start)
            {
                strcnt = i;
                start = true;
                cnt++;
            }
            else
            {
                cnt++;
            }
            if(cnt==K)
            {
                for(int j = strcnt; j < strcnt+K; ++j)
                    s[j] = rev(s[j]);
                start = false;
                cnt = 0;
                i = i - (K-1);
                res++;
            }
        }
    }
    
    if(s.find('-') != string::npos)
    {
        coutf << "IMPOSSIBLE";
        return;
    }
    coutf << res;
    return;
}



int main() {
    int T, K;
    string N;
    
    cinf.open("A-small.in.txt");
    coutf.open("A-small.out.txt");
    
    cinf >> T;
    
    for (int ri = 1; ri <= T; ++ri) {
        cinf >> N >> K;
        
        coutf << "Case #" << ri << ": ";
        flipCount(N, K);
        coutf << endl;
        
    }
    
    return 0;
}

