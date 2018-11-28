#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in;
    in.open("B-large.in");
    ofstream out;
    out.open("out.txt");

    int T; in >> T;

    string N,str,nines; long long val;
    for(int x = 1 ; x <= T ; x++)
    {
        in >> N;
        for(int i = N.length()-1 ; i>0 ; i--)
        {
            if(N[i]<N[i-1])
            {
                nines="";
                for(int j = i ; j < N.length() ; j++) nines+='9';
                stringstream ss;
                ss << N.substr(0,i);
                ss >> val;
                val--;

                ss.clear();
                ss << val;
                if(val==0)
                {
                    N=nines;
                    break;
                }
                else
                {
                    ss >> str;
                    N=str;
                    N+=nines;
                    i=str.length();
                }
            }
        }
        out << "Case #" << x << ": " << N << "\n";
    }
    return 0;
}
