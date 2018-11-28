#include <bits/stdc++.h>

using namespace std;

int T, C=1, n, p, v[1024], mod[4];

int PD[101][101][101][4];

inline int nl(int vi, int l) {
    int g = (vi-l+p)%p;
    int r =  p*((g+p-1)/p) - g;
    return r;
}

int calc4(int m1, int m2, int m3, int l) {
    if (m1 < 0 or m2 < 0 or m3 < 0) return -0x3f3f3f3f;
    if (m1+m2+m3==0) return 0;
    int &pd = PD[m1][m2][m3][l];
    if (pd != -1) return pd;
    int opc1 = (l==0) ? 1 : 0;
    opc1 += calc4(m1-1,m2,m3,nl(1,l));
    int opc2 = (l==0) ? 1 : 0;
    opc2 += calc4(m1,m2-1,m3,nl(2,l));
    int opc3 = (l==0) ? 1 : 0;
    opc3 += calc4(m1,m2,m3-1,nl(3,l));

    int r  = max(opc1,max(opc2,opc3));
    return pd = r;
}


int calc3(int m1, int m2, int l) {
    if (m1 < 0 or m2 < 0) return -0x3f3f3f3f;
    if (m1+m2==0) return 0;
    int &pd = PD[0][m1][m2][l];
    if (pd != -1) return pd;
    int opc1 = (l==0) ? 1 : 0;
    opc1 += calc3(m1-1,m2,nl(1,l));
    int opc2 = (l==0) ? 1 : 0;
    opc2 += calc3(m1,m2-1,nl(2,l));

    int r  = max(opc1,opc2);
    return pd = r;
}

int calc2(int m1, int l) {
    if (m1 < 0) return -0x3f3f3f3f;
    if (m1==0) return 0;
    int &pd = PD[0][m1][0][l];
    if (pd != -1) return pd;
    int opc1 = (l==0) ? 1 : 0;
    opc1 += calc2(m1-1,nl(1,l));

    return pd = opc1;
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&p);
        memset(mod,0,sizeof(mod));
        for (int i=0;i<n;i++) {
            scanf("%d",v+i);
            mod[v[i]%p]++;
        }
        memset(PD,0xff,sizeof(PD));
        int t;
        if (p==2) t = calc2(mod[1],0);
        if (p==3) t = calc3(mod[1],mod[2],0);
        if (p==4) t = calc4(mod[1],mod[2],mod[3],0);

        printf("%d\n",t + mod[0]);
    }

    return 0;
}
