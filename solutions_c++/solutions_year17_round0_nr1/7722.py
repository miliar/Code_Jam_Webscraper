#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int a=1; a<=t; a++)
    {
        char m[1001];
        int k,c=0,co=0;
        scanf("%s",m);
        cin>>k;
        int l=strlen(m);
        for(int i=0; i<=l-k; i++)
        {
            if(m[i]=='-')
            {
                for(int j=i; j<i+k; j++)
                {
                    if(m[j]=='-')
                    {
                        m[j]='+';
                    }
                else if(m[j]=='+')
                    {
                        m[j]='-';
                    }

                }
                co++;
            }
        }
        for(int i=0; i<l; i++)
        {
            if(m[i]=='-')
            {
                c=99;
                break;
            }
        }
        if(c==99)
        {
            cout<<"case"<<" "<<"#"<<a<<":"<<" "<<"IMPOSSIBLE"<<endl;
        }
        else cout<<"case"<<" "<<"#"<<a<<":"<<" "<<co<<endl;
        ///cout<<co<<endl;
    }
    return 0;
}

