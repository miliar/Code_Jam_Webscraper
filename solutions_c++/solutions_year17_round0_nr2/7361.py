#include<bits/stdc++.h>

using namespace std;



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output_file.out","w",stdout);

    int T;

    cin>>T;
    int C=1;

    while(T--)
    {
    string s;

    cin>>s;
//    changed[100]={0};
   int pos =s.size();

    for(int i=s.size()-1;i>=1;i--)
    {
        if(s[i-1]>s[i]){
            s[i-1] = s[i-1] -1;
            pos=i;
        }
    }

    for(int i=pos ;i<s.size();i++)
    {
        s[i]='9';
    }

    cout<<"Case #"<<C++<<": ";

    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='0'){continue;}
        cout<<s[i];

    }
    cout<<"\n";

    }


}
