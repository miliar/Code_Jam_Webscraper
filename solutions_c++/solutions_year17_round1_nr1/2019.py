#include<iostream>
#include<stdio.h>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<limits.h>
#include<cmath>
#include<vector>
#include<iomanip>
#include<unordered_map>
using namespace std;

int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("data.out","w",stdout);
    int t,z=0;
    cin>>t;
    while(t--)
    {
        z++;
        cout<<"Case #"<<z<<":\n";
        vector<pair<int,int> >v;
        int r,c,flag;
        char a[25][25];
        cin>>r>>c;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cin>>a[i][j];
                if(a[i][j]!='?')
                {
                    v.push_back(pair<int,int>(i,j));
                }
            }
        }

        for(int i=0;i<v.size();i++)
        {
            //cout<<"yo\n";
            int x=v[i].first;
            int y=v[i].second;
            //cout<<x<<" "<<y<<"\n";
            char ch=a[x][y];
            int dxl=0,dxr=0;
            int j=y-1;
            while(j>=0)
            {
                //cout<<"hey1\n";
                if(a[x][j]=='?')
                    {dxl++;a[x][j]=ch;}
                else
                    break;
                j--;
            }
            j=y+1;
            while(j<c)
            {
                //cout<<"hey2\n";
                if(a[x][j]=='?')
                    {dxr++;a[x][j]=ch;}
                else
                    break;
                j++;
            }
            //cout<<dxl<<" "<<dxr<<"\n";
            j=x-1;
            while(j>=0)
            {
                //cout<<"hey3\n";
                flag=0;
                for(int k=y-dxl;k<=y+dxr;k++)
                {
                    if(a[j][k]!='?')
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    break;
                else
                    for(int k=y-dxl;k<=y+dxr;k++)
                    {
                        a[j][k]=ch;
                    }
                    j--;
            }


            j=x+1;
            while(j<r)
            {
                //cout<<"hey4\n";
                flag=0;
                for(int k=y-dxl;k<=y+dxr;k++)
                {
                    if(a[j][k]!='?')
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    break;
                else
                    for(int k=y-dxl;k<=y+dxr;k++)
                    {
                        a[j][k]=ch;
                    }
                j++;
            }

        }

        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<a[i][j];
            }
            cout<<endl;
        }
    }

    return 0;
}
