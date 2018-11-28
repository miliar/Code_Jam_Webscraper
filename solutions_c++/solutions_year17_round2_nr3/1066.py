#include <stdio.h>
#include <vector>

long long D[100][100];
long long E[100];
int S[100];

struct Horse{
    long long dLeft;
    double speed;
    double time;

    Horse(long long dLeft, double speed, double time):dLeft(dLeft),speed(speed),time(time){
        //printf("Creating horse %lld %lf %lf\n",dLeft,speed,time);
    }

    void printHorse(){
        //printf("Horse %lld %lf %lf\n",dLeft,speed,time);
    }
};

int main(){
    int T;
    scanf("%d",&T);

    for (int i = 1; i<=T; i++){
        int N,Q;
        scanf("%d %d",&N,&Q);
        //printf("processing case %d %d %d\n",i,N,Q);
        long long e;
        int s;
        for (int j = 0; j<N; j++){
            scanf("%lld %d",&e,&s);
            E[j] = e;
            S[j] = s;
        }
        //printf("E,S read in\n");
        long long d;
        for (int j = 0; j<N; j++){
            for (int k = 0; k<N; k++){
                scanf("%lld",&d);
                D[j][k] = d;
                //printf("reading %lld into %d %d\n",d,j,k);
            }
        }

        int u;
        int v;
        scanf("%d %d",&u,&v);

        std::vector<Horse> H;
        H.push_back(Horse(E[0],S[0],0));

        for (int j = 1; j<N; j++){
            //printf("At town %d\n",j);
            std::vector<Horse> nH;

            long long d = D[j-1][j];
            double dd = d;
            Horse fastest = Horse(0,0,20000000000000);

            for (Horse h:H){
                h.dLeft-=d;
                h.time+= dd/h.speed;
                if (h.dLeft>=0){
                    nH.push_back(h);
                    //printf("Adding to stack");
                    h.printHorse();
                    if (h.time<=fastest.time){
                        fastest = h;
                    }
                }
            }
            fastest.dLeft = E[j];
            fastest.speed = S[j];
            //printf("Adding to stack");
            fastest.printHorse();
            nH.push_back(fastest);
            H = nH;
        }
        Horse fastest = Horse(0,0,20000000000000);
        for (Horse h: H){
            if (h.time<=fastest.time){
                fastest = h;
            }
        }
        printf("Case #%d: %lf\n",i,fastest.time);

    }
}
