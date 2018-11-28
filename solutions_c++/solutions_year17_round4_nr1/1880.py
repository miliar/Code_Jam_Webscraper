#include<iostream>
#include<cstring>
#include<set>
#include<cmath>
#include<cstdio>
using namespace std;
int f[101][101][101][4];
int arr[101];
int dp(int r1,int r2,int r3,int re){
    if(r1 == r2 == r3 &&r1 == 0){
        return f[r1][r2][r3][re] = (re > 0);
    }
    if(f[r1][r2][r3][re]!=-1)return f[r1][r2][r3][re];
    int m1,m2,m3;
    m1 =m2 = m3 = 0;
    if(r1 > 0)m1 = dp(r1-1,r2,r3,(re+1)%4) + ((re+1)%4 == 0);
    if(r2 > 0)m2 = dp(r1,r2-1,r3,(re+2)%4) + ((re+2)%4 == 0);
    if(r3 > 0)m3 = dp(r1,r2,r3-1,(re+3)%4) + ((re+3)%4 == 0);
    return f[r1][r2][r3][re] = max(m1,max(m2,m3));
}

int main(){
    int q,cas;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    cin>>cas;
    for(q = 1; q <= cas; q++){
        int n,p;
        int a[4]={0};
        memset(f,-1,sizeof(f));
        cin>>n>>p;
        for(int i = 0; i < n; i++){
            cin>>arr[i];
            arr[i]%=p;
            a[ arr[i] ]++;
        }
        int sol = 0;
        if(p == 2){
            sol = a[0] + (a[1]/2);
            a[1]%=2;
            if(a[1] > 0)sol++;
        }
        else if( p == 3 ){
            int mi = min(a[1],a[2]);
            a[1]-=mi;
            a[2]-=mi;
            sol = a[0] + mi;
            if( a[1] == 0){
                sol+=a[2]/3;
                a[2]%=3;
                if(a[2]>0)sol++;
            }
            else{
                sol+=a[1]/3;
                a[1]%=3;
                if(a[1]>0)sol++;
            }
        }
        else{
         //   cout<<a[1]<<' '<<a[2]<<' '<<a[3]<<endl;
            sol = dp(a[1],a[2],a[3],0) + a[0];
        }
        cout<<"Case #"<<q<<": "<<sol<<endl;

    }
 return 0;
}
