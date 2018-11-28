#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll>v;

void tidy(){
    for(ll a=0;a<=9;a++){
        for(ll b=a;b<=9;b++){
            for(ll c=b;c<=9;c++){
                for(ll d=c;d<=9;d++){
                    for(ll e=d;e<=9;e++){
                        for(ll f=e;f<=9;f++){
                            for(ll g=f;g<=9;g++){
                                for(ll h=g;h<=9;h++){
                                    for(ll i=h;i<=9;i++){
                                        for(ll j=i;j<=9;j++){
                                            for(ll k=j;k<=9;k++){
                                                for(ll l=k;l<=9;l++){
                                                    for(ll m=l;m<=9;m++){
                                                        for(ll n=m;n<=9;n++){
                                                            for(ll o=n;o<=9;o++){
                                                                for(ll p=o;p<=9;p++){
                                                                    for(ll q=p;q<=9;q++){
                                                                        for(ll r=q;r<=9;r++){
                                                                            ll ans=a*100000000000000000+b*10000000000000000+c*1000000000000000+d*100000000000000+e*10000000000000+f*1000000000000+g*100000000000+h*10000000000+i*1000000000+j*100000000+k*10000000+l*1000000+m*100000+n*10000+o*1000+p*100+q*10+r;
                                                                            v.push_back(ans);
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

int main(){
    tidy();
    ll t,p=1;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        if(n==1000000000000000000){
            cout<<"Case #"<<p<<": "<<999999999999999999<<"\n";
            p++;
            continue;
        }
        ll r=v.size();
        ll l=0;
        while(l<=r){
            ll mid=l+(r-l)/2;
            if(v[mid]>n){
                r=mid-1;
            }else if(v[mid]<=n){
                if(v[mid]==n){
                    cout<<"Case #"<<p<<": "<<v[mid]<<"\n";
                    p++;
                    break;
                }else if(v[mid]<n && v[mid+1]>n){
                    cout<<"Case #"<<p<<": "<<v[mid]<<"\n";
                    p++;
                    break;
                }else{
                    l=mid+1;
                }
            }
        }
    }
}
