#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("A-large.in.txt", ios::in);
    outFile.open("Oversized Pancake Flipper.txt", ios::out);
    int t;
    string cakes;
    int k;
    inFile>>t;
    int done;
    for(int z=1; z<=t; z++)
    {
    done=0;
    outFile<<"Case #"<<z<<": ";
    getline(inFile, cakes);
    getline(inFile, cakes, ' ');
    inFile>>k;
    int flip=0;
    int m=cakes.size();
    int temp[m];
    for(int i=0; i<=m-1; i++)
    {
            if(cakes[i]=='-') temp[i]=0;
            if(cakes[i]=='+') temp[i]=1;
            }
    for(int i=0; i<=m-k; i++)
    {
            if(temp[i]==0) 
            {
                        for(int j=0; j<=k-1; j++) temp[i+j]=1-temp[i+j];
                        flip=flip+1;
                        }
            }
    int h=m-k+1;
    while(h<=m-1&&done==0)
    { 
                 if(temp[h]==0) done=1;
                 h++;
                 }
    if(done==1) outFile<<"IMPOSSIBLE"<<endl;
    else outFile<<flip<<endl;
}
    inFile.close();
    outFile.close();
    system("PAUSE");
    return 0;
}
