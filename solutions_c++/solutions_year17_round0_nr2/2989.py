#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,br=0;
    string s,n;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>n;
        ///cout<<n<<endl;
        bool x=0;
        s=n;
        br=0;
        for(int h=1; h<s.length(); h++)
            if(s[h]>=s[h-1])
                br++;
        if(br==s.length()-1)
        {
            ///cout<<n<<" ";
            cout<<"case #"<<i+1<<": ";
            cout<<s<<endl;
            x=1;
        }
        if(!x)
            for(int j=n.length()-1; j>=0; j--)
            {
                s=n;
                for(int k=s[j]-1; k>='0'; k--)
                {

                    s[j]=k;
                    for(int h=j+1; h<s.length(); h++)
                        s[h]='9';
                    ///cout<<s<<endl;
                    br=0;
                    for(int h=1; h<s.length(); h++)
                        if(s[h]>=s[h-1])
                            br++;
                    ///cout<<br<<endl;
                    if(br==s.length()-1)
                    {
                        ///cout<<n<<" ";
                        cout<<"case #"<<i+1<<": ";
                        if(s[0]=='0')
                            s.erase(0,1);
                        cout<<s<<endl;
                        x=1;
                        break;
                    }
                }
                if(x)
                    break;
            }
    }
}
