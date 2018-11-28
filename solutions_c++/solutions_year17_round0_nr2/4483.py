#include<bits/stdc++.h>
#include <bits/stdc++.h>
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
long long int n;
cin>>n;
long long int x=n;
int len=0,a[20];
while(x)
{
a[len]=x%10;
len++;
x/=10;
}
for(int i=len-1;i>0;i--)
{
 if(a[i]>a[i-1])
 {
  for(int j=i-1;j>=0;j--) a[j]=9;
  a[i]--; i=len;
 }

}
int i=len-1;
 while(i>=0 && a[i]==0) { i--; continue;}
cout<<"Case #"<<z<<": ";
 for(;i>=0;i--)
 cout<<a[i];
 cout<<endl;
z++;
}
 return 0;
}
