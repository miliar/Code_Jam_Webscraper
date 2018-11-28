/*
Author    : MANISH RATHI
Institute : NIT KURUKSHETRA

*******************************
Don't Stop when you are tired  *
Stop When you are Done         *
******************************* 
*/

#include<bits/stdc++.h>
using namespace std;
#define MAX 1000007
#define mode 1000000007
#define ll long long
#define ii pair<int,int>
#define vi vector<int>
#define vii vector< ii >
#define vvi vector< vi >
#define vvii vector< vii >
#define mp make_pair
#define pb push_back
#define read(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define read2(x,y) scanf("%d%d",&x,&y);
#define print2(x,y) printf("%d %d\n",x,y);
#define read_s(x) scanf("%s",x);
#define print_s(x) printf("%s",x);
#define rep(i,a,b) for(i=a;i<=b;i++)
#define tr(container,it) \
	for((typeof(container.begin()) it= container.begin();it!=container.end();it++))

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("1large.txt", "w", stdout);
    int t,h;
    cin>>t;
    for(h=1;h<=t;h++)
    {
        int r,c;
        read2(r,c);
        vector<string> grid(r+1);
        int i,j,temp;
        rep(i,1,r)
            cin>>grid[i];
        
        int x,y,z,a,b,k;
        x=1;y=0;
        int flag=0;
        rep(i,1,r)
        {
            rep(j,0,c-1)
            {
                if(grid[i][j]!='?')
                {
                    flag=1;
                    rep(a,x,i)
                    {
                        rep(b,y,j)
                        grid[a][b]=grid[i][j];
                    }
                    y=j+1;
                }
            }
            if(flag==1)
            {
                if(y<c) // i.e some last columns remaining
                {
                    rep(a,x,i)
                    {
                        rep(b,y,c-1)
                        grid[a][b]=grid[x][y-1];
                    }
                }
                break;
            }
    		
        }
        x=i;
        // now i is the last row that is filled
        // now for each row just find the char in it
        rep(i,x+1,r)
        {
            a=1;b=0;
            rep(j,0,c-1)
            {
                if(grid[i][j]!='?')
                {
                    rep(k,b,j)
                        grid[i][k]=grid[i][j];
                    b=j+1;
                }
            }
            if(b==0)
            {
                // copy the last row
                rep(k,0,c-1)
                    grid[i][k]=grid[i-1][k];
            }
            else if(b<c)
            {
                rep(k,b,c-1)
                    grid[i][k]=grid[i][b-1];
            }
        }
        cout<<"Case #"<<h<<": \n";
        rep(i,1,r)
        {
            cout<<grid[i]<<endl;
        }
    }
    return 0;
}
