#include <bits/stdc++.h>
#define pii pair<int,int>

using namespace std;

int n,k;

struct state{
    int first,second,mi,ma;
};

bool operator< (const state& stt,const state& st){
    if(stt.mi==st.mi){
        if(stt.ma==st.ma)return st.first<stt.first;
        else return stt.ma<st.ma;
    }else return stt.mi<st.mi;
}

void calc(){
    priority_queue<state> q;
    state cur;
    cur.first = 1;
    cur.second = n;
    int mid;
    mid = (n+1)/2;
    cur.mi = min(n-mid,mid-1);
    cur.ma = max(n-mid,mid-1);
    q.push(cur);
    while(k--){
        cur = q.top();
//        cout<<cur.first<<" "<<cur.second<<endl;
        q.pop();
        if(cur.first==cur.second)continue;
        state l,r;
        mid = (cur.first+cur.second)/2;
        int ma,mi;
        l = {cur.first,mid-1,mi,ma};
        r = {mid+1,cur.second,mi,ma};

        if(cur.second>mid){
            mid = (r.second+r.first)/2;
            r.mi = min(r.second-mid,mid-r.first);
            r.ma = max(r.second-mid,mid-r.first);
            q.push(r);
        }
        if(mid>cur.first){
            mid = (l.second+l.first)/2;
            l.mi = min(l.second-mid,mid-l.first);
            l.ma = max(l.second-mid,mid-l.first);
            q.push(l);
        }

    }
    cout<<cur.ma<<" "<<cur.mi;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cs(0);
    while(t--){
        ++cs;
        cin>>n>>k;

        cout<<"Case #"<<cs<<": ";
        calc();
        cout<<"\n";
    }
    return 0;
}
