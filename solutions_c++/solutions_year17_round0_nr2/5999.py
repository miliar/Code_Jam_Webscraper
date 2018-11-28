#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,c=1;
    long long n,i,j,x,z,y;
    cin>>t;
    while(t>0)
    {
        cout<<"Case #"<<c<<": ";
        ++c;
        cin>>n;
        x=y=log10(n);
        int s[x+1];
        z=n;
        while(z>0)
        {
            s[x]=z%10;
            --x;
            z=z/10;
        }
        
        x=y;
        
        for(i=x-1;i>=0;--i)
        {
            if(s[i]>s[i+1])
            {
                for(j=i+1;j<=x;++j)
                s[j]=9;
                
                if(s[i]!=0)
                --s[i];
                
                else
                {
                    j=i;
                    while(s[j]==0)
                    {
                        s[j]=9;
                        --j;
                    }
                    s[j]=s[j]-1;
                    i=j;
                }
            }
        }
        
        for(i=0;i<=x;++i)
        if(s[i]!=0)
        break;
        
        for(;i<=x;++i)
        cout<<s[i];
        cout<<endl;
        --t;
    }
	return 0;
}

