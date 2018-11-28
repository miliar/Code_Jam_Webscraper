#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;

int main () {
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        int d,n;
        scanf("%d%d",&d,&n);
        int pos[n+10],speed[n+10];
        double maxtime=0;
        for(int i=0;i<n;i++){
            scanf("%d%d",&pos[i],&speed[i]);
            if(pos[i]<d){
                maxtime=max(maxtime,(double)(d-pos[i])/speed[i]);
            }
        }
        printf("Case #%d: %.6f\n",t,d/maxtime);

    }
	return 0;
}
