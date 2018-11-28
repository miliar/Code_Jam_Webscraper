#include<iostream>
#include<fstream>
using namespace std;
int length(long long int);
int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("B-large.in.txt", ios::in);
    outFile.open("Tidy Numbers.txt", ios::out);
    int t;
    inFile>>t;
    long long int n, temp;
    for(int z=1; z<=t; z++)
    {
    outFile<<"Case #"<<z<<": ";
    int done=0;
    inFile>>n;
    temp=n;
    int k=length(n);
    int digit[k];
    for(int i=0; i<=k-1; i++)
    {
            digit[k-1-i]=temp%10;
            temp=temp/10;
            }
    while(done!=1)
    {
    int i=0;
    int stop=0;
    while(i<=k-2&&stop==0)
    {
                 if(digit[i]>digit[i+1]) stop=1;
                 i++;
                 }
    if(stop==0)
    {
               done=1;
               int j=0;
               while(j<=k-2&&digit[j]==0)
               {
                                         j=j+1;
                                         }
               for(int i=j; i<=k-1; i++) outFile<<digit[i]; 
               outFile<<endl;
               }
    else
    {
                for(int j=i; j<=k-1; j++) digit[j]=9;
                digit[i-1]=digit[i-1]-1;
                }
                }
                }
    inFile.close();
    outFile.close();
    system("PAUSE");
    return 0;
}

int length(long long int n)
{
    int k=0;
    long long int a=1;
    while(a<=n)
    {
             a=a*10;
             k=k+1;  
               }
    return k;
}
