#include<bits/stdc++.h>
using namespace std;
int main()
{ long long t,p,n,k,x,y,a,b,z;
  ifstream fin;
  ofstream fout;
  fin.open("/home/anupam/C-large.in",ios::in);
  fin>>t;
  map<long long,long long>mp;
//cout<<t<<"\n";
  //cout<<mp.begin()->first<<"\n";
fout.open("/home/anupam/cjout.txt",ios::out);
  for(p=0;p<t;p++)
  {
    fin>>n>>k;
    k--;
    mp[n]=1;
    vector<pair<long long,long long> >v;
    v.push_back(make_pair(n,1));
    z=n;
    while(k>0)
    {
    x=v[0].first;
    y=v[0].second;
    //cout<<x<<" "<<y<<" "<<k<<"\n";
    mp.erase(x);
     if(x%2==0)
     {
       a=x/2;
       b=(x-1)/2;
     }
     else
     {
       a=b=x/2;
     }
     if(mp.find(a)!=mp.end())
     {
       mp[a]+=y;
     }
     else
     {
       mp[a]=y;
     }
    if(mp.find(b)!=mp.end())
     {
       mp[b]+=y;
     }
     else
     {
       mp[b]=y;
     }
     v.clear();
     map<long long,long long>::iterator it;
     for(it=mp.begin();it!=mp.end();it++)
     {
       v.push_back(make_pair(it->first,it->second));
     }
     sort(v.rbegin(),v.rend());
     //cout<<v[0].first<<" "<<v[0].second<<" "<<k<<"\n";

     for(long i=0;i<v.size();i++)
     {
       cout<<"hoho"<<v[i].first<<" "<<v[i].second<<"\n";
     }
      if(k<=v[0].second)
      {
        z=v[0].first;
        break;
      }
      else
      {
       k=k-v[0].second;
      }

     for(it=mp.begin();it!=mp.end();it++)
     {
       cout<<"omg"<<it->first<<" "<<it->second<<"\n";
     }
     //break;
    }
    if(z%2==0)
    {
      cout<<z/2<<" "<<(z-1)/2<<"\n";
      fout<<"Case #"<<p+1<<": "<<(z)/2<<" "<<(z-1)/2<<"\n";
    }
    else
    {
      cout<<z/2<<" "<<z/2<<"\n";
      fout<<"Case #"<<p+1<<": "<<(z)/2<<" "<<z/2<<"\n";
    }
    mp.clear();
    v.clear();
  }

return 0;
}
