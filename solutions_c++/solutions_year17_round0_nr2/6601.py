#include <bits/stdc++.h>
#include<string.h>
#define MOD 1000000009
#define MAXA 10000000000000ll
#define PI 3.14159265358979323846264338327950
//#define INF 0x3f3f3f3f
typedef long long int ll;
using namespace std;
//const int MAXA= 1e15;
const  int maxn=5e5+5;
const int N=1e6+5;
queue<pair<int,int> > q;
vector<int> v;
int main()
{
    freopen("BB.in","r+",stdin);
    freopen("out.txt","w+",stdout);
    int t,i,n;
    for(i=1;i<=9;i++)
        q.push(make_pair(i,i));
    while(!q.empty())
    {
        pair<int,int> p =q.front();
        q.pop();

        int n=p.first;
        if(n>1000)
            continue;
        v.push_back(n);
        int lar=p.second;
        for(i=lar;i<=9;i++)
        {
            q.push(make_pair(n*10+i,i));
        }
    }
    int t1=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int it = lower_bound(v.begin(),v.end(),n)-v.begin();
        if(it==v.size()||v[it]>n)
            it--;
        printf("Case #%d: %d\n",t1,v[it]);
        t1++;
    }
    return 0;

}
