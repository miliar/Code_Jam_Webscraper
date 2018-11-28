#include<iostream>
#include<fstream>
using namespace std;
void put(int *a,int n)
{
    for(int i=n;i>=0;i--)
    {
        a[i]=9;
    }
}
int main()
{
ofstream fout;
ifstream fin;
fout.open("output.txt");
fin.open("B-small-attempt0.in");
int t;
fin>>t;
long long a;
int b[18];
long long num;
for(int i=0;i<t;i++)
{
    int j=0;
    fin>>a;
    num=a;
    while(num!=0)
    {
        b[j]=num%10;
        j++;
        num/=10;
    }

j--;
int f=0;
for(int t1=0;t1<j;t1++)
{

    if(b[t1]<b[t1+1])
    {
        b[t1+1]--;
        if(b[t1+1]<0){
        b[t1+1]=9;
        put(b,t1+1);
        }
        b[t1]=9;
        put(b,t1);

    }

}

//if(f==0){
fout<<"Case #"<<i+1<<": ";
for(int t1=j;t1>=0;t1--)
{
    if(b[t1]!=0)
    fout<<b[t1];

}
fout<<endl;
}


}
