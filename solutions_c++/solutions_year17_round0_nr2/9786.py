#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fast    ios_base::sync_with_stdio(0)
#define ull unsigned long long int
#define pb  push_back
#define mp  make_pair
#define ll long long int
#define all(v)  v.begin(),v.end()
typedef pair<int,int> pii;
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> BTREE;

 
 void codejam(int x,int y,bool haa)
 {      if(!haa)
        {
            printf("Case #%d: IMPOSSIBLE\n",x);
            return;

        }
        printf("Case #%d: %d\n",x,y);
    

 }
 
 vector<int> data;
 
 void solve(int number,int sze,int prev)
 { 
    if(sze==3)
    {
        data.pb(number);
        return;

    }
    else
    {
        int start=prev;
        data.pb(number);

        if(number==0)start+=1;
        for(int i=start;i<=9;i++)
        {
            solve(number*10+i,sze+1,i);

        }
    }
 }
 int main()
 {
    solve(0,0,0);
    sort(data.begin(),data.end());
   int t;
   cin>>t;
   int testcase=1;
   while(t--)
   {
    int n;
    cin>>n;
    int idx=upper_bound(data.begin(),data.end(),n)-data.begin();
    codejam(testcase++,data[idx-1],true);

   }
 }