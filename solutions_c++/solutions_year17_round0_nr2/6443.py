#include<bits/stdc++.h>
using namespace std;
int main()
{
ios_base::sync_with_stdio(0);
long long testcases;
char n[100];
long long caseNum=0,i,l,j,x,check;
freopen("INPPP.in","r",stdin);
freopen("Lar.txt","w",stdout);
cin>>testcases;
while(testcases--)
{
cin>>n;
caseNum++;
l=strlen(n);
check=0;
for(j=0;j<18;j++)
{
check=0;
for(i=0;i<l;i++)
{
if(n[i+1]<n[i] && check==0 && i!=l-1)
{
check=1;
n[i]=n[i]-1;
}
else if(check==1)
n[i]='9';

}
}
x =atoll(n);
cout<<"Case #"<<caseNum<<": "<<x<<endl;

}
return 0;


}
