#include <iostream>
#include<set>
///#define int long long int
#define pb push_back
#define mp make_pair
using namespace std;
char a[30][30],eler[30],elec[30];
int cntr[30],cntc[30],freqr[40][150],freqc[40][150],mark[100];
int main()
{
    freopen("inpu3.in","r",stdin);
    freopen("outputu4.txt","w",stdout);
    int c1=1,t;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<c1<<": "<<endl;
        c1++;
        int r,c,x=0;
        cin>>r>>c;
        for(int i=0; i<r; i++)
            cntr[i]=0;
        for(int i=0; i<c; i++)
            cntc[i]=0;
        for(int i=65; i<=90; i++)
            mark[i]=0;
        for(int i=0; i<=30; i++)
        {

            elec[i]='0';
            elec[r]='0';
            for(int j=0; j<=100; j++)
            {
                freqr[i][j]=0;
                freqc[i][j]=0;
            }
        }
        for(int i=0; i<r; i++)
        {
           // if(eler[i]=='#')
             //   continue;
            for(int j=0; j<c; j++)
            {
                cin>>a[i][j];
                if(a[i][j]=='?')
                {
                    x++;
                }
                else
                {
                    eler[i]=a[i][j];
                    freqr[i][a[i][j]]++;
                    if(freqr[i][a[i][j]]==1)
                    {
                        cntr[i]++;
                    }
                }
            }
        }
        //cout<<x<<endl;
        if(x==0)
        {
            for(int i=0; i<r; i++)
            {
                for(int j=0; j<c; j++)
                {
                    cout<<a[i][j];
                }
                cout<<endl;
            }
            continue;
        }

        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(a[i][j]!='?'&&mark[a[i][j]]!=-1)
                {
                    //cout<<a[i][j]<<" ";
                    for(int k=j-1; k>=0; k--)
                    {
                        if(a[i][k]!='?')
                            break;
                        //cout<<a[i][j]<<" lol";
                        mark[a[i][j]]=-1;
                        a[i][k]=a[i][j];
                    }
                    for(int k=j+1; k<c; k++)
                    {
                        if(a[i][k]!='?')
                            break;
                        mark[a[i][j]]=-1;
                        a[i][k]=a[i][j];
                    }
                }
            }
        }
        x=0;
        set<int> s;
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(a[i][j]=='?')
                {
                    s.insert(i);
                    x++;
                }
            }
        }
        if(x==0)
        {
            for(int i=0; i<r; i++)
            {
                for(int j=0; j<c; j++)
                {
                    cout<<a[i][j];
                }
                cout<<endl;
            }
            continue;
        }
        for(auto it=s.begin(); it!=s.end(); it++)
        {
            int rr=(*it),row=-1;
            for(int i=rr-1; i>=0; i--)
            {
                if(s.find(i)==s.end())
                {
                    row=i;
                    break;
                }
            }
            if(row!=-1)
            {
                for(int i=0; i<c; i++)
                {
                    a[rr][i]=a[row][i];
                }
                continue;
            }
            for(int i=rr+1; i<r; i++)
            {
                if(s.find(i)==s.end())
                {
                    row=i;
                    break;
                }
            }
            if(row!=-1)
            {
                for(int i=0; i<c; i++)
                {
                    a[rr][i]=a[row][i];
                }
                continue;
            }
        }
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                cout<<a[i][j];
            }
            cout<<endl;
        }
            //continue;
    }
    return 0;
}
