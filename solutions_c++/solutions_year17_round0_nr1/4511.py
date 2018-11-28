#include<bits/stdc++.h>
using namespace std;

int main() {
 // your code goes here
 freopen("C:\\Users\\hp\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\hp\\Desktop\\output.txt","w",stdout);
int t;
cin>>t;
int z=1;
while(t--)
{
 string s;
 cin>>s;
 int n=s.length();
 int x;
 cin>>x;
 int ans=0,f=0;
 for(int i=0;i<n;i++)
 { if(s[i]=='-')
  {
   if(i+x>n) { f=1;   break;}
   for(int j=i;j<i+x;j++)
   { if(s[j]=='-') s[j]='+';
    else s[j]='-';
   }
   ans++;
  }
 }
 if(f==1) cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
 else cout<<"Case #"<<z<<": "<<ans<<endl;
z++;
  }
 return 0;
}
