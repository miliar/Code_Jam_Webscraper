#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<string>
#include <assert.h>
#include<cstring>
#include<vector>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<bitset>
#include<list>
#include<stack>
#define fl(i,s,n) for(i=s;i<n;i++)
#define flr(i,s,n) for(i=s;i>n;i--)
#define ls(i,s) for(i=0;s[i]!='\0';i++)
#define gi(x) scanf("%d",&x)
#define pi(x) printf("%d",x)
#define checkline(x) while(x!='\0' && x!='\n')
#define pt(s) printf(s)
#define PI acos(-1)
#define f_in freopen("input.in","r",stdin)
#define f_out freopen("output.txt","w",stdout)
#define in(i,j,k) ((j<=i) && (i<k))
#define ld long double
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sd3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define fi first
#define se second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define r0 return 0
#define mod 1000000007
#define INF 1e12
#define FS ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define lli long long int
using namespace std;
int prog()
{
    int i,j,k,n,x,y,z;
    priority_queue<int> heap;
    cin>>n>>k;
    heap.push(n);
    fl(i,0,k-1)
    {
        x = heap.top();
        heap.pop();
        y = ((x+1)/2)-1;
        z = (x)-((x+1)/2);
        heap.push(y);
        heap.push(z);
    }
    x = heap.top();
        y = ((x+1)/2)-1;
        z = (x)-((x+1)/2);
    cout<<max(y,z)<<' '<<min(y,z)<<endl;
    r0;
}
int main()
{
    f_in;
    f_out;
    int t,i;
    cin>>t;
    fl(i,1,t+1)
    {
        cout<<"Case #"<<i<<": ";
    prog();
    }
    return 0;
}
