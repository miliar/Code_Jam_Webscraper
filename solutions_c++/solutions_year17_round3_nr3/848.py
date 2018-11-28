#include<bits/stdc++.h>
using namespace std;
double P[60];
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": ";
        int N,K;
        fin >> N >> K;
        double U;
        fin >> U;
        for(int j=0 ; j<N ; j++) fin >> P[j];
        P[N]=1;
        if(N==K)
        {
            sort(P,P+N);
            int m=0;
            while(U>0 && P[0]<1)
            {
                for(int h=m+1; h<N; h++)
                {
                    if(P[h]==P[0]) m=h;
                    else break;
                }
                if((P[m+1]-P[0])*(m+1)>U)
                {
                    P[0]+= U/(m+1) ;
                    U=0;
                }
                else
                {
                    U-=(P[m+1]-P[0])*(m+1) ;
                    P[0]=P[m+1];
                }
            }
            double a=1;
            for(int e=0; e<=m ; e++)
            {
                a*=P[0];
            }
            for(int f=m+1; f<N ; f++)
            {
                a*=P[f];
            }
            fout << fixed << setprecision(12) << a << endl;
        }
    }
}
