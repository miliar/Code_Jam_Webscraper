#include<bits/stdc++.h>
using namespace std;
char A[1010];
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T; i++)
    {
        fout << "Case #" << i << ": ";
        int N,R,O,Y,G,B,V;
        fin >> N >> R >> O >> Y >> G >> B >> V;
        if(V>Y) fout << "IMPOSSIBLE" << endl;
        else if(O>B) fout << "IMPOSSIBLE" << endl;
        else if(G>R) fout << "IMPOSSIBLE" << endl;
        else if((R+O+V)*2 > N) fout << "IMPOSSIBLE" << endl;
        else if((B+G+V)*2 > N) fout << "IMPOSSIBLE" << endl;
        else if((Y+O+G)*2 > N) fout << "IMPOSSIBLE" << endl;
        else if(V==Y && 2*V < N && V>0) fout << "IMPOSSIBLE" << endl;
        else if(O==B && 2*O < N && O>0) fout << "IMPOSSIBLE" << endl;
        else if(G==R && 2*G < N && G>0) fout << "IMPOSSIBLE" << endl;
        else
        {
            int h=0;
            char x='Q';
            if(V>0)
            {
                A[0]='Y';
                for(int v=1 ; v<=V ; v++)
                {
                    A[2*v-1]='V';
                    A[2*v]='Y';
                }
                h+=2*V+1;
                x='Y';
                Y=Y-V-1;
            }
            if(O>0)
            {
                A[h]='B';
                for(int o=1 ; o<=O ; o++)
                {
                    A[h+2*o-1]='O';
                    A[h+2*o]='B';
                }
                h+=2*O+1;
                if(x=='Q') x='B';
                B=B-O-1;
            }
            if(G>0)
            {
                A[h]='R';
                for(int o=1 ; o<=G ; o++)
                {
                    A[h+2*o-1]='G';
                    A[h+2*o]='R';
                }
                h+=2*G+1;
                if(x=='Q') x='R';
                R=R-G-1;
            }
            if(x=='Q')
            {
                if(R>=B && R>=Y)
                {
                    A[0]='R';
                    x='R';
                    R--;
                }
                else if(B>=R && B>=Y)
                {
                    A[0]='B';
                    x='B';
                    B--;
                }
                else if(Y>=B && R<=Y)
                {
                    A[0]='Y';
                    x='Y';
                    Y--;
                }
                h=1;
            }
            while(h<N)
            {
                if(A[h-1]=='R')
                {
                    if(B>Y || (B==Y && x=='B'))
                    {
                        A[h]='B';
                        B--;
                    }
                    else
                    {
                        A[h]='Y';
                        Y--;
                    }
                }
                else if(A[h-1]=='B')
                {
                    if(R>Y || (R==Y && x=='R'))
                    {
                        A[h]='R';
                        R--;
                    }
                    else
                    {
                        A[h]='Y';
                        Y--;
                    }
                }
                else if(A[h-1]=='Y')
                {
                    if(B>R || (B==R && x=='B'))
                    {
                        A[h]='B';
                        B--;
                    }
                    else
                    {
                        A[h]='R';
                        R--;
                    }
                }
                h++;
            }
            for(int w=0; w<N ; w++)
            {
                fout << A[w];
            }
            fout << endl;
        }
    }
}
