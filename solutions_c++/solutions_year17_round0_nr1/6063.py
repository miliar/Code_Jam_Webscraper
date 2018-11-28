#include<bits/stdc++.h>
using namespace std;
#define MP          make_pair
#define PB          push_back
#define LL          long long
#define MAX         1000005
#define debug(a)    cout<<a<<"\n"
#define sd(a)       scanf("%d",&a)
#define sc(a)       scanf("%c",&a)
#define ss(a)       scanf("%s",&a)
#define mx(a,b,c)   max(a,max(b,c))
#define mn(a,b,c)   min(a,min(b,c))
#define pred(a)     printf("%0.6lf",a)
#define rep(i,x,b)  for(int i=x;i<b;i++)
#define rf          freopen("in.txt", "r", stdin)
#define wf          freopen("out.txt", "w", stdout)
#define fast()      ios_base::sync_with_stdio(0)
#define chloop(i,j) cout<<"i:"<<i<<" j:"<<j<<"\n"
#define sz(x)       x.size()
#define mst(x,a)    memset(x,a,sizeof(x))
#define pii         pair<LL,LL>
#define inf         1000000007
#define F            first;
#define S            second;  
int main(){
    rf;
    wf;
    int t;
    cin >> t;
    for(int z=0;z<t;z++)
    {
        string s;
        int k;
        cin >> s >> k;
        int i,j,step=0,size=s.size();
        for(i=0;i<=(size-k);i++)
            {
            if(s[i]=='-')
                {
                for(j=i;j<(i+k);j++)
                    {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                    }
                //cout << s << endl;
                step++;
                }
            }
        int flag=0;
        for(i=0;i<size;i++)
            {
            if(s[i]!='+')
                {
                flag=1;
                break;
                }
            }
        if(flag==0)
            cout << "Case #"<< (z+1)<<": " << step << endl;
        else
            cout << "Case #"<< (z+1)<<": "<< "IMPOSSIBLE" << endl;
    }
    return 0;
}