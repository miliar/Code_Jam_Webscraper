#include <fstream>

using namespace std;


ifstream fin ("input.in");
ofstream fout ("output.out");


long long int n, t;
char s[50], nr[50];

int main()
{
    int nrt, ok, i, j;
    char prec;
    fin>>t;
    for(nrt=1; nrt<=t; ++nrt)
    {
        fin>>s;
        prec='0';
        ok=1;
        for(i=0; s[i]; ++i)
            if(ok && s[i]<prec)
            {
                ok=0;
                for(j=i-1; nr[j]==nr[j-1]; --j)
                    nr[j]='9';
                --nr[j];
                nr[i]='9';
            }
            else if (ok && s[i]>=prec) prec=nr[i]=s[i];
            else if (!ok) nr[i]='9';
        nr[i]=0;
        fout<<"Case #"<<nrt<<": ";
        for(i=0; nr[i]=='0'; ++i);
        for(;nr[i]; ++i)
            fout<<nr[i];
        fout<<'\n';
    }
    return 0;
}
