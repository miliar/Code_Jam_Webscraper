#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

typedef struct {
	long double k;
	long double s;
	long double dst;
} Horse;

bool sortfunc(const pair<int,char>& a, const pair<int,char>& b) {
	return a.first > b.first;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T, N, R, O, Y, G, B, V;
	vector<pair<int,char> > v(3);
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
		scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
		v[0].first=R;
		v[0].second='R';
		v[1].first=Y;
		v[1].second='Y';
		v[2].first=B;
		v[2].second='B';
		
		
		if (R<=Y+B && Y<=R+B && B<=R+Y) {
			printf("Case #%d: ",t);
			sort(v.begin(),v.end(),sortfunc);
			for (int i=0;i<v[0].first;i++) {
				printf("%c",v[0].second);
				if (v[1].first) {
					printf("%c",v[1].second);
					v[1].first--;
				}
				if (v[0].first-v[2].first<=i) {
					printf("%c",v[2].second);
				}
			}
			printf("\n");
		} else {
			printf("Case #%d: IMPOSSIBLE\n",t);;
		}
	}
}