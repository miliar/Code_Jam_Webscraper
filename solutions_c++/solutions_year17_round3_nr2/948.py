#include <bits/stdc++.h>

using namespace std;

int n,m;
int f[1500];

int a[200][2],b[200][2];
int sum[3];
struct node{
	int x,y,z;
	node(){}
	bool operator<(const node& b)const{
		return x<b.x;
	}
}c[210];

struct stu{
	int x,y;
	stu(int x,int y):x(x),y(y){}
	bool operator<(const stu& b)const{
		return x<b.x;
	}
};

vector<stu> v[2];

int main(){
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&m);
		memset(f,0,sizeof(f));
		sum[0]=sum[1]=720;
		for (int i=0;i<n;i++){
			scanf("%d%d",&a[i][0],&a[i][1]);
			for (int j=a[i][0];j<a[i][1];j++) f[j]=2,sum[1]--;
			c[i].x=a[i][0];
			c[i].y=a[i][1];
			c[i].z=1;
		}
		if (a[0][0]>a[1][0]) swap(a[0],a[1]);
		for (int i=0;i<m;i++){
			scanf("%d%d",&b[i][0],&b[i][1]);
			for (int j=b[i][0];j<b[i][1];j++) f[j]=1,sum[0]--;
			c[n+i].x=b[i][0];
			c[n+i].y=b[i][1];
			c[n+i].z=0;
		}
		if (b[0][0]>b[1][0]) swap(b[0],b[1]);
		int ans=0;
		if (n+m==1) ans=2;
		if (n==2){
			int x=a[1][0]-a[0][1];
			int y=(a[0][0]+1440-a[1][1])%1440;
			//cout << x<<" "<<y<<endl;
			//if (y==0) y=1440;
			//if (x==0) x=1440;
			if (min(x,y)<=sum[1]) ans=2;
				else ans=4;
		}else
		if (m==2){
			int x=b[1][0]-b[0][1];
			int y=(b[0][0]+1440-b[1][1])%1440;
			//if (y==0) y=1440;
			//if (x==0) x=1440;
			if (min(x,y)<=sum[0]) ans=2;
				else ans=4;
		}else if(n+m==2) ans=2;
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}