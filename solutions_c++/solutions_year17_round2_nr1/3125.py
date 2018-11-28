#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    fstream plik1,plik2;
    plik1.open( "C:\\Users\\G500\\Desktop\\plik\\inputa.txt",ios::in ); //| ios::app );
    plik2.open( "C:\\Users\\G500\\Desktop\\plik\\outputa.txt",ios::out ); //| ios::app );
    int T;
    double d,n,x,s,time,maxx=0,ans;
    plik2.precision(6);
    plik2<<fixed;
    plik1>>T;
    for(int t=1;t<=T;t++)
    {
        plik1>>d>>n;
        maxx=0;
        for(int i=1;i<=n;i++)
        {
            plik1>>x>>s;
            time=(d-x)/s;
            if(maxx<time) maxx=time;
        }
        ans=d/maxx;
        plik2<<"Case #"<<t<<": "<<ans<<"\n";
    }
    plik2.close();
    plik1.close();
    return 0;
}
