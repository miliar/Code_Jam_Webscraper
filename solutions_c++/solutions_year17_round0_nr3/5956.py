#include<bits/stdc++.h>
#define N 1005
using namespace std;
int L[N],R[N];

int main(){
  int t;
  cin>>t;

  for(int T=1;T<=t;T++){
    int n,k;
    cin>>n>>k;

    string s=string(n,'.');
      
    int minans=(1e9),maxans=0,cnt=0;
  
    while(k--){
    
      memset(L,0,sizeof(L));
      memset(R,0,sizeof(R));
    
      int l=0;
      for(int i=0;i<n;i++){
	if(s[i]=='.')L[i]=l,l++;
	else l=0;
      }
    
      int r=0;
      for(int i=n-1;i>=0;i--){
	if(s[i]=='.')R[i]=r,r++;
	else r=0;
      }

      int max1=0;
      for(int i=0;i<n;i++)
	max1=max(max1,min(L[i],R[i]));
   
      int max2=0;
      for(int i=0;i<n;i++)
	if(max1==min(L[i],R[i]))
	  max2=max(max2,max(L[i],R[i]));
    
      for(int i=0;i<n;i++){
	if(s[i]=='o')continue;
	if(max1==min(L[i],R[i])&&max2==max(L[i],R[i])){
	  s[i]='o';
	  
	  if(!k){
	    s='o'+s+'o';
	    for(int j=i;j>=0;j--)
	      if(s[j]=='.')cnt++;
	      else{
		minans=min(minans,cnt);
		maxans=max(maxans,cnt);
		break;
	      }
	    cnt=0;
	    for(int j=i+2;j<s.size();j++)
	      if(s[j]=='.')cnt++;
	      else{
		minans=min(minans,cnt);
		maxans=max(maxans,cnt);
		break;
	      }
	    break;
	  }
	  break;
	}
      }
    }
    cout<<"Case #"<<T<<": "<<maxans<<' '<<minans<<endl;
  }
  return 0;
}
