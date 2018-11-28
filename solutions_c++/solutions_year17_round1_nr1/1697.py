#include<bits/stdc++.h>

using namespace std;

#define li long int
#define ii pair<li,li>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define vi vector<li>
#define vii vector<ii>
#define INF 99999
#define MAXN 100005
#define sz size()
#define ins insert


int main()
{
   // freopen("input.in","r",stdin);
   // freopen("output.out","w",stdout);
    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }

   li ttca; //read(ttca);
   cin>>ttca;
    for(li ts=1;ts<=ttca;ts++)
    {
        string strr[26];
        int i,j,k,r,c;
        cin>>r>>c;

       for(i=0;i<r;i++) cin>>strr[i];

       for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(strr[i][j]!='?')
                {
                    k=j;
                    while(k+1<c && strr[i][k+1]=='?') { strr[i][k+1]=strr[i][k]; k++; }

                   k=j;
                    while(k-1>=0 && strr[i][k-1]=='?') { strr[i][k-1]=strr[i][k]; k--; }
                }
            }
        }

       for(i=0;i<r;i++)
        {
            if(strr[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) strr[i][j]=strr[i-1][j];
                }
                else if (i+1<r)
                {
                    for(j=0;j<c;j++) strr[i][j]=strr[i+1][j];
                }
            }
        }

       for(i=r-1;i>=0;i--)
        {
            if(strr[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) strr[i][j]=strr[i-1][j];
                }
                if (i+1<r)
                {
                    for(j=0;j<c;j++) strr[i][j]=strr[i+1][j];
                }
            }
        }

       cout<<"Case #"<<ts<<":"<<endl;

       for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++) cout<<strr[i][j];
            cout<<endl;
        }
    }
    return 0;
}
