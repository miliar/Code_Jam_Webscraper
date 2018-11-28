#include<bits/stdc++.h>
using namespace std;
typedef long long int lt;
int main()
{
    lt t,n,d,e,i,b[10001][2],j,k;

    double s,ft=0,res;
    cin>>t;
    e=t;
    while(t--)
    {
        ft=0;
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>j>>k;
            s=(d-j)/(float)k;
            //cout<<d<<" "<<j<<" "<<s<< " ";
            if(s>ft)
            {
                ft=s;
            }
        }
        //cout<<ft<<" "<<d<<endl;
        res = d/ft;
        cout<<"Case #"<<e-t<<": ";
        printf("%.6f\n",res);

    }

}
