#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)a;i<=(int)b;i++)
#define rip(i,a,b) for(int i=(int)a;i>=(int)b;i--)
#define ll long long
#define MOD 1000000007
#define N 200005
#define f first
#define s second
#define pb push_back
#define pii pair<int,int>
#define matrix vector<vector<ll>>
#define PI acos(-1)
#define INF 10000000
#define LSOne(S) (S & (-S))
int main() {
   freopen("/home/vikhyat/Desktop/in.txt","r",stdin);
   freopen("/home/vikhyat/Desktop/out.txt","w",stdout);
     //ios_base::sync_with_stdio(false);
     //cin.tie(0);
	 //cout.tie(0);
	 int t;
	 cin>>t;
	 int test=1;
	 while(t--)
	 {
	 cout<<"Case #"<<test++<<": ";
	 cout<<endl;
       int r,c;
       cin>>r>>c;
       string gr[30];
       rep(i,0,r-1)
       {
            cin>>gr[i];
       }
       char prev,c1;
       rep(i,0,r-1)
       {
       int f=0;
       char c1='0';
       rep(j,0,c-1)
       {
        if(gr[i][j]!='?')
        {
            if(c1=='0')
            {
            int q=0;
            while(q<c&&gr[i][q]=='?')
            gr[i][q]=gr[i][j],q++;
            c1=gr[i][j];
            }
            while(j<c)
            {
                if(gr[i][j]=='?')
                gr[i][j]=c1;
                else
                c1=gr[i][j];
                j++;
            }
        }
       }
       }
       int p=-1;
       rep(i,0,r-1)
       {
        if(gr[i][0]=='?')
        {
        if(p==-1)
        {
         rep(j,i+1,r-1)
            {
                if(gr[j][0]!='?')
                {
                    p=j;
                    break;
                }
            }
        }
            while(i<r)
            {
                if(gr[i][0]=='?')
                {
                    rep(k,0,c-1)
                    gr[i][k]=gr[p][k];
                }
                else
                p=i;
                i++;
            }
        }
        else
        p=i;
       }
       rep(i,0,r-1)
       {
        rep(j,0,c-1)
        cout<<gr[i][j];
        cout<<endl;
       }
	 }
     return 0;
}
