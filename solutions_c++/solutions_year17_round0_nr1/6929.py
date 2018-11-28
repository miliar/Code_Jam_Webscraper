//All codes submitted Srivatsa Sinha
#include <bits/stdc++.h>

#define ll long long
#define MAX 1000001
#define ff first
#define ss second
#define MOD 1000000007
#define vi vector<int>
#define vll vector<ll,ll>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define DEBUG cout<<"I am here\n"
#define pb push_back
#define mp make_pair
#define CLEAR_LIST for(int i=1; i<=MAX; i++) adj[i].clear()


using namespace std;

string str;
ll k,BITree[1001],n;
void updateBIT(int index, int val)
{
    index = index + 1;
    while (index <= n)
    {
        BITree[index] += val;
        index += index & (-index);
    }
}
int getQuery(int index)
{
    int sum = 0;
    index = index + 1;
    while (index>0)
    {
        sum += BITree[index];
        index -= index & (-index);
    }
    return sum;
}
void update(int l,int r,int val)
{
    updateBIT(l, val);
    updateBIT(r+1, -val);
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ios_base::sync_with_stdio(false);
    ll t=1,ctr;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
      memset(BITree,0,sizeof(BITree));

      cin>>str>>k;
      n = str.size();
      ctr = 0;
      bool flag = true;
      for(int i=0; i<str.size(); i++)
      {
        if((str[i]=='-' && getQuery(i)%2==0)  || (str[i]=='+' && getQuery(i)%2))
        {
          if(i+k>n) flag = false;
          else
          {
            ctr ++;
            update(i,i+k-1,1);
          }
        }
      }
      if(flag) cout<<"Case #"<<c<<": "<<ctr<<endl;
      else
      cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
