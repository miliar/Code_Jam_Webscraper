//
//  main.cpp
//  17_round_1B_B
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cmath>

int main() {
    freopen("B-small-attempt1.in.txt", "r", stdin);
    freopen("B-small-attempt1.out.txt", "w", stdout);
    int t, n, r, y, b, g, v, o, r1, y1, b1, m, m1;
    bool rt, yt, bt;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        r1=r-g;
        y1=y-v;
        b1=b-o;
        printf("Case #%d: ", i);
        if(!(r1>=0 && y1>=0 && b1>=0 && r1<=y1+b1 && y1<=b1+r1 && b1<=r1+y1)) printf("IMPOSSIBLE\n");
        else if((y1==0 && v!=0 && y+v!=n) || (r1==0 && g!=0 && r+g!=n) || (b1==0 && o!=0 && b+o!=n)) printf("IMPOSSIBLE\n");
        else{
            if(y1==0 && y+v==n){
                for(int j=0; j<v; j++) printf("YV");
                printf("\n");
            }else if(r1==0 && r+g==n){
                for(int j=0; j<g; j++) printf("RG");
                printf("\n");
            }else if(b1==0 && b+o==n){
                for(int j=0; j<o; j++) printf("BO");
                printf("\n");
            }else{
                if(r1>y1) m=r1;
                else m=y1;
                if(b1>m) m=b1;
                m1=r1+y1+b1-2*m;
                rt=yt=bt=true;
                for(int j=0; j<m1; j++){
                    printf("R");
                    r--;
                    if(rt){
                        for(int k=0; k<g; k++){
                            printf("GR");
                            g--;
                            r--;
                        }
                        rt=false;
                    }
                    printf("Y");
                    y--;
                    if(yt){
                        for(int k=0; k<v; k++){
                            printf("VY");
                            v--;
                            y--;
                        }
                        yt=false;
                    }
                    printf("B");
                    b--;
                    if(bt){
                        for(int k=0; k<o; k++){
                            printf("OB");
                            o--;
                            b--;
                        }
                        bt=false;
                    }
                }
                r1-=m1;
                y1-=m1;
                b1-=m1;
                if(r1==y1+b1){
                    for(int j=0; j<y1; j++){
                        printf("R");
                        r--;
                        if(rt){
                            for(int k=0; k<g; k++){
                                printf("GR");
                                g--;
                                r--;
                            }
                            rt=false;
                        }
                        printf("Y");
                        y--;
                        if(yt){
                            for(int k=0; k<v; k++){
                                printf("VY");
                                v--;
                                y--;
                            }
                            yt=false;
                        }
                    }
                    for(int j=0; j<b1; j++){
                        printf("R");
                        r--;
                        if(rt){
                            for(int k=0; k<g; k++){
                                printf("GR");
                                g--;
                                r--;
                            }
                            rt=false;
                        }
                        printf("B");
                        b--;
                        if(bt){
                            for(int k=0; k<o; k++){
                                printf("OB");
                                o--;
                                b--;
                            }
                            bt=false;
                        }
                    }
                }else if(y1==b1+r1){
                    for(int j=0; j<r1; j++){
                        printf("R");
                        r--;
                        if(rt){
                            for(int k=0; k<g; k++){
                                printf("GR");
                                g--;
                                r--;
                            }
                            rt=false;
                        }
                        printf("Y");
                        y--;
                        if(yt){
                            for(int k=0; k<v; k++){
                                printf("VY");
                                v--;
                                y--;
                            }
                            yt=false;
                        }
                    }
                    for(int j=0; j<b1; j++){
                        printf("B");
                        b--;
                        if(bt){
                            for(int k=0; k<o; k++){
                                printf("OB");
                                o--;
                                b--;
                            }
                            bt=false;
                        }
                        printf("Y");
                        y--;
                        if(yt){
                            for(int k=0; k<v; k++){
                                printf("VY");
                                v--;
                                y--;
                            }
                            yt=false;
                        }
                    }
                }else if(b1==r1+y1){
                    for(int j=0; j<r1; j++){
                        printf("R");
                        r--;
                        if(rt){
                            for(int k=0; k<g; k++){
                                printf("GR");
                                g--;
                                r--;
                            }
                            rt=false;
                        }
                        printf("B");
                        b--;
                        if(bt){
                            for(int k=0; k<o; k++){
                                printf("OB");
                                o--;
                                b--;
                            }
                            bt=false;
                        }
                    }
                    for(int j=0; j<y1; j++){
                        printf("Y");
                        y--;
                        if(yt){
                            for(int k=0; k<v; k++){
                                printf("VY");
                                v--;
                                y--;
                            }
                            yt=false;
                        }
                        printf("B");
                        b--;
                        if(bt){
                            for(int k=0; k<o; k++){
                                printf("OB");
                                o--;
                                b--;
                            }
                            bt=false;
                        }
                    }
                }else printf("ERROR");
                printf("\n");
                if(!(r==0 && o==0 && y==0 && g==0 && b==0 && v==0)) printf("ERRORN\n");
            }
        }
    }
    return 0;
}
