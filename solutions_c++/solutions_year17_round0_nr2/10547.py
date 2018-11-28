#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>

#define ll unsigned long long int
#define mod 1000000007
using namespace std;

int main()
{
	ll  z,q,l,r,x,t,i,k,j,n,m,c;string s;
cin>>t;x=1;
while(t--)

{
	cin>>s;
	//strcpy(u,sort(s.begin(),s.end()));
	while(!is_sorted(s.begin(),s.end()))
	{n=std::stoi(s);
	n--;s=to_string(n);}
cout<<"Case #"<<x<<':'<<' '<<s<<endl;
		x++;	

}
return 0;
}	
