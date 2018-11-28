#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
char v[2010];
int main()
{
    int n,t,i,j,k;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        cin>>(v+1)>>k;
        int nr=0;
        n=strlen(v+1);
        for(int p=1;p<=10;p++)
        {
            for(i=1;i<=n-k+1;i++)
            {
                if(v[i]=='-')
                {
                    for(j=i;j<i+k;j++)
                    {
                        if(v[j]=='-') v[j]='+';
                        else v[j]='-';
                    }
                    nr++;
                }
            }
        }
        int ok=0;
        for(i=1;i<=n;i++) if(v[i]=='-') ok=1;
        cout<<"Case #"<<q<<": ";
        if(ok==1) cout<<"IMPOSSIBLE\n";
        else cout<<nr<<"\n";
    }
}
