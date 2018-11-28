#include<iostream>
#include<fstream>
using namespace std;
int main()
{

    ifstream fin;
    ofstream fout;

    fin.open("B-large.in");
    fout.open("B-small-out.txt");

    int t;
    fin >> t;

for(long long int k=0;k<t;k++)
{
    string  data;
    fin>>data;



    long long int len = data.length();
    long long int ar[len], x;
    for(long long int i=0;i<len;i++)
    {
        ar[i]=data[i]-'0';
    }

    for(long long int i=len;i>0;i--)
    {
        if(ar[i]<ar[i-1])
        {
            ar[i-1]=ar[i-1]-1;
            for(int j=i;j<len;j++)
            {
                ar[j]=9;
            }
        }
    }

    fout<<"Case #"<<k+1<<": ";
    if(ar[0]==0)
         x=1;
     else x=0;
    for(;x<len;x++)
         fout<<ar[x];
    fout<<endl;






}

}
