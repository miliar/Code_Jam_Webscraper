#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define f first
#define s second
#define pb push_back
#define mi 100000007
#define try int t;cin>>t; while(t--)
typedef long long llu;
typedef vector<int> vi;

int main()
{
    int bulb=1;
    try
    {
        llu nim; cin>>nim;
        vector<int> alu(19);
        for(int imp=0;imp<=18;imp++)
            alu[imp]='$';
        int jin =0;
        while(nim!=0)
        {
            alu[jin]=nim%10;
            nim=nim/10;
            jin++;
        }
        int gop=0;
        for(int ip=1;ip<jin;ip++)
        {
            if(alu[ip]>alu[ip-1])
            {
                alu[ip]=alu[ip]-1;
                for(int k=0;k<=ip-1;k++)
                   alu[k]=9;
                }
        }

        for(int ip=jin-1;ip>=0;ip--)
        {
            if(alu[ip]==0)
            gop++;
            else
                break;
        }
        cout<<"Case #"<<bulb<<": ";
        bulb++;
        for(int iv=jin-1-gop;iv>=0;iv--)
        {
          cout<<alu[iv];
        }
        cout<<endl;
    }
}
