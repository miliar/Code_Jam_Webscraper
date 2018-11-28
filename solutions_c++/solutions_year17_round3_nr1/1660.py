/*************************************************************************
 > File Name: A.cpp
 > Author: makeecat
 ************************************************************************/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
const double PI = acos(-1);
struct Node{
	double R,H;
	bool operator < (const Node &rhs)const{
	//	return (R>rhs.R || (R==rhs.R && H>=rhs.H));
		return (R*H>(rhs.R*rhs.H));
	}
}a[1010],b[1010];
int T;
double ans;
double tmp;
int N,K;
bool flag;
int main(){
	scanf("%d",&T);
	for (int kase=1;kase<=T;kase++){
		scanf("%d%d",&N,&K);
		for (int i=1;i<=N;i++){
			scanf("%lf%lf",&a[i].R,&a[i].H);
		}
		ans = 0;
		tmp=0;
		for (int i=1;i<=N;i++){
			for (int j=1;j<=N;j++){

				b[j].R= a[j].R;
				b[j].H= a[j].H;
			}
			sort(b+1,b+1+N);
			flag = false;
			int cnt = 0;
			ans=PI*a[i].R*(a[i].R+2*a[i].H);
			for (int j=1;j<=N;j++){
				if (cnt==K-1)break;
				if (b[j].R>a[i].R) continue;
				if (b[j].R==a[i].R || b[j].H==a[i].H) {
					if (!flag) {flag=true;continue;}
				}
				cnt++;
				ans+=2*PI*b[j].H*b[j].R;
			}
			if ((cnt==K-1)&&(ans>tmp)) tmp = ans;

		}
		printf("Case #%d: %.9lf\n",kase,tmp);
	}
	return 0;
}
