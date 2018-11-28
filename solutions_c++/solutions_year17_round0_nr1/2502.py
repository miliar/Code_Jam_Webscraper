#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("out.txt");

    int T; in >> T;

    string S; int K,x,y;
    for(int x = 1 ; x <= T ; x++)
    {
        in >> S >> K;
        int len = S.length();
        y=0;
        for(int i = 0 ; i <= len-K ; i++)
        {
            if(S[i]=='-')
            {
                y++;
                for(int j = i ; j<i+K ; j++)
                {
                    if(S[j]=='-') S[j]='+';
                    else if(S[j]=='+') S[j]='-';
                }
            }
        }
        bool bo=1;
        for(int i = len-K+1 ; bo && i<len ; i++)
            if(S[i]=='-') bo=0;

        out << "Case #" << x << ": ";
        if(bo) out << y << "\n";
        else out << "IMPOSSIBLE\n";
    }
    return 0;
}
