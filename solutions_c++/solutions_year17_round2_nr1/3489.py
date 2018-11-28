#include<fstream>
#include<vector>
#include<string>
#include<iomanip>
#define modulo 666013

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");


string sir;
int i, n, k, j,contor,st,dr,sol,x,y,t,dist;
int pos[10000], speed[10000];

int main()
{
    fin >> t;
    //fout<<std::fixed;
    //fout<<setprecision(20);
    for(int r = 1; r <= t; r++)
    {
        fin >> dist >> n;
        fin >> pos[1] >> speed[1];
        double timp = (double)(dist - pos[1]) / speed[1];
        double solution = dist / timp;
        //fout<<timp<<"\n";
        for(i = 2; i <= n; i++)
        {
            fin >> pos[i] >> speed[i];
            timp = (double)(dist - pos[i]) / speed[i];
            solution = min(solution, dist / timp);
            //fout<<timp<<"\n";

            //fout << timp <<"\n";
        }
         for(i = 1; i <= n; i++)
         {
             //fout<<pos[i]<<" "<<speed[i]<<"\n";
         }
        //fout<<"\n\n\n";
        fout<<std::fixed;
        fout << "Case #" << r <<": " << setprecision(6)<< (double)solution <<"\n";
    }
}


