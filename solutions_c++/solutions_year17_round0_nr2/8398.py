#include <iostream>
using namespace std;

int main() {
  int t,sno=1;
  cin>>t;
  while(t--){
    cout<<"Case #"<<sno++<<": ";
    string n;
    cin>>n;
    int l=n.length(),i;
    for(i=l-1;i>0;i--){
      if(n[i-1]>n[i]){
        if(n[i]=='0'){
          n[i-1]--;
          for(int x=l-1;x>i-1;x--)
            n[x]='9';
        }
        else
          n[i]--;
        i=l;
      }
    }
    while(n[i]=='0')
      i++;
    for(;i<l;i++)
      cout<<n[i];
    cout<<"\n";
  }
	return 0;
}
