#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#define PI acos(-1)
using namespace std;
int a[1001][1001];
int n,m,c;
int main()
{

	freopen("B-small-attempt0.in","r",stdin);
	freopen("bs","w",stdout);
	int T;
	cin>>T;


	for(int cs=1;cs<=T;cs++){
		cin>>n>>c>>m;
		for(int i=0;i<1000;i++){
			for(int j=0;j<1000;j++){
				a[i][j]=0;
			}
		}
		int tn,tc;
		for(int i=0;i<m;i++){
			cin>>tn>>tc;
			a[tc-1][tn-1]++;
		}
		int ans=0,change=0;
		int yu=0;
		int wei=1;
		int ma =0;
		for(int i=0;i<c;i++){
				ma=0;
			for(int j=0;j<n;j++){
				ma+=a[i][j];
			}
			ans = max(ans,ma);

		}
		//cout<<ans<<endl;
		//yu=ans;
		for(int i=0;i<n;i++){
				int now =0;
			for(int j=0;j<c;j++){
				now+=a[j][i];
			}

			now=now-ans;

			if(now<=0){
				yu=yu-now;

			}else{
				now-=yu;
				change+=yu;
				if(now<0){
					yu=-now;
					change-=yu;
				}
				else{
					ans+=(now+wei-1)/wei;
					change+=now-((now+wei-1)/wei);
					yu=wei-(now%wei);
					if(yu==wei)yu=0;
				}
			}
			wei++;
		}
				printf("Case #%d: %d %d\n",cs,ans,change);
		}

	return 0;
}
