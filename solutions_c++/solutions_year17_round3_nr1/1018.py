#include<bits/stdc++.h>
using namespace std;
// sum 2pir_ih_i + pir_k^2
typedef pair<long long int,long long int> ii;
long long int M[1100][1100];
ii A[1100];
long long int F(int tetto, int quanti)
{
    if(quanti==0) return 0;
    if(M[tetto][quanti]!=-1) return M[tetto][quanti];
    if(tetto==quanti) return M[tetto][quanti]=(A[tetto-1].first)*(A[tetto-1].second)+F(tetto-1,quanti-1);
    return M[tetto][quanti]=max((A[tetto-1].first)*(A[tetto-1].second)+F(tetto-1,quanti-1),F(tetto-1,quanti));
}
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": " ;
        int N,K;
        fin >> N >> K;
        for(int j=0 ; j<N ; j++)
        {
            long long int r,h;
            fin >> r >> h;
            A[j].first = r;
            A[j].second = h;
        }
        for(int h=0; h<N ; h++)
        {
            for(int l=0 ; l<N ; l++)
            {
                M[h][l]=-1;
            }
        }
        sort(A,A+N);
        long long int m=0;
        for(int j=K-1 ; j<N ; j++)
        {
            m=max(m,2*(A[j].second)*(A[j].first)+(A[j].first)*(A[j].first)+2*F(j,K-1));
        }
        long double res=m*(3.14159265358979);
        fout << fixed << setprecision(12) << res << endl;
    }
}
