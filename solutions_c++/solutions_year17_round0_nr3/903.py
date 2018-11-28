#include<iostream>
#include<fstream>
using namespace std;
long long int exp2(long long int);
int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("C-large.in.txt", ios::in);
    outFile.open("Bathroom Stalls.txt", ios::out);
    long long int n, p, temp, r, q, max, min;
    int t;
    inFile>>t;
    for(int i=1; i<=t; i++)
    {
    outFile<<"Case #"<<i<<": ";
    inFile>>n; inFile>>p;
    temp=exp2(p);
    temp=temp-1;
    r=(n-temp)%(temp+1);
    q=(n-temp)/(temp+1);
    if(p-temp<=r) q=q+1;
    min=(q-1)/2;
    max=q-1-min;
    outFile<<max<<" "<<min<<endl;
}
    inFile.close();
    outFile.close();
    system("PAUSE");
    return 0;
}

long long int exp2(long long int p)
{
     long long int a=1;
     long int e2=0;
     while(a-1<p)
     {
                 a=a*2;
                 e2=e2+1;
                 }
     a=a/2;
     return a;
 }
