#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pll pair<LL, LL>
#define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define fs first
#define sc second

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define EPS 1e-6
#define MOD (1000000007)
#define PI  2*acos(0);

#define fore(iter,v) for(iter=v.begin(); iter!=v.end(); iter++)
#define forup(i,a,n) for(i=a; i<n; i++)
#define rep(i,n) for(i=0; i<n; i++)
#define SET(a, v) memset(a, v, sizeof a)
#define all(a) a.begin(),a.end()
#define ALLOC0(N)   (int*)calloc(N, sizeof(int));

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)


#define ps(x) printf("%s",x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pn printf("\n")
#define spc printf(" ")
#define gc getchar
ll r,c;

void pri(vector<vector<char> > v)
{
    ll i,j;
    cout<<endl;
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
            cout<<v[i][j]<<" ";
        cout<<endl;
    }

}


int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,bk;
    cin>>t;
    for(bk=1;bk<=t;bk++)
    {
        cout<<"Case #"<<bk<<": ";
        ll line,i,j,k;
        bool b;
        char ch;
        vector<vector<char> > v;
        vector<char> tempv;
        cin>>r>>c;
        vector<bool> allk(r,false);

        for(i=0;i<r;i++)
        {
            tempv.clear();
            for(j=0;j<c;j++)
            {
                cin>>ch;
                tempv.push_back(ch);
            }
            v.push_back(tempv);
        }

        for(i=0;i<r;i++)
        {
            b=true;
            line=0;
            for(j=0;j<c;j++)
            {
                //cout<<"I:"<<i<<" J:"<<j<<endl;
                if(v[i][j]=='?')
                {
                    //cout<<" Question Make"<<endl;
                    if(b)
                    {
                        //cout<<"Line increased"<<endl;
                        line++;
                    }
                    else
                    {
                        //cout<<"Line is 0 so replaced by left"<<endl;
                        v[i][j]=v[i][j-1];
                    }
                }
                else
                {
                    if(b)
                    {
                        //cout<<"Now line breaks"<<endl;
                        b=false;
                        for(k=0;k<line;k++)
                        {
                            v[i][k]=v[i][j];
                        }
                        //cout<<"Replaced with Another content"<<endl;
                    }
                }
                //cout<<endl;
                //pri(v);
            }
            if(line==c)
            {
                allk[i]=true;
                //cout<<"I:"<<i<<endl;
            }
            //cout<<endl<<endl;
        }


        b=true;
        line=0;
        for(i=0;i<r;i++)
        {
            //cout<<"I:"<<i<<endl;
            if(allk[i])
            {

                if(b)
                {
                    line++;
                }
                else
                {
                    for(j=0;j<c;j++)
                        v[i][j]=v[i-1][j];
                }
            }
            else
            {
                if(b)
                {
                    b=false;
                    for(k=0;k<line;k++)
                    {
                        //cout<<"K:"<<k<<endl;
                        for(j=0;j<c;j++)
                            v[k][j]=v[i][j];
                    }
                    //cout<<endl;
                }

            }
        }
        cout<<endl;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
                cout<<v[i][j];
            cout<<endl;
        }

        //cout<<endl<<endl;
        //cout<<endl<<endl;
    }
    return 0;
}
