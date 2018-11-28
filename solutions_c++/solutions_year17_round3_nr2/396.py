#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

#define MAXN 205

struct node{
	int st,nd;
	bool f;
} a[MAXN];

bool cmpNode(node a,node b) {
	return a.st<b.st;
}

struct seg{
	int idx, len;
	seg(int t1,int t2):idx(t1),len(t2){}
};

bool cmpSeg(seg a,seg b){
	return a.len<b.len;
}


void solve() {
	int n,n1,n2;
	scanf("%d%d",&n1,&n2);
	n = n1+n2;
	int rem = 720;
	for (int i=0;i<n1;i++) {
		scanf("%d%d",&a[i].st,&a[i].nd);
		a[i].f=1;
		rem -= (a[i].nd-a[i].st);
	}
	for (int i=n1;i<n1+n2;i++) {
		scanf("%d%d",&a[i].st,&a[i].nd);
		a[i].f=0;
	}
	sort(a,a+n,cmpNode);
	//cerr<<"rem = "<<rem<<endl;

	vector<seg> connect, cut, fit;
	connect.clear();
	cut.clear();
	fit.clear();
	int fit_sum = 0;
	for (int i=1;i<n;i++) {
		if (a[i-1].f && a[i].f) {
			connect.push_back(seg(i-1,a[i].st-a[i-1].nd));
		}
		if (!a[i-1].f && !a[i].f) {
			cut.push_back(seg(i-1,a[i].st-a[i-1].nd));
		}
		if (!a[i-1].f && a[i].f || a[i-1].f && !a[i].f) {
			fit.push_back(seg(i-1,a[i].st-a[i-1].nd));
			fit_sum += (a[i].st-a[i-1].nd);
		}
	}
	if (a[0].f && a[n-1].f) {
		connect.push_back(seg(n-1,a[0].st+1440-a[n-1].nd));
	}
	if (!a[0].f && !a[n-1].f) {
		cut.push_back(seg(n-1,a[0].st+1440-a[n-1].nd));
	}
	if (!a[0].f && a[n-1].f || a[0].f && !a[n-1].f) {
		fit.push_back(seg(n-1,a[0].st+1440-a[n-1].nd));
		fit_sum += (a[0].st+1440-a[n-1].nd);
	}
	//cerr<<"fit_sum = "<<fit_sum<<endl;
	//cerr<<(bool)a[0].f<<endl;
	//cerr<<(bool)a[1].f<<endl;
	sort(connect.begin(),connect.end(),cmpSeg);
	sort(cut.begin(),cut.end(),cmpSeg);

	int num = n1;
	for (int i=0;i<connect.size();i++) {
		if (rem==0) break;
		if (connect[i].len<=rem) {
			rem -= connect[i].len;
			num--;
			//cerr<<"len = "<<connect[i].len<<endl;
			//cerr<<"rem = "<<rem<<endl;
		}
		else {
			rem = 0;
			break;
		}
	}
	if (rem>0) {
		if (rem<=fit_sum) {
			rem = 0;
		}
		else {
			rem -= fit_sum;
			for (int i=cut.size()-1;i>=0;i--) {
				if (rem==0) break;
				if (cut[i].len<=rem) {
					rem -= cut[i].len;
					num++;
				}
				else {
					rem = 0;
					num++;
					break;
				}
			}
		}
	}
	cout<<num*2<<endl;
	connect.clear();
	cut.clear();
	fit.clear();
}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}