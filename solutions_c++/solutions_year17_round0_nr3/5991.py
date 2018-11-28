#include <cstdio>
#include <iostream>
#include <queue>
#define INT long long
using namespace std;
INT n, k, ans1, ans2 = 9876543219876543ll;

void solve(int no)
{
    priority_queue<INT> q;
    cin>>n>>k;
    q.push(n);
    while( k-- )
    {
        INT v = q.top(); q.pop();
        v--;
        ans1 = v/2 + v%2, ans2 = v/2;
        q.push(ans1), q.push(ans2);
    }
    cout<<"Case #"<<no<<": "<<ans1<<" "<<ans2<<endl;
}
int main()
{
    ios::sync_with_stdio(false);
    //freopen("intput.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1 ; i <= t ; i++ ) solve(i);
    return 0;
}


