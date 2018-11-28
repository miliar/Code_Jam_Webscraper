#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    int N,i,j,c,d,p,k,n,g,e;
    string S;
    cin>>N;
    for(i=0;i<N;i++)
    {
        cin>>n>>p;
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
        d=c>e?c:e;
        e=c<e?c:e;
        cout<<"Case #"<<i+1<<": "<<d<<" "<<e<<endl;
    }
    return 0;
}
