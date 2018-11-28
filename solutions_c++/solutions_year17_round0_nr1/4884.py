#include<iostream>
#include<string>
using namespace std;
#define ll long long int 

int main()
{
    ll t;
    cin>>t;
    ll xx =0;
    
    for(ll i =0;i<t;i++)
    {
        xx++;
        ll n,j,k;
        ll count =0;
         ll flag =1;
        string str,str2;
        str2 = "-";
        cin>>str>>k;
        ll len = str.length();
        for(j = 0;j<str.length();j++)
        {
            if(str.at(j)=='-')
            {
                for(ll x = 0;x<k;x++)
                {
                    if((j+k)>len){break;flag=0;}
                    if(str.at(j+x) =='+'){str.at(j+x)= '-';}
                    else {str.at(j+x)= '+';}
                }
                count++;
            }
            
             std::size_t found = str.find(str2);
             if (found!=std::string::npos)
                { continue;}
            break; 
        }
        //cout<<str<<endl;
        std::size_t found = str.find(str2);
             if (found!=std::string::npos){cout<<"Case #"<<xx<<": "<<"IMPOSSIBLE"<<endl;}
                else {
                    cout<<"Case #"<<xx<<": "<<count<<endl;
                }
    }
}
