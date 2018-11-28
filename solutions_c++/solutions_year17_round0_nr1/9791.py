#include<bits/stdc++.h>
using namespace std;

void flip(string s,int i,int k)
    {
    int j;
    for(j=i;j<i+k;j++)
        {
        if(s[j]=='+')s[j]='-';
        else s[j] ='+'; 
    }
    
}

int main()
    {
    
    int t,b=1;
    string s;
    
    cin>>t;
    
    while(t)
        {
        int k,flag=0;
       cin>>s;
       cin>>k;
        int count=0;
        int i=0;

        cout<<"Case #"<<b<<": ";


        while(flag!=1)
            {
            
            while(s[i]=='+')
                {
                i++;
            }
            
            
            if(i==s.size()) break;
            
            if((s.size()-i)>=k && s[i]=='-')
            {   
        int j;
        for(j=i;j<i+k;j++)
         {
            if(s[j]=='+')   s[j]='-';
            else s[j] ='+'; }
    
                count++;
                //cout<<count<<" "<<s;
            }
            else {
                flag=1;
                cout<<"IMPOSSIBLE"<<"\n";
            }
            i++;
        }
        
       if(flag==0) cout<<count<<"\n";
        
        b++;
        t--;
    }
    
    return 0;
}