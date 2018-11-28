#include <iostream>
#include<fstream>

using namespace std;

ifstream fin("input.in");
ofstream fout("text.out");

int main()
{
    int n,N;
    fin>>N;
    long long int x;
    int v[20];
    for(int Case=1; Case<=N;++Case)
    {
        fin>>x;

        if(x<10)
        {
            fout<<"Case #"<<Case<<": "<<x<<'\n';
            continue;
        }
        n=0;
        while(x)
        {
            v[n++]= x%10;
            x/=10;
        }
        for(int i=1;i<n;++i)
        {
            if(v[i]>v[i-1])
            {
                v[i]--;
                for(int ii=i-1;ii>=0;--ii)
                {
                    v[ii]=9;
                }
            }
        }
        fout<<"Case #"<<Case<<": ";
        if(v[n-1]!=0)
        fout<<v[n-1];
        for(int i=n-2;i>=0;--i)
        {
            fout<<v[i];
        }
        fout<<'\n';
    }
    return 0;
}
