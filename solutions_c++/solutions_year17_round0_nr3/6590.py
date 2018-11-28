#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>

using namespace std;

typedef long long in;

int main(){
    int test;
    cin >> test;
    for(int t=1;t<=test;t++){
        cout << "Case #" << t << ": ";
        int n,k;
        cin >> n >> k;
        int lastpos=n/2;
        if(n%2==0)
            lastpos--;
        vector<int> a(n);
        a[lastpos]=1;
        vector<pair<int,int> > dist(n);
        int mini,maxi;
        for(int i=0;i<n;i++){
            if(i<lastpos){
                dist[i].first=i;
                dist[i].second=lastpos-i-1;
            }
            if(i==lastpos){
                dist[i].first=-1;
                dist[i].second=-1;
            }
            if(i>lastpos){
                dist[i].first=i-lastpos-1;
                dist[i].second=dist.size()-i-1;
            }
        }
        k--;
        if(k==0){
            mini=n/2;
            maxi=n/2;
            if(n%2==0)
                mini-=1;
        }
        while(k!=0){
            k--;
            mini=-1;
            maxi=-1;
            for(int i=0;i<n;i++){
                if(a[i]!=1&&min(dist[i].first,dist[i].second)>mini){
                    mini=min(dist[i].first,dist[i].second);
                    maxi=max(dist[i].first,dist[i].second);
                    lastpos=i;
                }
                else if(a[i]!=1&&min(dist[i].first,dist[i].second)==mini&&max(dist[i].first,dist[i].second)>maxi){
                    mini=min(dist[i].first,dist[i].second);
                    maxi=max(dist[i].first,dist[i].second);
                    lastpos=i;
                }
            }
            //cout << k << " " << lastpos << endl;
            if(k!=0){
                a[lastpos]=1;
                for(int i=0;i<n;i++){
                    if(i<lastpos){
                        dist[i].second=min(dist[i].second,lastpos-i-1);
                    }
                    if(i==lastpos){
                        dist[i].first=-1;
                        dist[i].second=-1;
                    }
                    if(i>lastpos){
                        dist[i].first=min(dist[i].first,i-lastpos-1);
                    }
                }
            }
        }
        /*cout << endl;
        for(int i=0;i<n;i++)
            cout << a[i] << " ";
        cout << endl;*/
        cout << maxi << " " << mini << endl;
    }
}
