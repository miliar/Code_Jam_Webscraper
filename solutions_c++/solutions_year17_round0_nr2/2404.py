#include<iostream> 
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>
#include<cmath>
#define clr(x) memset(x,0,sizeof(x))
using namespace std;
string sub(string a,string b)
{
    string c;
    bool ok=0;
    int len1=a.length();
    int len2=b.length();
    int len=max(len1,len2);
    for(int i=len1;i<len;i++)
        a="0"+a;
    for(int i=len2;i<len;i++)
        b="0"+b;
    if(a<b)
    {
        string temp=a;
        a=b;
        b=temp;
        ok=1;
    }
    for(int i=len-1;i>=0;i--)
    {
        if(a[i]<b[i]) 
        {
            a[i-1]-=1;
            a[i]+=10;
        }
        char temp=a[i]-b[i]+'0';
        c=temp+c;
    }
    int pos=0;
    while(c[pos]=='0' && pos<len) pos++;
    if(pos==len) return "0"; 
    if(ok) return "-"+c.substr(pos);
    return c.substr(pos);
}
int main()
{
  freopen("B-large.in", "r", stdin);  
  freopen("b.txt", "w", stdout);
  int t;
  scanf("%d",&t);
  for(int cas=1;cas<=t;cas++)
  {
    string s;
    cin>>s;
    printf("Case #%d: ",cas);
    int len=s.length();
    int k=-1;
    for(int i=0;i<len-1;i++){
      if(s[i]>s[i+1]){
        k=i; break;
      }
    }
    if(k==-1){
      cout<<s<<endl;
      continue;
    }
    int h=k;
    while(h){
      s[h]=s[h]-1;
      if(s[h]>=s[h-1])
        break;
      else{
        h--;
      }
    }
    if(s[0]>s[1])
    	s[0]=s[0]-1;
    string str="";
    for(int i=0;i<=h;i++)
      str+=s[i];
    //cout<<str<<endl;
    string zz="";
      zz=str;
    for(int i=h+1;i<len;i++)
      zz+='9';
    int w=zz.length();
    string uu="";
    int v=0;
    for(int i=0;i<zz.length();i++)
      if(zz[i]>'0'){
        v=i; break;
      }
    for(int i=v;i<zz.length();i++)
      uu+=zz[i];
    cout<<uu<<endl;

  }
}
