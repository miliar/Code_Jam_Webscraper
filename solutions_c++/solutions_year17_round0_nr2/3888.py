#include<bits/stdc++.h>
using namespace std;
using ll = long long;
string slim;
ll lim;
string ans;
bool dfs(int d,int last,bool over=true)
{
    if( d>=slim.size() )return true;
    int dig = slim[d]-'0';
    int mx = over?dig:9;
    for(int i=mx;i>=last;--i)
    {
        ans.push_back('0'+i);
        if( dfs(d+1,i,over) )return true;
        ans.pop_back();
        over = false;
    }
    return false;
}
int main()
{
    int T,c=1;
    cin>>T;
    while(T--)
    {
        cin>>lim;
        slim=to_string(lim);
        cout<<"Case #"<<c++<<": ";
        ans.clear();
        dfs(0,0);
        cout<< stoll(ans) <<'\n';
    }
}

