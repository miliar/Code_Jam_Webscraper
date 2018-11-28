#include<bits/stdc++.h>
using namespace std;

int main(){
    int t,i=1;
    cin>>t;
    while(t--)
    {
    list <int> ll;
    list <int>::iterator it;
    int k,n,mi,ma;
    mi=ma=0;
    cin>>k>>n;
    if(k%2==0)
    {
    ll.push_back((k/2)-1);
    ll.push_back(k/2);
    mi=std::min((k/2)-1,(k/2));
    ma=std::max((k/2)-1,(k/2));
    }
    else
    {
    ll.push_back(k/2);
    ll.push_back(k/2);
    mi=ma=k/2;
    }n--;
    while(n--)
    {
       it=ll.begin();
       list <int>::iterator it2=ll.begin();
       for(it=ll.begin(); it!=ll.end(); ++it)
       {    
             if(*it2<*it)
             it2=it;
       }
       if(*it2%2==0)
        {
        ll.insert(it2,((*it2/2)-1));
        ll.insert(it2,(*it2/2));
        mi=std::min((*it2/2)-1,(*it2/2));
        ma=std::max((*it2/2)-1,(*it2/2));
        }
       else
        {
        ll.insert(it2,2,(*it2/2));
        mi=ma=*it2/2;
        }
        ll.erase(it2);
        
   }
   cout<<"Case #"<<i++<<": "<<ma<<" "<<mi<<endl;
   }
return 0;

}
        
    
    
