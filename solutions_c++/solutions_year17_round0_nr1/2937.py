#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout;   ifstream cin;
    cout.open("out_large.txt");
    cin.open("large.in");

    int T,k,l,ans,i,j,t;
    cin>>T;
    char s[10005];
    for(t=1;t<=T;t++)
    {
        cin>>s; l=strlen(s);
        cin>>k; ans=0;
        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                if(i<l-k+1)
                {
                    ans++;
                    for(j=i;j<i+k;j++) { s[j]=( (s[j]=='+')?'-':'+'); }
                }
                else{ans=-1; break;}
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ans!=-1){cout<<ans<<"\n";}
        else{cout<<"IMPOSSIBLE\n";}
    }
    return 0;
}
