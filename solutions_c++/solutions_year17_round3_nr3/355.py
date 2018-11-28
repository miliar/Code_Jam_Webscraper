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
    int n, k;
    double p, u, fin, addition;
    vector<double> vp;
    
    scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        fin = 0;
        vp.clear();
        
        for (int i=0;i<n;i++) {
            scanf("%lf",&p);
            vp.push_back(p);
        }
        
        sort(vp.begin(),vp.end());
        vp.push_back(1);
        
        int terms = 0;
        for (int i=1;i<=n;i++) {
            terms++;
            if (abs(vp[i]-vp[i-1])<0.000001) {
                continue;
            }
            
            if (terms*(vp[i]-vp[i-1]) > u) {
                addition = u/terms;
                for (int j=i-1;j>=0;j--) {
                    vp[j]+=addition;
                }
                break;
            } else {
                u -= terms*(vp[i]-vp[i-1]);
                addition = (vp[i]-vp[i-1]);
                
                for (int j=i-1;j>=0;j--) {
                    vp[j]+=addition;
                }
                if (u<0) break;
            }
        }
        
        fin=1;
        for (int i=0;i<n;i++) {
            fin *= vp[i];
        }
        if (fin>1) fin = 1;
        
        printf("Case #%d: %.9lf\n",t,fin);
    }
}