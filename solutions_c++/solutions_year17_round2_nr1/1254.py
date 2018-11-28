#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        long long d;
        int n;
        cin>>d>>n;
        int i;
        double mt=-1;
        for(i=0;i<n;i++)
        {
            long long k;
            int s;
            cin>>k>>s;
            if(1.0*(d-k)/s>mt)mt=1.0*(d-k)/s;
        }
        printf("Case #%d: %.8lf\n",tci,d/mt);
        //cout<<"Case #"<<tci<<": "<<d/mt<<endl;
    }
    return 0;
}
