#include <fstream>

using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");


int t, r, c;
int nr;
int plit[50];
char C[50][50], rez[50][50];

int main()
{
    int i, j, k, l, last, prev;
    fin>>t;
    for(int nrt=1; nrt<=t; ++nrt)
    {
        fin>>r>>c;
        nr=0;
        for(i=1; i<=r; ++i)
        {
            fin.get();
            for(j=1; j<=c; ++j)
            {
                fin.get(C[i][j]);
                if(C[i][j]!='?' && plit[nr]!=i)
                {
                    plit[++nr]=i;
                }
            }

        }
        prev=0;
        for(i=1; i<=nr; ++i)
        {
            for(k=1; k<=c; ++k)
                if(C[plit[i]][k]!='?')
                {
                    for(j=prev+1; j<=plit[i]; ++j)
                        rez[j][k]=C[plit[i]][k];
                    last=k;
                    for(l=k-1; l>=1 && C[plit[i]][l]=='?'; --l)
                    for(j=prev+1; j<=plit[i]; ++j)
                        rez[j][l]=C[plit[i]][k];
                }
                for(l=last+1; l<=c; ++l)
                for(j=prev+1; j<=plit[i]; ++j)
                    rez[j][l]=C[plit[i]][last];


            prev=plit[i];
        }
        if (prev!=r)
        {
            for(k=1; k<=c; ++k)
            for(j=prev+1; j<=r; ++j)
                    rez[j][k]=rez[prev][k];

        }
        fout<<"Case #"<<nrt<<":\n";
        for(i=1; i<=r; ++i)
        {
            for(j=1; j<=c; ++j)
            fout<<rez[i][j];
            fout<<'\n';
        }
    }

    return 0;
}
