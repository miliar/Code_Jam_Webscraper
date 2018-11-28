#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
    int t,i,ans,k,j,g,gg,ans2;
    cin>>t;
    string s,ss;
    for(int tt=1;tt<=t;tt++){
        cin>>s>>k;
        ans=ans2=g=gg=0;
        ss=s;
        for(i=0;i<s.length();i++){
            if(s[i]=='+')
                continue;
            if(i+k<=s.length())
                ans++;
            for(j=i;i+k<=s.length() && j<i+k;j++){
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
            //cout<<s<<" ";
        }

        for(i=ss.length()-1;i>=0;i--){
            if(ss[i]=='+')
                continue;
            if(i-k>=-1)
                ans2++;
            for(j=i;i-k>=-1 && j>i-k;j--){
                if(ss[j]=='-')
                    ss[j]='+';
                else
                    ss[j]='-';
            }
            //cout<<s<<" ";
        }


        //cout<<s;
        for(i=0;i<s.length();i++){
            if(s[i]=='-'){
                g=1;
            }
            if(ss[i]=='-'){
                gg=1;
            }
            if(g && gg){
                cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE\n";
                goto out;
            }
        }
        if(g)
            ans=ans2;
        else if(gg)
            ;
        else
            ans=min(ans,ans2);
        cout<<"Case #"<<tt<<": "<<(ans)<<endl;
        out:
            ;
    }

    return 0;
}
