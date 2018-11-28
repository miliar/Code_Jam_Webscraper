#include<bits/stdc++.h>
using namespace std;
void dig_in_array(vector <int> &a,int dig,long long n)
{long long p=n;
for(int i=dig-1;i>=0;i--)
{
a[i]=p%10;
p=p/10;
}
}
int main()
{
int t;
cin>>t;
for(int ii=1;ii<=t;ii++)
{
long long n,pri=1,pri1;
cin>>n;
int dig=log10(n)+1;
if(dig==1)
{
cout<<"Case #"<<ii<<": ";
cout<<n<<endl;
continue;
}
vector <int> a(dig);

dig_in_array(a,dig,n);
love:
for(int i=0;i<dig-1;i++)
if(a[i]>a[i+1])
{
	a[i]--;
	for(int j=i+1;j<dig;j++)
	a[j]=9;
	break;
}
if(!(is_sorted(a.begin(), a.end())))
{goto love;}
else
{cout<<"Case #"<<ii<<": ";
for(int i=0;i<dig;i++)
if(i==0&&a[i]==0)continue;
else
cout<<a[i];
cout<<endl;
}
}
return 0;
}