#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <fstream>

#define PI 3.14159265

using namespace std;

struct node{
    int R;
    int H;
    double S;
};

bool comp(const node &a,const node &b)
{
    return a.R>b.R;
}

bool cmp(const node &a,const node &b)
{
    return a.S>b.S;
}

int T,N,K;
node nn[1008];

double get_Ans(int index){
   node nn1[1008];
   int len=0;
   double ans=0;
   for (int i=index+1;i<N;i++)
   {
       nn1[len]=nn[i];
       //cout<<"copy:"<<nn1[i].R<<" "<<nn1[i].H<<endl;
       len++;
   }
   //cout<<"len="<<len<<endl;
   sort(nn1,nn1+len,cmp);
   //for (int j=0;j<len;j++)
   // {
   //     cout<<nn1[j].R<<" "<<nn1[j].H<<endl;
   // }
   for (int i=0;i<K-1;i++)
   {
       ans+=nn1[i].S;
   }
   return ans;
}

int main()
{
    double ans,maxa;
    ifstream fin("1.in");
    ofstream fout("1.out");
    fin>>T;
    //cout<<T<<endl;
    fout<<setiosflags(ios::fixed);
    for (int i=0;i<T;i++)
    {
        fin>>N>>K;
        for (int j=0;j<N;j++)
        {
            fin>>nn[j].R>>nn[j].H;
            nn[j].S=PI*2*nn[j].R*nn[j].H;
        }
        sort(nn,nn+N,comp);maxa=0;

        for (int j=0;j<N;j++)
        {
            ans=PI*nn[j].R*nn[j].R+PI*2*nn[j].R*nn[j].H+get_Ans(j);
            if (maxa<ans)
                maxa=ans;
        }
        fout<<"Case #"<<i+1<<": "<< setprecision(13) <<maxa<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
