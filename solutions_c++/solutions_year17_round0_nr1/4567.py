#include <iostream>
#include<fstream>
#include<string>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("text.out");

int main()
{
    int N;
    fin>>N;
    string s;
    int k;
    int n;
    int v[1000];
    int i,j;
    int sum;
    int sol;
    for(int Case=1; Case<=N;++Case)
    {
        sol=0;
        fin>>s;
        fin>>k;
        i=0;
        for(auto c:s)
        {
            if(c=='+')
                v[i] =0;
            else
                v[i]=1;
                sum+=v[i];
            i++;
        }
        n=i;
        for(i=0;i<n;++i)
        {
            if(v[i]==1)
            {
                sol++;
                if(i+k>n)
                {
                    fout<<"Case #"<<Case<<": IMPOSSIBLE\n";
                    goto nextt;
                }
                for(j=i;j<i+k;++j)
                {
                    v[j]^=1;
                }
            }
        }
        fout<<"Case #"<<Case<<": "<<sol<<'\n';
        nextt:;
    }


    return 0;
}
