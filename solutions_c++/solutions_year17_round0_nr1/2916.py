#include<iostream>
#include<string>
using namespace std;
#define ll long long int 

int main()
{
    ll t;
    cin>>t;
    ll value =0;for(ll i =0;i<t;i++ ){value++;
        ll n,j,k;
        ll count =0;
         ll flag =1;
        string wire,dusrawala;
        dusrawala = "-";
        cin>>wire>>k;
        ll lambai = wire.length();
        for(j = 0;j<wire.length();j++)
        {  if(wire.at(j)=='-')
            {
                for(ll x = 0;x<k;x++)
                {
                    if((j+k)>lambai){break;flag=0;}
                    if(wire.at(j+x) =='+'){wire.at(j+x)= '-';}
                    else {wire.at(j+x)= '+';}
                }
                count++; }
             std::size_t found = wire.find(dusrawala);
             if (found!=std::string::npos)
                { continue;}
            break;  }
        //cout<<wire<<endl;
        std::size_t found = wire.find(dusrawala);
             if (found!=std::string::npos){cout<<"Case #"<<value<<": "<<"IMPOSSIBLE"<<endl;}
                else {
                    cout<<"Case #"<<value<<": "<<count<<endl;
                }
    }
}
