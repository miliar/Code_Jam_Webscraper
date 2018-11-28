#include <bits/stdc++.h>
using namespace std;
int T;
int a[6];
int b[6];
vector<int> v;
string s="ROYGBV";
int tr[6]={
	3,4,5,0,1,2
};
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	cin>>T;
	//cout<<T<<endl;
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		int n;
		cin>>n;
		for(int i=0;i<6;i++)cin>>a[i];
		v.clear();
		v.push_back(a[0]);
		v.push_back(a[2]);
		v.push_back(a[4]);
		sort(v.begin(),v.end());
		int now=0;
		for(;now<6;now+=2)
		{
			if(a[now]==v[2])break;
		}
		int l,r;

		for(l=0;l<6;l+=2)
		{
			if(l==now)continue;
			for(r=0;r<6;r+=2)
			{
				if(r==l||r==now)continue;
				break;
			}
			break;
		}
		
		if(a[now]>a[l]+a[r]){
			puts("IMPOSSIBLE");
			continue;
		}
		if(a[l]<a[r])swap(l,r);//cout<<now<<" "<<l<<" "<<r<<endl;
		if(a[l]==a[now]&&a[l]+a[r]==n)
		{
			for(int i=0;i<a[l];i++)printf("%c%c",s[now],s[l]);
				puts("");
			continue;
		}
		int need=a[now];
		int duo=a[l]+a[r]-need;
		//cout<<duo<<endl;
		for(int i=0;i<a[now];i++)
		{
			printf("%c",s[now]);
			if(duo)
			{
				duo--;
				a[l]--;
				a[r]--;
				printf("%c%c",s[l],s[r]);
			}
			else if(a[l]>a[r]){
					a[l]--;
					printf("%c",s[l]);
				}
				else {
					printf("%c",s[r]);
					a[r]--;
				}
		}
		puts("");
	}
	//while(1);
	return 0;
}