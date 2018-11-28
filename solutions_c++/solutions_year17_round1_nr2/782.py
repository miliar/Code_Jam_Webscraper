#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <algorithm> // sort
#include <map> // pair
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
        int N,P,R;
        scanf("%d%d",&N,&P);
        int r[N];
        for(int i=0; i<N; i++)
            scanf("%d",&r[i]);
        int q[N][P];
        for(int i=0; i<N; i++)
            for(int j=0; j<P; j++)
                scanf("%d",&q[i][j]);
        int a[N][P],b[N][P];
        for(int i=0; i<N; i++)
            for(int j=0; j<P; j++){
                a[i][j] = ceil(q[i][j]/(1.1*r[i]));
                b[i][j] = floor(q[i][j]/(0.9*r[i]));
                a[i][j] = ceil(q[i][j]*10.0/(11.0*r[i]));
                b[i][j] = floor(q[i][j]*10.0/(9.0*r[i]));
            }
        vector<pair<int, int> > intervals[N];
        for (int i=0; i<N; i++){
            for(int j=0; j<P; j++)
                if(a[i][j]<=b[i][j])
                    intervals[i].push_back(make_pair(b[i][j],a[i][j]));
            sort(intervals[i].begin(),intervals[i].end());
        }
//        for(int i=0; i<N; i++){
//            for(int j=0; j<intervals[i].size(); j++)
//                printf("(%d,%d)",intervals[i][j].second,intervals[i][j].first);
//            printf("\n");
//        }
        int now[N];
        for(int i=0; i<N; i++)
            now[i] = 0;
        int ans=0;
        while(1){
            int finish=0;
            for(int i=0; i<N; i++)
                if(now[i]>=intervals[i].size())
                    finish = 1;
            if(finish)
                break;
            int minb = intervals[0][now[0]].first,argminb=0;
            for(int i=1; i<N; i++)
                if(intervals[i][now[i]].first<minb){
                    minb = intervals[i][now[i]].first;
                    argminb = i;
                }
            int maxa = intervals[0][now[0]].second,argmaxa=0;
            for(int i=1; i<N; i++)
                if(intervals[i][now[i]].second>maxa){
                    maxa = intervals[i][now[i]].second;
                    argmaxa = i;
                }
            if(maxa>minb)
                now[argminb]++;
            else{
                ans++;
                for(int i=0; i<N; i++)
                    now[i]++;
            }
        }
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
