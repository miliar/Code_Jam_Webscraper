#include<bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define fileio freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
int main()
{   
    fileio
    fastio
    int test;
    cin>>test;
    string s;
    for(int t=1;t<=test;t++)
    {
        cin>>s;
        long long len=s.length();
        int pos=1;
        if(s[0]>s[1]) pos=0;
        else{
        while(s[pos]>=s[pos-1])
        {
            pos++;
        }
        }
        if(pos==(len) || (len==1))
        {
            cout<<"Case #"<<t<<": "<<s<<endl;
            continue;
        }
        else{
            while((s[pos]-1) <s[pos-1])
            {
                pos--;
            }
            s[pos]-=1;
            for(int i=pos+1;i<len;i++)
            {
                s[i]='9';
            }
            int j=0;
            while(s[j]=='0') j++;
            string ans;
            //int l=s.copy(ans,len-j,j);
            //ans[l]='\0';
            ans= s.substr(j);
            cout<<"Case #"<<t<<": "<<ans<<endl;
        }

    }
    return 0;
}
