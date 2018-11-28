#include <iostream>
using namespace std;

int main() {
        ios_base::sync_with_stdio(false); cin.tie(0);
        freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
        int t;cin>>t;
        for(int z=1;z<=t;z++)
        {string s;
        cin>>s;
        int l=s.length();
        for(int i=l-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {s[i]--;
            for(int j=i+1;j<l;j++)
            s[j]='9';
            }
        }
        int k;
        for(k=0;k<l;k++)
        if(s[k]!='0')break;
        string s1=s.substr(k);
        
        cout<<"Case #"<<z<<": "<<s1<<endl;
        
        }
        
}
