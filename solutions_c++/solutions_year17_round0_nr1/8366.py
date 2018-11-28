#include <iostream>
using namespace std;

int main() {
  int t,k,sno=1;
  string s;
  cin>>t;
  while(t--){
    cout<<"Case #"<<sno++<<": ";
    cin>>s>>k;
    int l=s.length();
    int i=0,j=l-1,ans=0;
    while(i<=j){
      if(s[i]=='-'){
        if(i+k>l)
          i=l-k;
        for(int x=i;x<i+k;x++){
          if(s[x]=='-')
            s[x]='+';
          else
            s[x]='-';
        }
        ans++;
        i=-1,j=l;
        if(ans==1000)
          break;
      }
      if(s[j]=='-'){
        if(j-k<-1)
          j=k-1;
        for(int x=j;x>j-k;x--){
          if(s[x]=='+')
            s[x]='-';
          else
            s[x]='+';
        }
        ans++;
        i=-1,j=l;
        if(ans==1000)
          break;
      }
      i++;
      j--;
    }
    if(ans==1000)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<ans<<"\n";
  }
	return 0;
}
