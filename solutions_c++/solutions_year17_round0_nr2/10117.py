#include<stdio.h>
#include<vector>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
using namespace std;

int T;
int N;
int VectorToNum(vector<int> a)
{
int num=0;
int i=0;
while(i<a.size())
{
    num=num*10+a[i];
    i++;
}
return num;
}
vector<int> NumToVector(int num)
{
    int temp=num;
    vector<int> N;
    while(temp!=0)
    {
        int x=temp%10;
        N.push_back(x);
        temp=temp/10;
    }
    reverse(N.begin(),N.end());
    return N;
}
vector<int> Sort(vector<int> a)
{
    for(int i=0;i<a.size();i++)
    {
        for(int j=i+1;j<a.size();j++)
        {
            if(a[i]>a[j])
            {
                int temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    return a;
}

int main()
{
freopen("B-small-attempt0.in","r+",stdin);
freopen("B-small-attempt0.out","w+",stdout);

cin>>T;
for(int i=0;i<T;i++)
{
    cin>>N;
    for(int l=N;l>0;l--)
    {
     int temp=l;
     vector<int> VN=NumToVector(l);
     VN=Sort(VN);
     int NN=VectorToNum(VN);
     if(temp==NN)
     {
         cout<<"Case #"<<i+1<<": "<<l<<endl;
         break;
     }
    }
}

return 0;
}

