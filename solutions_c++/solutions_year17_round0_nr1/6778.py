//__ hr1212 __//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mi;

#define si(a) scanf("%d",&a)
#define sii(a,b) scanf("%d %d",&a,&b)
#define siii(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define pi(a) printf("%d\n",a)
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define f(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b) for(i=a;i>=b;i--)
#define clr(x,a) memset(x,a,sizeof(x))
#define MAX 1005
#define MOD 1000000007

int n,m,a[MAX];

int main(){
    int r,k,i,tt,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0;
    ll ans=0;string p;

    cin>>t;
    f(tt,1,t+1){
        clr(a,0);
        cin>>p;
        cin>>m;
        f(i,0,p.size()){
            if(p[i]=='+')
                a[i]=1;
            else
                a[i]=0;
        }
        c=0;
        f(i,0,p.size()-m+1){
            if(a[i]==0){
                for(j=i;j<i+m;j++){
                    a[j]=1-a[j];
                }
                c++;
            }
        }
        f(i,0,p.size())
            if(a[i]==0)
                c=-1;
        if(c>=0)
            cout<<"Case #"<<tt<<": "<<c<<endl;
        else
            cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
