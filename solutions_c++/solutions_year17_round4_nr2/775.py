#include<stdio.h>
#include<vector>
#include<algorithm>
#define MAX 1000000007
#define NODE 2020
#define HALF = (NODE/2)
#define QLEN 1000000
int con[NODE][NODE],cost[NODE][NODE],dist[NODE],from[NODE];
bool inq[NODE];
int arr[QLEN];
struct queue{
    int front,rear,*ar;
    void init(){
        front=rear=0;
        ar=arr;
    }
    int deq(){
        int x=ar[front];
        front=++front%QLEN;
        return x;
    }
    void enq(int a){
        ar[rear]=a;
        rear=++rear%QLEN;
    }
}q;
int n,t,max;
int T;
int N, C, M;
std::vector<int> count[3];
int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
    for(int tc=1; tc<=T; tc++) {
    	scanf("%d%d%d", &N, &C, &M);
    	n = N;
        //Initialize
        max=0;
        for(int i=0;i<NODE;i++)
            for(int j=0;j<NODE;j++)
                con[i][j]=cost[i][j]=0;
        for(int i=0; i<3; i++) {
        	count[i] = std::vector<int>();
		}
        //Input
        for(int mi=0; mi<M; mi++) {
        	int P, B;
        	scanf("%d%d", &P, &B);
        	count[B].push_back(P);
		}
		int size1, size2;
		size1 = count[1].size();
		size2 = count[2].size();
		std::sort(count[1].begin(), count[1].end());
		std::sort(count[2].begin(), count[2].end());
		int ED = size1+size2+1;
        for(int i=1;i<=size1;i++)
            con[0][i] = 1;
		for(int i=1;i<=size2;i++)
			con[i+size1][ED] = 1;
		for(int i1=0; i1<size1; i1++) {
			for(int i2=0; i2<size2; i2++) {
				//printf("%d %d: %d %d\n", i1, i2, count[1][i1], count[2][i2]);
				if(count[1][i1] != count[2][i2]) {
					con[i1+1][i2+1+size1] = 1;
					cost[i1+1][i2+1+size1] = 0;
					cost[i2+1+size1][i1+1] = 0;
				}
				else if(count[1][i1] != 1) {
					con[i1+1][i2+1+size1] = 1;
					cost[i1+1][i2+1+size1] = 1;
					cost[i2+1+size1][i1+1] = 1;
				}
			}
		}
        /*for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++){
                scanf("%d",&t);
                con[i][j+HALF]=1;
                cost[i][j+HALF]=-t;
                cost[j+HALF][i]=t;
                if(!t)con[i][j+HALF]=1;
            }*/
        int mflow = 0;
        while(1){
            //Initialize
            q.init();q.enq(0);
            int flow=MAX,now,m=0;
            for(int i=0;i<=ED;i++){
                dist[i]=MAX;inq[i]=0;
                from[i]=-1;
            }
            //SPFA
            dist[0]=0;inq[0]=1;
            while(q.front!=q.rear){
                now=q.deq();
                //printf("now=%d\n", now);
                for(int i=0;i<=ED;i++){
                	//printf("i=%d con%d dist%d\n", i, con[now][i], dist[i]);
                    if(con[now][i]>0 && dist[i]>dist[now]+cost[now][i]){
                        dist[i]=dist[now]+cost[now][i];
                        from[i]=now;
                        if(!inq[i]){
                            inq[i]=1;
                            q.enq(i);
                        }
                    }
                }
                inq[now]=0;
            }
            if(from[ED] == -1)break;
            for(now=ED;now;now=from[now]){
                if(flow>con[from[now]][now])
                    flow=con[from[now]][now];
            }
            for(now=ED;now;now=from[now]){
                m+=cost[from[now]][now];
                con[from[now]][now]-=flow;
                con[now][from[now]]+=flow;
            }
            //printf("m=%d flow=%d\n", m, flow);
            max += m;
            mflow += flow;
        }
        printf("Case #%d: %d %d\n",tc,M-mflow,max);
        fprintf(stderr, "Case #%d: %d %d\n",tc,M-mflow,max);
    }
}
