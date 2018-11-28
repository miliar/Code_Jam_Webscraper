#include <iostream>
#include<queue>
#include<fstream>

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

priority_queue<int> q;

int main()
{
    int Cases,n,k,aux,aux2,aux1;
    fin>>Cases;
    for(int Case=1;Case<=Cases;++Case)
    {
        fin>>n>>k;
        q = priority_queue<int>();
        q.push(n);
        while(k>1)
        {
            k--;
            aux = q.top();
            q.pop();
            if(aux%2==0)
            {
                q.push(aux/2);
                q.push(aux/2-1);
            }
            else
            {
                q.push(aux/2);
                q.push(aux/2);
            }
        }
        aux=q.top();
        if(aux%2==0)
        {
            aux1=aux/2;
            aux2=aux/2-1;
        }
        else
        {
            aux1=aux2=aux/2;
        }
        fout<<"Case #"<<Case<<": "<<aux1<<" "<<aux2<<'\n';
    }

    return 0;
}
