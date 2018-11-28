#include<iostream>
using namespace std;
int pancake(string str,int nb,int p,int r)
{
int i=0,j,var=0,k,m=0;
while(i<nb)
{
for(i=0;i<nb;i++)
{
if(str[i]=='-')
{ 
	k=nb-p+1;
if(i>=k)
{
cout<<"Case #"<<r<<":"<<" "<<"IMPOSSIBLE";
cout<<endl;
var=1;
break;
}
j=i;
while(j<i+p)
{
if(str[j]=='+')
{
 str[j]='-';
 }else
 {
 str[j]='+';}
j++;
   }
 m++;
  }
  
  }
    if(var==1)
        break;
    }
    if(var!=1){
    cout<<"Case #"<<r<<": "<<m<<endl;
    }
  
}
int main(){
    string w;
    int t,c=1;
    cin>>t;
    while(c<=t){
    int h;
    cin>>w>>h;
    pancake(w,w.length(),h,c);
    c++;
    }
    return 0;
}
 