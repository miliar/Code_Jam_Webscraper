#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
void solve(int no)
{
    cout<<"Case #"<<no<<": ";
    int k, ans = 0;
    string s;
    cin>>s>>k;
    for(int i = 0 ; i <= s.size()-k ; i++)
    {
        if( s[i] == '-' )
        {
            ans++;
            for(int j = i ; j < i+k ; j++ )
                if( s[j] == '-' ) s[j] = '+';
                else s[j] = '-';
        }
    }
    for(int i = 0 ; i < s.size() ; i++ )
        if( s[i] == '-' )
        {
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
    cout<<ans<<endl;
    return;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++ ) solve(i);
    return 0;
}
