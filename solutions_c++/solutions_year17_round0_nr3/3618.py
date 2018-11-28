#include<bits/stdc++.h>
#include<cstdint>
using namespace std;
#define for1(i,n) for(int i=0;i<(n);i++)
#define for2(j,a,b) for(j=a;j<=b;j++)
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ll long long

#define endl "\n"
//Precice log2 computation taken from stackoverflow
const int tab64[64] = {
    63,  0, 58,  1, 59, 47, 53,  2,
    60, 39, 48, 27, 54, 33, 42,  3,
    61, 51, 37, 40, 49, 18, 28, 20,
    55, 30, 34, 11, 43, 14, 22,  4,
    62, 57, 46, 52, 38, 26, 32, 41,
    50, 36, 17, 19, 29, 10, 13, 21,
    56, 45, 25, 31, 35, 16,  9, 12,
    44, 24, 15,  8, 23,  7,  6,  5};

int log2_64 (uint64_t value)
{
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    value |= value >> 32;
    return tab64[((uint64_t)((value - (value >> 1))*0x07EDD5E59A4E28C2)) >> 58];
}


int main()
{

freopen("input1.txt","r",stdin);
freopen("output1.txt","w",stdout);
ios_base::sync_with_stdio(false);
uint64_t t,x,y,i,j,m,s,k,z,l,r,n,d,pe,po,ans,a,b,mx,mi;

cin>>t;
for(x=1;x<=t;x++)
{
	cin>>n>>k;

z=log2_64(k);
l=pow(2,z);
//r=pow(2,z+1)-1;

//cout<<l<<" "<<r<<endl;


 
if(n%2==0)//even
	pe=1;
else
	pe=0;
for(i=1;i<=z;i++)
{
a=n/pow(2,i-1);
b=n/pow(2,i);
if((a%2==0&&b%2==1) ||(b%2==0&&a%2==1))
	pe=pow(2,i)-pe;



}
a=n/l;
b=a-1;
po=pow(2,z)-pe;
k=k-l+1;
if(a%2==0)
{
if(k<=pe)
	ans=a;
else
	ans=b;

}
else
{

	if(k<=po)
		ans=a;
	else
		ans=b;
}


cout<<"Case #"<<x<<": ";

if(ans%2==0)
	{mx=ans/2;
   mi=mx-1;}
   else
   {
   	mx=ans/2;
   	mi=mx;
   }

cout<<mx<<" "<<mi<<endl;

}




return 0;
}