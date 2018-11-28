#include<bits/stdc++.h>
using namespace std;
const int inf = (1<<28);
int K,len;
int cumSmileCount[1001];
string str;

int main()
{
    ios_base::sync_with_stdio(false);
      freopen("a.in","r+",stdin);
      freopen("a.out","w+",stdout);
    int T,cas=0;
    cin>>T;
    while(T--)
    {
        cin>>str>>K;
        len = str.size();
        int ans = 0;
        for(int i=0;i<len;i++)
        {
            //cout<<str<<endl;
            if(i+K > len) continue;
            if(str[i] == '+') continue;
            ans++;
            for(int j=i;j<i+K;j++){
                if(str[j] == '+') str[j] = '-';
                else str[j] = '+';
            }
        }
        for(auto x : str){
            if(x != '+') ans = inf;
        }
        if(ans<inf)cout<<"Case #"<<++cas<<": "<<ans<<endl;
        else cout<<"Case #"<<++cas<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
