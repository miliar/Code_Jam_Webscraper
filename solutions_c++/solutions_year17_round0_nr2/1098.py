/*************************************************************************
	> File Name: B.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月08日 星期六 11时53分49秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll arr[50],vis[50];
ll N;

int dfs(int pos){
    if(pos==0)
        return -1;
    if(arr[pos]>arr[pos-1]){
        vis[pos]--;
        vis[pos-1]=9;
        return pos;
    }
    int point=dfs(pos-1);
    if(vis[pos]>vis[pos-1]){
        vis[pos]--;
        vis[pos-1]=9;
        return pos;
    }else return point;
}

int main(){
    //ios::sync_with_stdio(false);
    //freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    int T;scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        cin>>N;ll x=N;
        int pos=0;
        while(x){
            arr[pos++]=x%10;
            x/=10;
        }
        memcpy(vis,arr,sizeof(arr));
        int p=dfs(pos-1);
        bool change=false;
        cout<<"Case #"<<kase<<": ";
        for(int i=pos-1;i>=0;i--){
            if(change)
                cout<<9;
            else{
                if(i==p)
                    arr[i]--,change=true;   
                if(arr[i])
                    cout<<arr[i];
            }
        }
        cout<<endl;
    }
    return 0;
}
