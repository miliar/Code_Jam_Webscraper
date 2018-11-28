#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
#define int long long
using namespace std;

const int nmax = 100010;
int n, k, p, x, t, y, a[1010], ls[1010], rs[1010];

pair<int,int> solve(int n, int k){
memset(a, 0, sizeof a);
        while (k--){
            ls[0]=0;
            for (int i=1; i<=n; i++) if (a[i]==1) ls[i]=0; else ls[i]=ls[i-1]+1;
            rs[n+1]=0;
            for (int j=n; j>=1; j--) if (a[j]==1) rs[j]=0; else rs[j]=rs[j+1]+1;
            int mn = -1;
            for (int i=1; i<=n; i++) if (a[i]==0) mn = max(mn, min(ls[i], rs[i]));

            int cnt=0, pos=-1;
            for (int i=1; i<=n; i++)
                if ((a[i]==0) && min(ls[i], rs[i])==mn){
                    cnt++;
                    pos=i;
                }
            if (cnt==1){
                a[pos]=1;
                if (k==0){
                    return make_pair(max(ls[pos], rs[pos])-1, min(ls[pos], rs[pos])-1);
                }
                continue;
            }
/*
for (int i=1; i<=n; i++) cout << ls[i] << " ";
            cout << endl;
            for (int i=1; i<=n; i++) cout << rs[i] << " ";
            cout << endl;*/
            int mn2 = -1;
            for (int i=1; i<=n; i++) if ((a[i]==0) && min(ls[i], rs[i])==mn) mn2 = max(mn2, max(ls[i], rs[i]));
            cnt=0, pos=-1;
            for (int i=1; i<=n; i++)
                if ((a[i]==0) && max(ls[i], rs[i])==mn2 && min(ls[i], rs[i])==mn){
                    cnt++;
                    pos=i;
                    break;
                }
            if (cnt==1){
                a[pos]=1;
                if (k==0){
                    return make_pair(max(ls[pos], rs[pos])-1, min(ls[pos], rs[pos])-1);
                }
                continue;
            }


        }
       // for (int i=1; i<=n; i++) cout << a[i] << " ";
       // cout << endl;
}

int f(int pos, int x){
    if (pos<=1) return 0;
    int b = (pos/2)>=x;
    if (b==0) return 0;
    if (pos%2==0){
        return f(pos/2, x)+f((pos-1)/2, x)+b;
    }
    return 2*f(pos/2, x)+b;
}

int f2(int pos, int x){
    if (pos<=1) return 0;
    int b = ((pos-1)/2)>=x;
    if (b==0) return 0;
    if (pos%2==0){
        return f2(pos/2, x)+f2((pos-1)/2, x)+b;
    }
    return 2*f2(pos/2, x)+b;
}

int cool(int n, int k){
    int l=0, r=n;
    while (l+1<r){
        int mid = (l+r) >> 1;
        if (f(n, mid)>=k) l=mid; else r=mid;
    }
    //if (f(n, l>k) l++;
    return l;
}

int cool2(int n, int k){
    int l=0, r=n;
    while (l+1<r){
        int mid = (l+r) >> 1;
        if (f2(n, mid)>=k) l=mid; else r=mid;
    }
    //if (f(n, l>k) l++;
    return l;
}

pair<int, int> norm(int n, int k){
    map<int, int> mm;
    mm.clear();
    mm[n]=1;
    while (k>0){
        int last = mm.rbegin()->first;
        int cnt = mm[last];
        if (k-cnt<0) break;
        k-=cnt;
        mm.erase(mm.find(last));
        if (last%2==0){
            mm[(last/2)]+=cnt;
            mm[(last/2)-1]+=cnt;
        } else mm[last/2]+=cnt*2;
    }
    int last = mm.rbegin()->first;
    return make_pair(last/2, last/2 - (last%2==0?1:0));

}

main(){
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);

/*
for (int i=1; i<=200; i++){
        //cout << i << ": ";
        for (int j=1; j<=i; j++) {
            if (solve(i, j).first!=cool(i, j)) cout << i << " booya " << j << endl;
        }
        //cout << endl;
    }
    return 0;*/
    /*
    int num=0;
    for (int i=1; i<=1000; i++){
        //cout << i << ": ";
        for (int j=1; j<=i; j++){
            if (make_pair(cool(i,j), cool2(i, j))!=norm(i, j-1)) puts("boooya");
        }
        //cout << endl;
    }
    return 0;
    for (int i=1; i<=50; i++){
        cout << i << ": ";
        for (int j=1; j<=i; j++) cout << norm(i, j-1).first << " ";
        cout << endl;
    }
    return 0;*/

int num=0;
cin >> t;
    while (t--){
        num++;
        cin >> n >> k;
        pair<int, int> ans=norm(n, k-1);
        cout << "Case #" << num << ": " << ans.first << " " << ans.second << endl;


    }


}

