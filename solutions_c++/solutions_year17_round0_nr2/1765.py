#include <iostream>

using namespace std;

int main()
{
    int tdb,i,j;
    long long A;
    cin>>tdb;
    int t;
    int felb[19];
    for (t=0; t!=tdb; t++)
    {
        cin>>A;
        cout<<"CASE #"<<t+1<<": ";
        if (A==0) {cout<<0<<endl; continue;}
        for (i=0; i!=19; i++)
        {
            felb[i]=A%10;
            A/=10;
        }
        for (i=0; i!=18; i++)
        {
            if (felb[i]<felb[i+1])
            {
                for (j=i; j!=-1; j--)
                felb[j]=9;
                felb[i+1]--;
            }
        }
        i=18;
        while (felb[i]==0) {i--;}
        for (i=i; i!=-1; i--)
        {
            cout<<felb[i];
        }
        cout<<endl;
    }
    return 0;
}
