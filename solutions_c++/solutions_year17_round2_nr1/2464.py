#include<bits/stdc++.h>

using namespace std;

int main()
{
freopen("a.in", "r", stdin);
freopen("b.out", "w", stdout);

long long int t,d,s,T,n,k,ans,ansr,i,j,flag=0;
double time,maxtime,speed;
cin>>t;


for(T=1;T<=t;T++)
{
	cin>>d>>n;
	maxtime=0;
	
	for(i=0;i<n;i++)
	{
		cin>>k>>s;
		time = ((d-k)*1.0)/(s*1.0);
		if(time*1000000>maxtime*1000000)
		maxtime = time;
	}
	
	speed = (d*1.0)/(maxtime*1.0);

	printf("Case #%lld: ",T);
	
	printf("%.6f",speed);
	cout<<endl;
}

return 0;
}
