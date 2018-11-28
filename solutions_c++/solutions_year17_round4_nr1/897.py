#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#define PI acos(-1)
using namespace std;
int a[101];
int p[5];
int n,pp;
int main()
{

	freopen("A-large.in","r",stdin);
	freopen("al","w",stdout);
	int T;
	cin>>T;


	for(int cs=1;cs<=T;cs++){
		cin>>n>>pp;
		for(int i=0;i<4;i++){
			p[i]=0;
		}
		for(int i=0;i<n;i++){
			cin>>a[i];
			p[a[i]%pp]++;
		}
		int ans=0;
		ans+=p[0];
		if(pp==2){
			ans+=(p[1]+1)/2;
		}else if(pp==3){
			if(p[1]>p[2]){
				swap(p[1],p[2]);
			}
			ans+=p[1];
			ans+=(p[2]-p[1]+2)/3;

		}
		else {
			ans+=(p[2]/2);
			if(p[1]>p[3]){
				swap(p[1],p[3]);
			}
			ans+=p[1];
			p[3]=p[3]-p[1];
			if(p[2]%2!=0){
				ans++;
				p[3]-=2;
			}
			if(p[3]>0){
				ans+=(p[3]+3)/4;
			}
		}

		printf("Case #%d: %d\n",cs,ans);


	}


	return 0;
}
