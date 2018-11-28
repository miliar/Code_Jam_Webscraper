#include<bits/stdc++.h>

using namespace std;


int main()
{
    freopen("A-large(2).in","r",stdin);
    freopen("output_file1.out","w",stdout);

    int T;
    cin>>T;
    int C=1;
    while(T--)
    {
    string s;

    int k;
    cin>>s>>k;
    int flag=0;
    int step=0;
    for(int i=0;i<s.size();)
    {
        if(s[i]=='+'){i++;continue ;}

        if(i+k>s.size()){flag=1;break;}

        int next=i+1;

        for(int j=i;j<i+k;j++)
        {
            if(s[j]=='-'){s[j]='+';}
            else if(s[j]=='+') { s[j]='-'; next= min(next,j);}
        }
//        cout<<s<<"\n";
        step++;
        i= next;

    }
    cout<<"Case #"<<C++<<": ";
    if(flag){cout<<"IMPOSSIBLE\n";}
    else cout<<step<<"\n";

    }

}
