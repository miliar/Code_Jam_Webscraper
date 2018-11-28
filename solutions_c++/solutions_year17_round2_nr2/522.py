#include<stdio.h>

char as[10000]={0};
int cnt = 0;
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int t, test, i, j;
    scanf("%d",&test);
    for(t=1;t<=test;t++){
        int n, r, o, y, g, b, v;
        int bk, rk, yk;
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        bk = b, rk = r, yk = y;

        if(b == 0 && o == 0 && r == 0 && g == 0 && y == v){
            printf("Case #%d: ", t);
            for(i=0;i<y;i++) printf("YV");
            printf("\n");
            continue;
        } else if(y == 0 && v == 0 && r == 0 && g == 0 && b == o){
            printf("Case #%d: ", t);
            for(i=0;i<b;i++) printf("BO");
            printf("\n");
            continue;
        } else if(y == 0 && v == 0 && b == 0 && o == 0 && r == g){
            printf("Case #%d: ", t);
            for(i=0;i<r;i++) printf("RG");
            printf("\n");
            continue;
        }

        if( (o>0 && b < o+1) || (g>0 && r < g+1) || (v>0 && y < v+1) ){
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }

        b-=o, r-=g, y-=v;

        if(b+r < y-v || b+y < r-g || r+y < b-o){
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }
        if(b+r < y) y = b+r;
        if(b+y < r) r = b+y;
        if(r+y < g) g = r+y;

        cnt = 0;
        if(b >= r && b >= y){
            int yt = y, rt = r;
            for(i=0;i<b-1;i++){
                as[2*i] = 'b';
                if(yt >= rt){
                    as[2*i+1] = 'y';
                    yt--;
                } else {
                    as[2*i+1] = 'r';
                    rt--;
                }
            }
            as[2*(b-1)] = 'b';
            for(i=0;i<rt+yt;i++){
                if( (i%2 == 0) ^ (rt >= yt) )
                    as[2*b-1 + i] = 'y';
                else
                    as[2*b-1 + i] = 'r';
            }
        }
        else if(r >= b && r >= y){
            int yt = y, bt = b;
            for(i=0;i<r-1;i++){
                as[2*i] = 'r';
                if(yt >= bt){
                    as[2*i+1] = 'y';
                    yt--;
                } else {
                    as[2*i+1] = 'b';
                    bt--;
                }
            }
            as[2*(r-1)] = 'r';
            for(i=0;i<bt+yt;i++){
                if( (i%2 == 0) ^ (bt >= yt) )
                    as[2*r-1 + i] = 'y';
                else
                    as[2*r-1 + i] = 'b';
            }
        }
        else{
            int bt = b, rt = r;
            for(i=0;i<y-1;i++){
                as[2*i] = 'y';
                if(bt >= rt){
                    as[2*i+1] = 'b';
                    bt--;
                } else {
                    as[2*i+1] = 'r';
                    rt--;
                }
            }
            as[2*(y-1)] = 'y';
            for(i=0;i<rt+bt;i++){
                if( (i%2 == 0) ^ (rt >= bt) )
                    as[2*y-1 + i] = 'b';
                else
                    as[2*y-1 + i] = 'r';
            }
        }

        printf("Case #%d: ", t);
        int bcnt = 0, rcnt = 0, ycnt = 0;
        for(i=0;i<b+r+y;i++){
            if(as[i] == 'b'){
                if(bcnt == 0){
                    int os = 2 * o - bk + b;
                    for(j=0;j<2*os+1;j++){
                        if(j%2 == 0) printf("B");
                        else printf("O");
                    }
                } else if(bcnt <= bk - o - b){
                    printf("BOB");
                } else printf("B");
                bcnt++;
            } else if(as[i] == 'r'){
                if(rcnt == 0){
                    int gs = 2 * g - rk + r;
                    for(j=0;j<2*gs+1;j++){
                        if(j%2 == 0) printf("R");
                        else printf("G");
                    }
                } else if(rcnt <= rk - g - r){
                    printf("RGR");
                } else printf("R");
                rcnt++;
            } else {
                if(ycnt == 0){
                    int vs = 2 * v - yk + y;
                    for(j=0;j<2*vs+1;j++){
                        if(j%2 == 0) printf("Y");
                        else printf("V");
                    }
                } else if(ycnt <= yk - v - y){
                    printf("YVY");
                } else printf("Y");
                ycnt++;
            }
        }
        printf("\n");
    }
    return 0;
}
