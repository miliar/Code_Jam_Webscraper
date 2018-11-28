#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int a=1;a<=t;a++)
    {
        string n;
        cin>>n;
        int l=n.length();
        for(int b=l-1;b>0;b--)
        {
            if(n[b]<n[b-1])
            {
                n[b-1]--;
                for(int c=b;c<l;c++)
                    n[c]='9';
            }
        }
        string s="";
        for(int x=0;x<l;x++)
            if(n[x]!='0')
            {
                for(int y=x;y<l;y++)
                    s+=n[y];
                break;
            }
        cout<<"Case #"<<a<<": "<<s<<"\n";
    }
}
