#include <iostream>
#include<fstream>
using namespace std;
typedef unsigned long long ll;
int arr[25];
int main()
{
    ll a, b, n, c, d, e, f=1, t;
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    fin>>t;
//    cin>>t;
    bool yo=true;
    while(f<=t)
    {
//        cin>>n;
        fin>>n;
        for(a=0; a<25; a++)
            arr[a]=0;
        a=n;b=24;
        while(a>0)
        {
            arr[b]=a%10;
            a/=10;
            b--;
        }
        for(a=0; a<25; a++)
            if(arr[a]>0)
                break;
        //A IS THE STARTING POINT
        for(b=a; b<24; b++)
        {
            if(arr[b]>arr[b+1])
            {
                arr[b]--;
                arr[b+1]=9;
                break;
            }
        }
        for(a=b; a<24; a++)
        {
            if(arr[a]>arr[a+1])
                arr[a+1]=9;
        }
        for(a=24; a>=1; a--)
        {
            if(arr[a]<arr[a-1])
            {
                arr[a]=9;
                arr[a-1]--;
            }
        }
        bool yp=true;
//        cout<<"Case #"<<f<<": ";
        fout<<"Case #"<<f<<": ";
        for(a=0; a<25; a++)
        {
            if(arr[a]==0 && yp==true)
                continue;
            else
            {
                yp=true;
//              cout<<arr[a];
                fout<<arr[a];
            }
        }
//        cout<<"\n";
        fout<<"\n";
        f++;
    }
    return 0;
}
