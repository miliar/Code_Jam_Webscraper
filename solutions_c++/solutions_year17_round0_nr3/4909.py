#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long

lld nextPowerOf2(lld n)
{
	n--;
	n |= n >> 1;
	n |= n >> 2;
	n |= n >> 4;
	n |= n >> 8;
	n |= n >> 16;
	n++;
	return n;
}

int main() {
	// your code goes here
	freopen("in.txt", "r", stdin);
	freopen("out_c_large.txt", "w", stdout);
	lld test,n,i,j,k;
    cin>>test;
    for(lld t=1;t<=test;t++){
        cin>>n>>k;
        if(k==1){
            if(n%2==0){
                cout<<"Case #"<<t<<": "<<n/2<<" "<<n/2-1<<endl;
            }
            else{
                cout<<"Case #"<<t<<": "<<n/2<<" "<<n/2<<endl;
            }
            continue;
        }
        map<lld,lld> m;
        map<lld,lld>::iterator it;
        if(n%2==0){
            m[n/2]++;
            m[n/2-1]++;
        }
        else{
            m[n/2]+=2;
        }
        lld x=n/2;
        it=m.end();
        while(x!=1){
            it--;
            x=it->first;
            if(x%2==0){
                m[x/2]+=it->second;
                m[x/2-1]+=it->second;
            }
            else{
                m[x/2]+=2*it->second;
            }
        }
   //     for(it=m.begin();it!=m.end();it++){
     //       cout<<it->first<<": "<<it->second<<endl;
       // }
        lld nearest_power=nextPowerOf2(k);
        if(k!=nearest_power){
            nearest_power/=2;
        }
        x=n/nearest_power;
        lld diff=k-nearest_power;
        lld ans;
 //       cout<<nearest_power<<" "<<x<<" "<<diff<<" "<<m[x]<<endl;
        if(diff<m[x]){
            ans=x;
        }
        else{
            ans=x-1;
        }
        if(ans%2==0){
            cout<<"Case #"<<t<<": "<<ans/2<<" "<<ans/2-1<<endl;
        }
        else{
            cout<<"Case #"<<t<<": "<<ans/2<<" "<<ans/2<<endl;
        }

    }


    return 0;
}
