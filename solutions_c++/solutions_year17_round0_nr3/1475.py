#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  //freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  LL tc;cin>>tc;for(LL t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<": ";
     
     LL n,k;
     cin>>n>>k;
 
     LL res=1,i=1;

     map<LL,LL>m; m[n]=1;

     while(res<k){
        map<LL,LL>tmp;
        map<LL,LL>::iterator it,it1;

        for(it=m.begin();it!=m.end();it++)
        {
          LL cur=(it->first);
          if(cur&1){
             tmp[(cur-1)/2]+=2*(it->second);
          }
          else{
          	 LL u=(cur/2)-1;
             tmp[u]+=it->second;
             tmp[u+1]+=it->second;
          }
        }

        m.clear();
        
        for(it1=tmp.begin();it1!=tmp.end();it1++){
        	if((it1->first) >0){
        		m[it1->first]+=it1->second;
        	}
        }

        tmp.clear();

     	res+=(1ll<<i);
     	i++;
     }
     	i--;
     	res-=(1ll<<i);
     k-=res;
     map<LL,LL>::reverse_iterator r;
     for(r=m.rbegin();r!=m.rend();r++){
           k-=r->second;
           if(k<=0){
           	 LL cur=r->first;
           	 if(cur&1){
               cout<<cur/2<<" "<<cur/2<<endl;
           	 }
           	 else{
                cout<<(cur/2)<<" "<<(cur/2)-1<<endl;
           	 }
           	 break;
           }
     }
  }
          
  return 0;
}