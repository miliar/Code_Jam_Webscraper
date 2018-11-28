#include<bits/stdc++.h>
using namespace std;
#define for1(i,n) for(int i=0;i<(n);i++)
#define for2(j,a,b) for(j=a;j<=b;j++)
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ll long long




#define endl "\n"
int main()
{
ios_base::sync_with_stdio(false);
int64_t t,x,y,i,j,m,s,k,a[20],l,n,n1;

freopen("input1.txt","r",stdin);
freopen("output1.txt","w",stdout);

cin>>t;
for(x=1;x<=t;x++)
{

cin>>n;
n1=n;
k=0;
while(n1!=0)
{
	a[k++]=n1%10;
	n1=n1/10;

}
reverse(a,a+k);

for(i=1;i<k;i++)
{
if(a[i]>=a[i-1])
	continue;
else
{
	a[i-1]--;

	for(j=i;j<k;j++)
		a[j]=9;
	i-=2;
	
}


}

cout<<"Case #"<<x<<": ";
if(a[0]>0)
	cout<<a[0];

for(i=1;i<k;i++)
cout<<a[i];

cout<<endl;



}

return 0;
}
