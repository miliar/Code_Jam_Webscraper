#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ofstream fout;
ifstream fin;
fout.open("output.txt");
fin.open("B-large (1).in");
long long test;
fin>>test;
//cout<<test;
long long a;
long long b[20];
long long num;

for(long long i=0;i<test;i++)
{


    long long j=0;
    fin>>a;
    //cout<<a;
    num=a;
    while(num!=0)
    {
        b[j]=num%10;
        j++;
        num/=10;
    }

j--;
long long f=0;
for(long long t1=0;t1<j;t1++)
{

    if(b[t1]<b[t1+1])
    {
        b[t1+1]--;
        if(b[t1+1]<0){
        b[t1+1]=9;
        for(long long i1=t1+1;i1>=0;i1--)
    {
        b[i1]=9;
    }
        }
        b[t1]=9;
            for(long long i1=t1;i1>=0;i1--)
    {
        b[i1]=9;
    }

    }

}


fout<<"Case #"<<i+1<<": ";
for(long long t1=j;t1>=0;t1--)
{
    if(b[t1]!=0)
    fout<<b[t1];
    //cout<<test<<endl;

}
fout<<endl;
}


}
