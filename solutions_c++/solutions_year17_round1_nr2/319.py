#include <bits/stdc++.h>

using namespace std;
bool test(vector<int> & v,int p)
{
   for(int i=0;i<v.size();i++)
   {
      if(v[i]>=p)return 0;
   }
   return 1;
}
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
       int n,p;
       cin>>n>>p;
       vector<int> need(n);
       for(int i=0;i<n;i++)
       {
          cin>>need[i];
       }
       int x;
       vector<vector<pair<int,int> > > packs(n,vector<pair<int,int> >(p));
       vector<int> pos(n);
       for(int i=0;i<n;i++)
       {
          for(int j=0;j<p;j++)
          {
             cin>>x;
             int st=1e9,en=0;
             for(int z=1;z<=1e6;z++)
             {
                if(10ll*x>=need[i]*9ll*z&&x*10ll<=need[i]*11ll*z)
                {
                   st=min(st,z);
                   en=max(en,z);
                }
             }
               packs[i][j].first=st;
               packs[i][j].second=en;
               //cout<<st<<' '<<en<<endl;
            // cout<<packs[i][j].first<<' '<<packs[i][j].second<<endl;
          }
       }
       for(int i=0;i<n;i++)
       {
          sort(packs[i].begin(),packs[i].end());
       }
       int ans=0;
       if(n==1)
       {
          for(int i=0;i<p;i++)
          {
             int l=packs[0][i].first;
             int r=packs[0][i].second;
             if(l<=r)ans++;
          }
       }
       else
       {
          vector<int> pos(n);
          for(int i=0;i<p&&test(pos,p);)
          {
             int l=packs[0][i].first;
             int r=packs[0][i].second;
             int cl=l;
             int dec=0;
             for(int j=1;j<n;j++)
             {
                l=max(packs[j][pos[j]].first,l);
                r=min(packs[j][pos[j]].second,r);
             }
             if(l<=r)
             {
                i++;
                for(int k=1;k<n;k++)
                {
                   pos[k]++;
                }
                ans++;
                continue;
             }
             int kek=0;
             for(int k=1;k<n;k++)
             {
                if(packs[k][pos[k]].first<=cl)
                {
                   cl=packs[k][pos[k]].first;
                   kek=k;
                }
             }
             if(kek==0)
             {
                i++;
             }
             else
             {
                pos[kek]++;
             }
          }
       }
       cout<<"Case #"<<o<<": "<<ans<<'\n';


    }
    return 0;
}
