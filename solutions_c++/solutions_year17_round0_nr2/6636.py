#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,l;
    string n;
    char prev;
    cin>>t;
    for(int _=0;_<t;_++)
    {
        cin>>n;
        l=n.length();
        prev=n[l-1];
        for(int i=l-2;i>=0;i--)
        {
            if(n[i]>prev)
            {
                n[i]--;
                for(int j=i+1;j<l&&n[j]!='9';j++)
                    n[j]='9';
            }
            prev=n[i];
            
        }
        
        if(n[0]=='0')
            n.erase(0,1);
        cout<<"Case #"<<_+1<<": "<<n<<"\n";
    }
            
    return 0;
}
