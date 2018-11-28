#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

int main() {
	int T,t,n,p,i,s,x,a[4];
	cin>>T;
	for (t=1;t<=T;t++) {
		cin>>n>>p;
		memset(a,0,sizeof(a));
		for (i=0;i<n;i++) {
			scanf("%d",&x);
			a[x%p]++;
		}
		s=a[0];
		if (p==2) {
			if (a[1]%2==0) {
				s+=a[1]/2;
			}
			else {
				s+=a[1]/2+1;
			}
		}
		else if (p==3) {
			x=min(a[1],a[2]);
			s+=x;
			x=(a[1]==x?a[2]-x:a[1]-x);
			if (x%3==0) {
				s+=x/3;
			}
			else {
				s+=x/3+1;
			}
		}
		else {
			x=min(a[1],a[3]);
			s+=x;
			a[1]-=x;
			a[3]-=x;
			s+=a[2]/2;
			a[2]%=2;
			if (a[1]==0) {
				x=a[3];
			}
			else {
				x=a[1];
			}
			//x and a[2]
			if (a[2]>0 && x>=2) {
				a[2]=0;
				x-=2;
				s++;
			}
			s+=x/4;
			x%=4;
			if (x>0 || a[2]>0) {
				s++;
			}
		}
		printf("Case #%d: %d\n",t,s);
	}
    return 0;
}
