#include<bits/stdc++.h>

using namespace std;


int main(void)
{
    freopen("C:\\Users\\user\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\user\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;


    for(int i=1;i<=t;i++)
    {
        double n,d;
        cin>>d>>n;

        double max=0;
        for(int j=1;j<=n;j++)
        {
            double sp,lo;
            cin>>lo>>sp;
            if((d-lo)/sp>max)
                max=(d-lo)/sp;

        }
        cout<<"case #"<<i<<": ";
        printf("%6f\n",d/max);


    }
}
