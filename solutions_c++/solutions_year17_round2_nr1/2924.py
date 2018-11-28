#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("inp.in", ios::in);
    fout.open("output.txt", ios::out);


    int c = 0;
    int t;
    fin>>t;
    while(t--)
    {
        c++;
        long double dest, n, k, d;
        fin>>dest>>n;
        long double longest = 0;
        for(int i=0; i<n; i++)
        {
            fin>>d>>k;
            long double temp = ((dest-d)/k);
            if(temp > longest)
                longest = temp;
        }

        fout<<"Case #"<<c<<": "<<std::fixed<<std::setprecision(6)<<(dest/longest)<<endl;
    }
    fin.close();
    fout.close();
}
