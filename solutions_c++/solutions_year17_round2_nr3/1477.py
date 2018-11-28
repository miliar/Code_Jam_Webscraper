#include<cstdio>


using namespace std;

int testy, n, q;
int miasta[1200][2];
int odl[1100][1100];
//double graf[1100][1100];
double drogi[1100][1100];
double czasy[1100][1100];

void czysc() {
    for (int i=0; i<1100; ++i) {
        miasta[i][0]=miasta[i][1]=0;
        for (int j=0; j<1100; ++j) {
            odl[i][j]=-1;
            //graf[i][j]=0.0;
            drogi[i][j] = 10e12;
            czasy[i][j] = 10e12;
        }
    }
}

void liczkrawedzie(int n) {
    for (int i=0; i<n; ++i) {
        for (int j=0; j<n; ++j) {
            if (odl[i][j] == -1) continue;
            if (miasta[i][0] < odl[i][j]) continue;
            drogi[i][j] = (double)odl[i][j];
            czasy[i][j] = (double)odl[i][j]/(double)miasta[i][1];
            //printf("!!%d %d %lf\n", i, j, drogi[i][j]);
        }
    }
}

void liczwielokrawedzie(int n) {

    for (int k=0; k<n; ++k) {
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (drogi[i][k] + drogi[k][j] <= miasta[i][0] && (drogi[i][k] + drogi[k][j])/miasta[i][1] < czasy[i][j])
                    czasy[i][j] = (drogi[i][k] + drogi[k][j])/miasta[i][1];
                    //printf("!!%d %d %d %lf %lf %lf\n", i, j, k, czasy[i][j], drogi[i][k], drogi[k][j]);
            }
        }
    }
}

void liczdrogi1(int n) {
    for (int k=0; k<n; ++k) {
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (drogi[i][k] + drogi[k][j] < drogi[i][j]) drogi[i][j] = drogi[i][k] + drogi[k][j];
            }
        }
    }
}

void liczdrogi(int n) {
    for (int k=0; k<n; ++k) {
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (czasy[i][k] + czasy[k][j] < czasy[i][j]) czasy[i][j] = czasy[i][k] + czasy[k][j];
            }
        }
    }
}

int main() {

    scanf("%d", &testy);


    for (int licz=1; licz<=testy; ++licz) {
        czysc();
        scanf("%d", &n);
        scanf("%d", &q);
        double czas = (double)0.0;
        for (int i=0; i<n; ++i) {
            scanf("%d", &miasta[i][0]);
            scanf("%d", &miasta[i][1]);
        }
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                scanf("%d", &odl[i][j]);
            }
        }

        liczkrawedzie(n);
        liczdrogi1(n);
        liczwielokrawedzie(n);
        liczdrogi(n);

        //jeszcze czytanie pytań

        printf("Case #%d:", licz);

        for (int i=0; i<q; ++i) {
            int raz, dwa;
            scanf("%d", &raz);
            scanf("%d", &dwa);
            printf(" %.6lf", czasy[raz-1][dwa-1]);
        }

        printf("\n");
    }


    return 0;
}
