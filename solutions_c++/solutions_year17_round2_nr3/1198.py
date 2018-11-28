#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
long long int D[110][110];
long long int E[110];
long long int S[110];
int N;
double M[101][101];
double minimo_tempo(int a, int cavallo)
{
    if(M[a][cavallo]!=-1) return M[a][cavallo];
    if(a==N) return 0;
    if(D[cavallo][a+1]>E[cavallo]) return -1;
    double e=minimo_tempo(a+1,cavallo);
    double f=minimo_tempo(a+1,a+1);
    if(e == -1) return M[a][cavallo]=f+((double)(D[a][a+1]))/S[cavallo];
    if(f == -1) return M[a][cavallo]=e+((double)(D[a][a+1]))/S[cavallo];
    return M[a][cavallo]= min(e,f)+((double)(D[a][a+1]))/S[cavallo];

}
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        for(int a=0 ; a<101;a++)
        {
            for(int b=0 ; b<101 ; b++)
            {
                M[a][b]=-1;
            }
        }
        fout << "Case #" << i << ": " ;
        int Q;
        fin >> N >> Q;
        for(int j=1 ; j<=N ; j++)
        {
            fin >> E[j] >> S[j];
        }
        for(int j=1 ; j<=N ; j++)
        {
            for(int t=1 ; t<=N ; t++)
            {
                long long int a;
                fin >> a;
                if(a!=-1)
                {
                    D[j][j+1]=a;
                    for(int l=1 ; l<j ; l++)
                    {
                        D[l][j+1]=D[l][j]+a;
                    }
                }
            }
        }
        int U,V;
        fin >> U >> V;
        fout << fixed << setprecision(10) << minimo_tempo(1,1) << endl;
    }
}

