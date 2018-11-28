#include <fstream>
#include <cstring>
using namespace std;


ifstream fin ("input.in");
ofstream fout ("output.out");

int k, t;
char s[1020], c[1020];

int main()
{
    int i, j;
    long long nr, mini, lg;
    fin>>t;
    for(int nrt=1; nrt<=t; ++nrt)
    {
        fin>>s>>k;
        nr=0;
        strcpy(c, s);
        for (lg=0;s[lg]; ++lg);
        for(i=0; s[i+k-1]; ++i)
            if(s[i]=='-')
            {
                ++nr;
                for(j=0; j<k; ++j)
                    if( s[i+j] =='-' ) s[i+j]='+';
                    else s[i+j]='-';
            }
        for(; s[i]; ++i)
            if(s[i]=='-')
                break;
        if(!s[i])
            mini=nr;
        else mini=1000000000;
        nr=0;

        for(i=lg-1; i-k>=0; --i)
            if(c[i]=='-')
            {
                ++nr;
                for(j=0; j<k; ++j)
                    if( c[i-j] =='-' ) c[i-j]='+';
                    else c[i-j]='-';
            }
        for(; i>=0; --i)
            if(c[i]=='-')
                break;
        if(i<0 && nr<mini)
            mini=nr;
        if(mini!=1000000000)
            fout<<"Case #"<<nrt<<": "<<mini<<'\n';
        else fout<<"Case #"<<nrt<<": IMPOSSIBLE\n";
    }
    return 0;
}
