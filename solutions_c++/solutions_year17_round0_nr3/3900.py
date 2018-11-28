#include <bits/stdc++.h>
using namespace std;

long long n,k;

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cs = 1;
    while(t--){
        printf("Case #%d: ",cs++);
        cin >> n >> k;
        map<long long,long long> mp;
        map<long long,bool> vis;
        mp[n]++;
        priority_queue<long long> q;
        q.push(n);
        long long mx = 0 ;
        long long mn = 0;
        vis[n] = 1;
        while(!q.empty()){
            long long num = q.top();
            q.pop();
            if(mp[num] >= k){
                if(num % 2 == 0){
                    mx = num/2;
                    mn = num/2-1;
                }
                else{
                    mx = num/2;
                    mn = num/2;
                }
                break;
            }
            k-=mp[num];
            if(num % 2 == 0){
                    long long one = num/2;
                    long long two = num/2-1;
                    mp[one]+=mp[num];
                    mp[two]+=mp[num];
                    if(!vis[one]){
                        q.push(one);
                        vis[one] = 1;
                    }
                    if(!vis[two]){
                        q.push(two);
                        vis[two] = 1;
                    }
                }
                else{
                    long long one = num/2;
                    mp[one] += mp[num]*2;
                    if(!vis[one]){
                        q.push(one);
                        vis[one] = 1;
                    }
                }
        }
        cout << mx << " " << mn << endl;
    }
    return 0;
}
