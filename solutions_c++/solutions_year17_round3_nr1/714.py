#include<stdio.h>
#include<cmath>
#include<algorithm>

using namespace std;


struct Pcake{
    double side, top;
    int id;
    Pcake(){}
    inline bool operator < (const Pcake &p){
        return side > p.side;
    }
};


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    const double pi = 2*acos(0);
    //fprintf(stderr,"pi=%lf\n",pi);
    Pcake pcake[1002];
    int cases,N,i,T,j,K;
    double R,H,an,surface;
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++){
        scanf("%d%d",&N,&K);
        for(i=0;i<N;i++){
            scanf("%lf%lf",&R,&H);
            pcake[i].id=i;
            pcake[i].top=pi*R*R;
            pcake[i].side=2*pi*R*H;
        }
        sort(pcake,pcake+N);
        an=0;
        for(i=0;i<N;i++){
            surface = pcake[i].top + pcake[i].side;
            for(j=0;j< (i>K-1?K-1:K);j++){
                if(i!=j){
				    surface+=pcake[j].side;
				    //fprintf(stderr,"i=%d j=%d idi =%d %lf %lf id=%d %lf %lf\n",i,j,pcake[i].id, pcake[i].side,pcake[i].top, pcake[j].id,pcake[j].side,pcake[j].top);
			    }
            }
            //fprintf(stderr,"i=%d surface=%lf\n",i,surface);
            if(surface>an)an=surface;
        }
        printf("Case #%d: %lf\n",cases, an);
    }
    
    return 0;
}

