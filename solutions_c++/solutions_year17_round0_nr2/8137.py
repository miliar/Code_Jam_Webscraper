#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t,n=1;
    bool inn;
    string v;
    cin>>t;
    while(t--)
    {
        cin>>v;
  	//cout<<v;
        inn=true;
        
        while(inn)
        {
        	
            inn=false;
            for(int i=1;i<v.size();i++)
                if(v[i]<v[i-1])
                {
                    inn=true;
                    for(int z=i;z<v.size();z++)
                        v[z]='9';
                    v[i-1]--;
                    break;
                }
        }
    	cout<<"Case #"<<n++<<": ";
        int j=0;
        while(v[j]=='0')
            j++;
        for(;j<v.size();j++)
            cout<<v[j];
        cout<<"\n";
        
    }
    
    return 0;
}