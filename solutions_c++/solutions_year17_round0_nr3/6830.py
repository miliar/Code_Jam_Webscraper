#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("C-small-1-attempt0.in");
    ofstream fout("outputfile.out");
    int N,i,j,c,d,p,k,n,g,e;
    string S;
    fin>>N;
    int A[N][2];
    for(i=0;i<N;i++)
    {
        fin>>n>>p;
        n=n+2;
        S[0]='O';
        for(j=1;j<n;j++)
        {
            S[j]='.';
        }
        S[j-1]='O';
         for(j=0;j<p;j++)
         {
             c=0;e=0;
             for(k=0;k<n;k++)
                {
                    if(S[k]=='.')
                    {
                        d=1;
                        g=1;
                        while(k+g<n && S[k+g]=='.')
                        {
                                d++;
                                g++;
                        }
                        if(d>=c+1)
                        {
                            c=d;
                            e=k;
                        }
                    }
                }
                S[e+((c-1)/2)]='O';
         }
         j=e+((c-1)/2);
         e=0;c=0;
        for(k=j+1;k<n;k++)
        {
            if(S[k]=='O')
                break;
            else e++;
        }
        for(k=j-1;k>=0;k--)
        {
             if(S[k]=='O')
                break;
            else c++;
        }
        A[i][0]=c>e?c:e;
        A[i][1]=c<e?c:e;
    }
    for(i=0;i<N;i++)
    {
        fout<<"Case #"<<i+1<<": "<<A[i][0]<<" "<<A[i][1]<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
