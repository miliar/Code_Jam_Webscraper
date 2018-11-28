#include<stdio.h>
#include<queue>
#include<cstring>

using namespace std;

double dis[102][102]; // dis[c][h]  time to get in city c on hourse h
bool ud[102][102];
int D[102][102];

struct Node{
    int c, h, E; // E = energy left
    double dis;
    Node(){}
    Node(int cc, int hh, int EE, double dd){
        c=cc;
        h=hh;
        E=EE;
        dis=dd;
    }
};

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T, cases, N, Q, i, E[102],j ,U,V;
    double S[102];
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++){
        scanf("%d%d",&N,&Q);
        for(i=1;i<=N;i++){
            scanf("%d%lf",&E[i],&S[i]);
        }
        for(i=1;i<=N;i++){
            for(j=1;j<=N;j++){
                scanf("%d",&D[i][j]);
            }
        }
        printf("Case #%d:", cases);
        for(i=1;i<=Q;i++){
            memset(ud,0,sizeof(ud));
            queue<Node> near;
            scanf("%d%d",&U,&V);
            ud[U][U]=1;
            dis[U][U]=0;
            near.push(Node(U,U,E[U],0));
            //fprintf(stderr,"U=%d V=%d\n",U,V);
            while(!near.empty()){
                Node temp = near.front();
                //printf("  %d %d %d %lf\n",temp.c, temp.h, temp.E, temp.dis);
                near.pop();
                for(j=1;j<=N;j++){
                    if(D[temp.c][j]!=-1){
                        if(temp.E>=D[temp.c][j] && 
						    (ud[j][temp.h]==0  || dis[j][temp.h]>dis[temp.c][temp.h] + D[temp.c][j]/S[temp.h])){
						        ud[j][temp.h]=1;
						        dis[j][temp.h] = dis[temp.c][temp.h] + D[temp.c][j]/S[temp.h];
						        //printf("go to %d with horse %d\n",j,temp.h); 
						        near.push(Node(j,temp.h,temp.E-D[temp.c][j], dis[j][temp.h]));
						    }
						if(E[temp.c]>=D[temp.c][j] && 
						    ud[j][temp.c]==0 || dis[j][temp.c]>dis[temp.c][temp.h]+D[temp.c][j]/S[temp.c]){
						        ud[j][temp.c]=1;
						        dis[j][temp.c] = dis[temp.c][temp.h]+D[temp.c][j]/S[temp.c];
						        near.push(Node(j,temp.c,E[temp.c]-D[temp.c][j],dis[j][temp.c]));
						        //printf("go to %d with horse %d\n",j,temp.c); 
						    }
                    }
                }
            }
            double an = -1;
            for(j=1;j<=N;j++)if(ud[V][j]){
                if(an==-1 || an > dis[V][j]) an = dis[V][j];
            }
            printf(" %lf",an);
        }
        printf("\n");
    }
    

    return 0;
}
