#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T , i , j , k,c=1;
    string s;
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&T);
    while(T--)
    {
        cin>>s>>k;
        bool imp=false;
        int ans=0;
        for(i=0;i<s.length(); i++)
        {
            if(s[i]=='-')
            {
                if(i+k>s.length()){cout<<"Case #"<<c++<<": IMPOSSIBLE"<<endl; imp=true;break;}
               else{
                ans++;
                for(j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
               }
            }
        }
        if(!imp)cout<<"Case #"<<c++<<": "<<ans<<endl;
        else continue;


    }



    return 0;
}
