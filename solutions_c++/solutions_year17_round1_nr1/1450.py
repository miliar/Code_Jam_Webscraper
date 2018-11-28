#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define maxx(a,b) ((a)>(b))?(a):(b)
#define minn(a,b) ((a)<(b))?(a):(b)
#define arr_print(arr_,size_) int c_0;for(int c_0=0;c_0<size_;c_0++)cout<<arr_[c_0]<<" ";


//vector<int> a;
int n;
char a[25][25];
string s;
char ch;
int r,c;
void row_scan(int rr,int jj)
{
    for(int j=jj-1;j>=0;j--)
    {

        if(a[rr][j]=='?')
        {
            a[rr][j]=a[rr][j+1];
        }
    }
    for(int j=jj+1;j<c;j++)
    {
        if(a[rr][j]=='?')
        {
            a[rr][j]=a[rr][j-1];
        }
    }
}


void col_scan(int rr,int jj)
{
    for(int j=jj-1;j>=0;j--)
    {
        if(a[j][rr]=='?')
        {

            a[j][rr]=a[j+1][rr];
        }
    }
    for(int j=jj+1;j<r;j++)
    {
        if(a[j][rr]=='?')
        {

            a[j][rr]=a[j-1][rr];
        }
    }
}

void attack()
{
    for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(a[i][j]!='?')
                    {
                        row_scan(i,j);
                    }
            }
        }
    for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(a[i][j]!='?')
                    {
                        col_scan(j,i);
                    }
            }
        }
}


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.out","w",stdout);
    int t,ii=1;
    cin>>t;
    while(ii<=t)
    {
        //cin>>n;
        int var;
        cin>>r>>c;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
                cin>>a[i][j];

        }
            cout<<"Case #"<<ii<<": ";

        attack();
        for(int i=0;i<r;i++)
        {
            cout<<endl;
            for(int j=0;j<c;j++)
                cout<<a[i][j];

        }

        cout<<endl;
        ii++;
    }
}
