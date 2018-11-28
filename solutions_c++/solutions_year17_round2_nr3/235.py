#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Mat {
    double d[128][128];
};

int N, Q;
int E[128], S[128];

double BIG=1000000000000;

void sq(const Mat& A, Mat& B) {
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) {
            B.d[i][j] = A.d[i][j];
            for (int x=0; x<N; x++)
                B.d[i][j] = min(B.d[i][j], A.d[i][x]+A.d[x][j]);
        }
}


int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        cin>>N>>Q;
        for (int i=0; i<N; i++) cin>>E[i]>>S[i];
        
        Mat D;
        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++) {
                cin>>D.d[i][j]; if (D.d[i][j]==-1) D.d[i][j]=BIG;
                if (i==j) D.d[i][j]=0;
            }

        Mat DD;
        for (int i=0; i<10; i++) sq(D, DD), D=DD;
        
        Mat Z;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++)
                Z.d[i][j] = ((D.d[i][j] <= E[i]) ? double(D.d[i][j])/S[i] : BIG);//, printf("@%.9lf ", D.d[i][j]);
//            printf("\n");
        }
            
        Mat ZZ;
        for (int i=0; i<10; i++) sq(Z, ZZ), Z=ZZ;
        
        printf("Case #%d:", t);
        for (int q=0; q<Q; q++) {
            int i, j; cin>>i>>j; i--, j--;
            printf(" %.9lf", Z.d[i][j]);
        }
        printf("\n");
        
        
        
    }
    return 0;
}
