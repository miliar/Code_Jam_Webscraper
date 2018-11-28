#include <bits/stdc++.h>

using namespace std;

typedef long long int LL;


int k;
map<string ,int >vis;

void bfs(string s){
    vis.clear();

    queue<pair<string,int> >q;
    int sz = s.size();
    string res="";
    for(int i=0;i<sz;i++) res+="+";
//    cout<<res<<endl;
    q.push(make_pair(s,0));
    pair<string,int> tem,tmp;
    while(!q.empty()){
        tem = q.front();q.pop();
        if(tem.first==res){
            cout<<tem.second<<endl;
            return ;
        }

        for(int i=k-1;i<sz;i++){
            tmp = tem;
            for(int j=i;j>i-k;j--){
                if(tmp.first[j]=='+')
                    tmp.first[j]='-';
                else
                tmp.first[j]='+';
            }

            if(vis[tmp.first])  continue;
            tmp.second++;
            q.push(tmp);
            vis[tmp.first]=1;
        }

    }
    cout<<"IMPOSSIBLE"<<endl;
    return ;
}

void solve(string s){
    int sz = s.size();
    string res="";
    for(int i=0;i<sz;i++) res+="+";
    int l=0,r=sz-1,sum=0;
    if(res==s){
        printf("%d\n",sum);
        return ;
    }

    while(l+k-1<=r){
        while(l+k-1<=r&&s[l]=='+')l++;
        while(l+k-1<=r&&s[r]=='+')r--;
        if(s[l]==s[r]&&s[r]=='+') break;
        if((~sum&1)&&s[l]=='-'){
            for(int i=l;l+k<=sz&&i<l+k;i++){
                if(s[i]=='+')  s[i]='-';
                else           s[i]='+';
            }
//            printf("%d <--l\n",l);
//            cout<<s<<endl;
            sum++;
            if(res==s){
                printf("%d\n",sum);
                return ;
            }
        }
        if((sum&1)&&s[r]=='-'){
            for(int i=r;i>r-k;i--){
                if(s[i]=='+')  s[i]='-';
                else           s[i]='+';
            }
//            printf("%d <--r\n",r);
//            cout<<s<<endl;
            sum++;
            if(res==s){
                printf("%d\n",sum);
                return ;
            }
        }
    }
    cout<<"IMPOSSIBLE"<<endl;
    return ;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _;
    cin>>_;
//    cout<<_<<endl;
    for(int i=1;i<=_;i++){
        string s;

        cin>>s>>k;
//        cout<<s<<" "<<k<<endl;
        printf("Case #%d: ",i);
        solve(s);
    }
    return 0;
}
