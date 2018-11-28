#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <queue>
#include <map>
#define PI 3.14159265358979323846

using namespace std;


bool sortfunc(const pair<int,int>& a, const pair<int,int>& b) {
    if (a.first==b.first) {
        return a.second>b.second;
    }
    return a.first > b.first;
}

double surfaceArea(int radius) {
    return PI*radius*radius;
}

double heightArea(int radius, int height) {
    return 2*PI*radius*height;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T=0;
    int n, k, a, b;
    double answer;
    vector< pair<int,int> > v(1001);
    double dp[1001][1001];
    
    scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
        scanf("%d%d",&n,&k);
        
        for (int i=0;i<n;i++) {
            scanf("%d%d",&a,&b);
            v[i].first=a;
            v[i].second=b;
        }
        
        sort(v.begin(),v.begin()+n,sortfunc);
        
        fill(dp[0],dp[0]+k,0);
        
        for (int i=1;i<=n;i++) {
            dp[i][0] = 0;
            dp[i][1] = heightArea(v[i-1].first,v[i-1].second) + surfaceArea(v[i-1].first);
            //printf("----%lf\n",dp[i][1]);
            for (int j=2;j<=k;j++) {
                dp[i][j] = -1;
                for (int kk=j-1;kk<i;kk++) {
                    dp[i][j] = max(dp[i][j],dp[kk][j-1]+heightArea(v[i-1].first,v[i-1].second));
                }
            }
        }
        
        answer = -1;
        for (int i=k;i<=n;i++) {
            answer = max(answer,dp[i][k]);
        }
        
        printf("Case #%d: %.9lf\n",t,answer);
    }
}