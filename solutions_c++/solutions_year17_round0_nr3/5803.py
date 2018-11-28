#include<iostream>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;

int main(){
    freopen("C-small-1-attempt1.in","r",stdin);
    freopen("C-small-1-attempt1.out","w",stdout);
    long t;
    cin >> t;
    for(long c=1;c<=t;c++){
        long n,k;
        cin >> n >> k;
        long s[n];
        vector<long> index;
        vector<long> dist;
        long mid = (n-1)/2;
        s[mid]=1;
       // cout << "mid: " << mid << " s[mid]: " << s[mid] << endl;
        index.push_back(n);
        index.push_back(-1);
        index.push_back(mid);
        sort(index.begin(),index.end());
        /*for(int i=0;i<index.size();i++)
            cout << index[i] << " ";
        cout << endl;*/
        dist.push_back(mid);
        dist.push_back(n-mid-1);
        long maxi;
        long z;
        long in = dist[0]>=dist[1]?0:1;
        //cout << "in: " << in << endl;
        k--;
        if(k==0){
                in =1;
                long ls = index[in]-index[in-1]-1;
        long rs = index[in+1]-index[in]-1;
        if(ls>=rs){
            cout << "Case #" << c << ": " << ls << " " << rs << endl;
        }
        else{
            cout << "Case #" << c << ": " << rs << " " << ls << endl;
        }
        continue;
        }
        /*else if(k>n/2){
                cout << "Case #" << c << ": " << 0 << " " << 0 << endl;
                continue;
        }*/
        else{
        for(long i=0;i<k;i++){
            //if(i==0){
                //cout << "in: " << in << " index[in]: " << index[in] << endl;
                mid = index[in] + (index[in+1]-index[in])/2;
                s[mid]=1;
                //cout << "mid: " << mid << " s[mid]: " << s[mid] << endl;
                index.push_back(mid);
                sort(index.begin(),index.end());
                for(z=0;z<index.size();z++){
                    if(index[z]==mid)
                        break;
                }
                /*for(int k=0;k<index.size();k++)
                    cout << index[k] << " ";
                cout << endl;*/
                dist.clear();
                for(long j=1;j<index.size();j++){
                        //cout << "j: " << j << " index[j]: " << index[j] << endl;
                        long temp = index[j]-index[j-1]-1;
                        //cout << "temp: " << temp << endl;
                        dist.push_back(temp);
                }
                /*for(int k=0;k<dist.size();k++)
                    cout << dist[k] << " ";
                cout << endl;*/
                maxi = dist[0];
                in = 0;
                for(long j=1;j<dist.size();j++){
                    if(dist[j]>maxi){
                        maxi = dist[j];
                        in = j;
                    }
                }
                //cout << "in: " << in << " maxi: " << maxi << endl;
            /*}
            else{
                h
            }*/
        }
        }
        long ls = index[z]-index[z-1]-1;
        long rs = index[z+1]-index[z]-1;
        if(ls>=rs){
            cout << "Case #" << c << ": " << ls << " " << rs << endl;
        }
        else{
            cout << "Case #" << c << ": " << rs << " " << ls << endl;
        }
    }
}
