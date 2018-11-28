#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{

    long long t;
    cin>>t;
    for(long r=1;r<=t;r++)
    {
        string v;
        cin>>v;

        if(v.size()<2)
        {
            cout<<"Case #"<<r<<": "<<v<<endl;
            continue;
        }
        int i,j;
        while(!is_sorted(v.begin(),v.end()))
        {
            for(i=0;i<v.size()-1;i++)
            {   
                if(v[i]>v[i+1])
                {
                    v[i]=v[i]-1;
                    for(int z=i+1;z<v.size();z++)  
                    v[z]= '9';
                    
                }
            }
        }
       if(v[0]=='0')
        {
            cout<<"Case #"<<r<<": ";
            for(i=1;i<v.size();i++)    
            cout<<v[i];
            cout<<endl;
        }
        else
        {
            cout<<"Case #"<<r<<": ";
            for(i=0;i<v.size();i++)    
            cout<<v[i];
            cout<<endl;
        }

    }
    return 0;
}