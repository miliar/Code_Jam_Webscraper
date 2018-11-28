
#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;
int main()
{
    freopen("B-small-attempt2.txt","r",stdin);
freopen("output_file_name.out","w",stdout);
    int t;int x;
    cin>>t;
    for(x=1;x<=t;x++)
    {
        unsigned long long int N,ans;
        ans=0;
        cin>>N;
        int a1[20]; int i=0;
        while(N)
        {
            a1[i]=N%10;
            N=N/10;i++;
        }
        i=i-1; // coz an extra increment happened
        int a2[20];int j;
        a2[i]=a1[i];
        for(j=i;j>=1;j--)
        {
            if(a1[j-1]<a1[j])
            {
                int p=a2[j];int q=j; int f=0;
                a2[j]=a2[j]-1;

                 if(a2[q+1]==p)
               {
                while(a2[q+1]==p){
                         a2[q]=9;q++;
                   }
                   f=1;
                }
                if(f==1)
                  a2[q]=a2[q]-1;

               for(int k=j-1;k>=0;k--)
                        a2[k]=9;
                   break;
            }
            a2[j-1]=a1[j-1];
        }
        for(int b=i;b>=0;b--)
           ans=ans*10+a2[b];

        cout<<"Case #"<<x<<": "<<ans<<endl;

    }

    return 0;
}
