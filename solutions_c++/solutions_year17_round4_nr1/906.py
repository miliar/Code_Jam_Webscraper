#include <bits/stdc++.h>
using namespace std;
#define maxn 120

int a[maxn];

#define count _count
int dp4[maxn][maxn][maxn][5];
int dp3[maxn][maxn][5];
int dp2[maxn][5];

int P;

int sub (int a, int b){
    return ((a-b)%P+P)%P;
}

int comp4 (int A, int B, int C, int lt){
    if (dp4[A][B][C][lt]!=-1) return dp4[A][B][C][lt];
    if (A==0 and B==0 and C==0 and lt==0){
        return dp4[A][B][C][lt]= 0; 
    }
    if (A==0 and B==0 and C==0) return dp4[A][B][C][lt]= -100000; 
    int t= 0;
    P= 4;
    int res= 0;
    if (A>0) {
        int nt= sub(lt, 1);
        if (nt==0) res= max(res, comp4(A-1, B, C, nt)+1);
        else res= max(res, comp4(A-1, B, C, nt));  
    }
    if (B>0){
        int nt= sub(lt, 2);
        if (nt==0) res= max(res, comp4(A, B-1, C, nt)+1);
        else res= max(res, comp4(A, B-1, C, nt));
    }
    if (C>0){
        int nt= sub(lt, 3);
        if (nt==0) res= max(res, comp4(A, B, C-1, nt)+1);
        else res= max(res, comp4(A, B, C-1, nt)); 
    }
    return dp4[A][B][C][lt]= res;
}

int comp3 (int A, int B, int lt){
    if (dp3[A][B][lt]!=-1) return dp3[A][B][lt];
    if (A==0 and B==0 and lt==0) return dp3[A][B][lt]= 0;
    if (A==0 and B==0 ) return dp3[A][B][lt]= -10000000;
    int res= 0;
    P= 3;
    if (A>0){
        int nt= sub(lt, 1);
        if (nt==0) res= max(res, comp3(A-1, B, nt)+1);
        else res= max(res, comp3(A-1, B, nt));
    }
    if (B>0){
        int nt= sub(lt, 2);
        if (nt==0) res= max(res, comp3(A, B-1, nt)+1);
        else res= max(res, comp3(A, B-1, nt));
    }
    return dp3[A][B][lt]= res;
}

int comp2 (int A, int lt){
    if (dp2[A][lt]!=-1) return dp2[A][lt];
    if (A==0 and lt==0) return dp2[A][lt]= 0;
    if (A==0) return dp2[A][lt]= -10000000;
    P= 2;
    int res= 0;
    if (A>0){
        int nt= sub(lt, 1);
        if (nt==0) res= max(res, comp2(A-1, nt)+1);
        else res= max(res, comp2(A-1, nt));
    }
    return dp2[A][lt]= res;
}

int count[6];


void solve (int ind){
    int n, p;
    cin>>n>>p;
    for (int i=0; i<6; i++) count[i]= 0;
    int cur= 0, ans= 0;
    for (int i=1; i<=n; i++) {
        int x;
        cin>>x;
        if (x%p==0) {
            ans++;
            continue;
        }
        cur++;
        x%=p;
        count[x]++;
        a[cur]=p;
    }
    int res= 0;
    if (p==4) {
        for (int i=0; i<4; i++) res= max(res, comp4(count[1], count[2], count[3], i));
    }
    if (p==3){
        for (int i=0; i<3; i++) res= max(res, comp3(count[1], count[2], i));
    } 
    if (p==2){
        for (int i=0; i<2; i++) res= max(res, comp2(count[1], i));
    }
    cout<<"Case #"<<ind<<": "<<res+ans<<endl;

}


int main(){
    memset(dp2, -1, sizeof(dp2));
    memset(dp3, -1, sizeof(dp3));
    memset(dp4, -1, sizeof(dp4));
    int t;
    cin>>t;
    for (int i=1; i<=t; i++) solve(i);
}