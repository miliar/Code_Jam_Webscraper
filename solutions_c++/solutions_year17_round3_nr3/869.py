/*************************************************************************
    > File Name: procsmall.cpp
    > Author: Yuchen Wang
    > Mail: wyc8094@gmail.com 
    > Created Time: Sun Apr 30 17:44:42 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int maxn = 55;

double P[maxn];
int T,K,N;
double U;

int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	int i;
	int ncase = 0;
	cin >> T;
	for(ncase=1;ncase<=T;ncase++){
		printf("Case #%d: ",ncase);
		double sumP = 0.0;
		cin >> N >> K >> U;
		for(i=0;i<N;i++){
			scanf("%lf",&P[i]);
			sumP += P[i];
		}
		double mean = (sumP+U)/K;
		double adjust = 0.0;
		double ans = 1.0;
		int tmp = 0;
		for(i=0;i<N;i++){
			if(P[i] < mean){
				adjust += P[i];
				tmp++;
			}
		}
		adjust = (adjust+U)/tmp;

		for(i=0;i<N;i++){
			if(P[i]>=mean)
				ans *= P[i];
			else
				ans *= adjust;
		}
		printf("%.7f\n",ans);
	}
}

