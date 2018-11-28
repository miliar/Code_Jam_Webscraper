#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": " ;
        string s;
        int k;
        fin >> s >> k;
        int l = s.size();
        int cont=0;
        for(int j=0 ; j<=l-k ; j++)
        {
            if(s[j]=='-')
            {
                cont++;
                for(int w=j+1; w<j+k ; w++)
                {
                    if(s[w]=='+') s[w]='-';
                    else s[w]='+';
                }
            }
        }
        for(int j=l-k+1 ; j<l ; j++)
        {
            if(s[j]=='-')
            {
                cont=-1;
                break;
            }
        }
        if(cont ==-1) fout << "IMPOSSIBLE" << "\n";
        else fout << cont << "\n";
    }
}
