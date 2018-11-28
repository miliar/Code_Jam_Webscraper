#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{

    int T,N,K;
    double U;
    double a[58];
    ifstream fin("1.in");
    ofstream fout("1.out");
    fin>>T;
    //cout<<T<<endl;
    fout<<setiosflags(ios::fixed);
    for (int i=0;i<T;i++)
    {
        fin>>N>>K;
        fin>>U;
        double sum=U,avg,ans=1;
        for (int j=0;j<N;j++)
        {
            fin>>a[j];sum+=a[j];
        }
        sort(a,a+N);
        int N1=N-1;
        avg=sum/N;cout<<avg<<endl;
        while (N1>0 && a[N1]>avg) { ans*=a[N1];sum-=a[N1];avg=sum/N1;N1--;}
        cout<<N1<<" "<<ans<<" "<<avg<<endl;
        for (;N1>=0;N1--) ans*=avg;
        fout<<"Case #"<<i+1<<": "<< setprecision(13) <<ans<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
