#include <bits/stdc++.h>
#define int long long int
using namespace std;

string maxt(string a, string b)
{
    if(a.length()==b.length())return max(a,b);
    return a.length()>b.length()?a:b;
}

#undef int
int main() 
{
#define int long long int

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int t;
    cin>>t;
    for(int tc = 1; tc<=t;tc++)
    {
        string n;
        cin>>n;
        int l = n.length();
        if(l==1)
        {
            cout<<"Case #"<<tc<<": "<<n<<endl;
            continue;
        }
        bool b = true;
        for(int i = 0;i<l-1;i++)
            if(n[i]>n[i+1])
                b = false;
        string ans = b?n:string(l-1,'9');
        for(int i = l-1;i>=0;i--)
        {
            string temp = n;
            int j = l-1;
            for(;j>i;j--)
                temp[j] = '9';
            if(i!=l-1)temp[j--]--;
            for(j = min(j,l-2);j>=0;j--)temp[j] = min(temp[j], temp[j+1]);
            ans = maxt(ans, temp);
        }
        int x = 0;
        for(;ans[x]=='0';x++);
        cout<<"Case #"<<tc<<": ";
        for(;x<l;x++)
            cout<<ans[x];
        cout<<endl;
    }
    
    return 0;
}