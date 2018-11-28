#include <iostream>
#include<string>
using namespace std;
char convert(int pos ,  char n[] , int & length)
{
 if(pos==0&&n[pos]=='1'){length--; for(int i=0;i<length;i++)n[i]='9';}
 else if(n[pos]=='0')
 {
     while(pos!=0&&n[pos]=='0'){
        pos--;
     }
 if(pos==0&&n[pos]=='1'){length--; for(int i=0;i<length;i++)n[i]='9';}
 else {n[pos]--; for(int i=pos+1;i<length;i++) n[i]='9';}
 }
 else {n[pos]--; for(int i=pos+1;i<length;i++) n[i]='9';}
 return true;
}
int main()
{
   freopen("input.txt","r" , stdin);
   freopen("ans.txt","w" , stdout);
    int T; cin>>T;
    for(int w=0;w<T;w++)
    {
       char n[100]; cin>>n;
       int length=strlen(n); bool flag=false;
       for(int i=0;i<length-1;i++)
       {
           if(n[i+1]>=n[i]) continue;
           else {convert(i,n,length); i=-1;}
       }
       cout<<"Case #"<<w+1<<":"<<" ";
       for(int i=0;i<length;i++) cout<<n[i];
       cout<<endl;
    }
}
