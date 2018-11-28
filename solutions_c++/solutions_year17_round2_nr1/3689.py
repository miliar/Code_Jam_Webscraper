#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,c=1;
    cin>>T;
    while(T--)
    {
        long long int N,D,i;
        cin>>D>>N;
        long long int ki=0;
        double houri=0,hour =0;
        long double si;
        for(i=0;i<N;i++)
        {
            cin>>ki>>si;
            houri = (long double)(D-ki)/si;
            if(houri>hour)
                {
                    hour=houri;
                }
        }
        double speed = (long double) D/hour;
        printf("Case #%d: %lf\n",c,speed);
        //cout<<"Case #"<<i<<": "<<speed<<endl;
        c++;


    }
}
