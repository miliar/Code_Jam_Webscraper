#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  //freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  int tc;cin>>tc;for(int t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<": ";
     
     LL n;
     cin>>n;

     vector<int>v;

     while(n){
     	v.push_back(n%10); 
     	n/=10;
     }

     reverse(v.begin(),v.end());
     
     bool fnf=true;

     for(int i=0;i+1<v.size();i++)
     {  
       if(v[i+1]<v[i]){
       	 if(v[i]==1){
           fnf=false;
           for(int j=0;j+1<v.size();j++)cout<<"9";cout<<endl;
       	 }
       	 else{
            int f=i;
            while((f>=0)&&(v[f]==v[i])){
            	f--;
            }
            f++; v[f]--;
            for(int j=f+1;j<v.size();j++)v[j]=9;
       	 }
       	 break;
       }
     }
    if(fnf){
    	for(int j=0;j<v.size();j++)cout<<v[j];cout<<endl;
    }
  }
          
  return 0;
}