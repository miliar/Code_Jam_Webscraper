#include<bits/stdc++.h>
using namespace std;
typedef pair<pair<int,int>,char> iic;
iic C[250];
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": " ;
        int Ac, Aj;
        fin >> Ac >> Aj;
        int N=Ac+Aj;
        for(int j=0 ; j<Ac ; j++)
        {
            C[j].second='c';
            fin >> C[j].first.first >> C[j].first.second;
        }
        for(int j=Ac ; j<N ; j++)
        {
            C[j].second='j';
            fin >> C[j].first.first >> C[j].first.second;
        }
        sort(C,C+N);
        if(Ac<=1 && Aj<=1) fout << 2 << endl;
        else
        {
            if(C[1].first.second > C[0].first.first + 720 && C[0].first.second+720 > C[1].first.first) fout << 4 << endl;
            else fout << 2 << endl;
        }
    }
}
