#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;


int main()
{
    ifstream ifile("A-small-attempt0.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        int arr[5]={0};
        int n,p;
        cin>>n>>p;
        for(int i=0;i<n;i++)
        {
            int a;
            cin>>a;
            arr[a%p]++;
        }

        int ans=0;
        ans+=arr[0];

        if(p==3)
        {

            int d=min(arr[1],arr[2]);
            ans+=d;
            arr[1]-=d;
            arr[2]-=d;
            ans+=(arr[1]+arr[2]+2)/3;
        }
        else if(p==2)
        {
            ans+=(arr[1]+1)/2;
        }
        /*else if(p==4)
        {
            int d=min(arr[1],arr[3]);
            ans+=d;
            ans+=arr[2]/2;
            arr[2]=arr[2]%2;
            arr[1]-=d;
            arr[2]-=d;

            ans+=(arr[1]+arr[3]+2)/3;
        }*/
                cout<<"case #"<<fff<<": "<<ans<<"\n";
    }
    return 0;
}
