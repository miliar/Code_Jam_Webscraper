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

llu bs;
string s;

int main()
{
    //READ("in.txt");
    //WRITE("out.txt");

    int T,N=0;
    cin>>T;
    while(++N<=T){
        llu num;
        string str;
        cin>>str;

        bs = num = 0;
        int pnt = -1,len = str.length();
        for(int i=0;i<str.length();i++){
            bs = (bs*10) + str[i]-'0';
            if(i<str.length()-1 && pnt<0){
                if(str[i]>str[i+1]) pnt = i;
            }
        }

        if(pnt==-1 && str[len-1]<str[len-2]) pnt = len-2;

        //cout<<pnt<<endl;

        if(pnt==-1) printf("Case #%d: %lld\n",N,bs);
        else{

            for(int i=pnt-1;i>=0;i--){
                if(str[i]==str[i+1]) pnt--;
            }

            for(int i=0;i<pnt;i++) num = (num*10) + str[i]-'0';
            for(int i=pnt;i<len;i++){
                if(i==pnt && str[pnt]>'1') num = (num*10) + (str[i]-'0')-1;
                else num = (num*10) + 9;
            }
            if(num>bs){
                num = 0;
                for(int i=1;i<len;i++) num = (num*10) + 9;
            }

            printf("Case #%d: %lld\n",N,num);
        }

    }
    return 0;
}

