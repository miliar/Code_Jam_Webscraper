#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.out","w",stdout);
    freopen("B-large.in","r",stdin);
    int tc,t=0;
    cin>>tc;
    while(t<tc){
        t++;
        int str[25];
        for(int i=0;i<25;i++)str[i]=0;
        long long n;
        cin>>n;
        int i=0;
        while(n!=0){
            str[i]=n%10;;
            n=n/10;
            i++;
        }
        //cout<<i<<endl;
        bool flag=false;
        int x,y;
        for(x=i-1,y=i-2;y>=0;y--,x--){
            if(str[x]>str[y] && flag==false){
                str[x]--;
                flag=true;
                str[y]=9;
                int p,q;
                for(p=x,q=x+1;q<i;p++,q++){
                    if(str[p]<str[q]){
                        str[p]=9;
                        str[q]--;
                    }
                }
                continue;
            }
            if(flag==true){
                str[y]=9;
            }
        }
        flag=false;
        for(x=i-1,y=i-2;y>=0;y--,x--){
            if(str[x]>str[y] && flag==false){
                str[x]--;
                flag=true;
                str[y]=9;
                continue;
            }
            if(flag==true){
                str[y]=9;
            }
        }
        printf("Case #%d: ",t);
        bool tri=false;
        for(int j=i-1;j>=0;j--){
            if(tri==false && str[j]==0)
                continue;
            else{
                    tri=true;
                    cout<<str[j];
            }
    }
        cout<<endl;
        //printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
