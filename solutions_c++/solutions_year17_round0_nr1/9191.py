#include<bits/stdc++.h>
using namespace std;

int d8x[]={-1,-1,0,1,1,1,0,-1};
int d8y[]={0,1,1,1,0,-1,-1,-1};
#define ll long long int
#define llu unsigned long long int
#define mem(a,b) memset(a,b,sizeof(a))
#define pr pair<int,int>
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define pii 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 1007
#define int_map map<int,int>
#define v_map map<int,vector<int> >
#define long_map map<long long,long long>
#define IO ios::sync_with_stdio(false)
#define inputline(a) getline(cin,a)
#define INF (1LL<<31)-1
//int gcd(int x,int y){return (y==0)?x:gcd(y,x%y);};
#define gcd(a,b) __gcd(a,b)

string str;
int k,ar[1003];

int main()
{
    //READ("in.txt");
    //WRITE("out.txt");

    int T,N=0;
    cin>>T;
    while(++N<=T){

        mem(ar,0);
        cin>>str;
        scanf(" %d",&k);

        int c = 0;

        int len = str.length();
        for(int i=0;i<len;i++) if(str[i]=='+') ar[i] = 1;

        for(int i=0;i<=len-k;i++){
            if(ar[i]==1) continue;
            //cout<<i<<" "<<ar[i]<<endl;
                c++;
                for(int j=i;j<i+k;j++){
                    if(ar[j]==0) ar[j] = 1;
                    else ar[j] = 0;
              //      cout<<ar[j];
                }
                //cout<<endl<<endl;

        }
        bool flag = false;
        for(int i=0;i<len;i++){
            //cout<<ar[i];
            if(ar[i]==0){
                flag = true;
                break;
            }
        }
//cout<<endl;
        if(flag) printf("Case #%d: IMPOSSIBLE\n",N);
        else printf("Case #%d: %d\n",N,c);
    }
    return 0;
}
