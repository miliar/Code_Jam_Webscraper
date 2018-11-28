#include <bits/stdc++.h>
using namespace std;
vector<int> ans,ori;

int work(vector<int> &out,vector<int> &in,int pos,int nine) {
    if (pos==in.size())
        return 1;
    int sta,pre;
    if (nine==0) {
        sta=in[pos];
        if (pos!=0)
            pre=out[pos-1];
    }
    else if (nine==1) {
        sta=9;
        pre=out[pos-1];
    }
    if (pos==0)
        pre=0;
    for (int i=sta;i>=pre;i--) {
        out[pos]=i;
        if (nine==0)
            if (i!=in[pos])
                nine=1;
        if (work(out,in,pos+1,nine)==1)
            return 1;
    }
    return 0;
}

int main () {
    int T;
    cin>>T;
    string o;
    for (int i=1;i<=T;i++) {
        ori.clear();
        cin>>o;
        int si=o.size();
        for (int j=0;j<si;j++) {
            int bep=(o[j]-'0');
            ori.push_back(bep);
        }
        ans.clear();
        ans.resize(si);
        work(ans,ori,0,0);
        int flag=0;
        printf("Case #%d: ",i);
        for (int j=0;j<si;j++) {
            if ((flag==0)&&ans[j]==0)
                continue;
            printf("%d",ans[j]);
            flag=1;
        }
        printf("\n");
    }
    return 0;
}
