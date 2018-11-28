#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    string n;
    cin >> T;
    while(T--)
    {
        cout << "Case #" << ++cas << ": ";
        cin >> n;
        string res;
        res+=n[0];
        int i=1;
        for(;i<n.size()&&n[i-1]<=n[i];i++)
            res+=n[i];
        if(res.size()<n.size())
        {

        int j=res.size()-1;
        while(j&&res[j]==res[j-1]) j--;
//        if(j==0||res[j]==res[j-1])
        res=res.substr(0,j)+char(res[j]-1);
        int k=(n.size()-1-j);
        while(k--) res+='9';
        }
        if(res[0]=='0') res=res.substr(1,res.size()-1);
        cout << res <<endl;
    }
    return 0;
}
