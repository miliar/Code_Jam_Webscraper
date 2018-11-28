#include<iostream>
#include<fstream>
using namespace std;
int check(int);
int main()
{
    int N,i,T;
    ifstream fin("B-small-attempt0.in");
    ofstream fout("qb.txt",ios::out);
    fin>>T;
    for(i=0;i<T;i++)
    {
        fin>>N;
        while(!check(N))
            N--;
        fout<<"Case #"<<i+1<<": "<<N<<endl;
    }
    return 0;
}

int check (int temp)
{
    int d;
    d=temp%10;
    temp/=10;
    while(temp!=0)
    {
        if(d<temp%10)
            break;
        else
        {
            d=temp%10;
            temp/=10;
        }
    }
    return(temp%10==0);
}
