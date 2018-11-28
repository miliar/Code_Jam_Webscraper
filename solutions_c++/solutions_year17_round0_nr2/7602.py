#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("blarge.in","r",stdin);
  freopen("blarge-out.txt","w",stdout);
  int t; cin>>t;
  for(int test=1;test<=t;test++) {
    string a;
    cin>>a;
    int n=a.length();
    int s[20];
    for(int i=0;i<n;i++){
    	s[i] = (a[i]-'0');
    }
    for (int i=0;i<n-1;i++){
      if(s[i]>s[i+1]){
        s[i]--;
        for(int j=i-1;j>=0;j--) {
          if(s[j]>s[j+1]) {
            s[j]--;
            s[j+1]=9;
          } else {
            break;
          }
        }
        for(i=i+1;i<n;i++) {
          s[i]=9;
        }
      }
    }

    if(s[0]==0) {
      cout<<"Case #"<<test<<": ";
      for(int i=1;i<n;i++) {
      	if(s[i]==0)
      	{
      		cout<<"9";
      	}else {
      		cout<<s[i];
      	}
      }
      cout<<endl;
    } else {
      cout<<"Case #"<<test<<": ";
      for(int i=0;i<n;i++) {
      	if(s[i]==0)
      	{
      		cout<<"9";
      	}else {
      		cout<<s[i];
      	}
      }
      cout<<endl;
    }
  }
}
