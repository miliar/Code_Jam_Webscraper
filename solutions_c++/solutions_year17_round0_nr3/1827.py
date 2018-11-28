#include<iostream>
#include<cstdio>
#include<string>
#include<map>
using namespace std;
int main(){
    int cas,q;
    freopen("C-large.in","r",stdin);
    freopen("Cout.txt","w",stdout);
    cin>>cas;
    for(int q=1;q<=cas;q++){
        unsigned long long n,k,ans1,ans2,tmp;
        map<unsigned long long,unsigned long long> ma;
        map<unsigned long long,unsigned long long>::reverse_iterator iter;
        cin>>n>>k;
        ma[n] = 1;
        while(true){
            iter = ma.rbegin();
            n = iter->first;
            if(k <= iter->second){
                if(n&1) ans1 = ans2 = n/2;
                else{
                    ans1=n/2;
                    ans2 = ans1-1;
                }
                break;
            }

            k-=iter->second;
            if(n&1){
                if(n > 1) ma[n/2]+=2*iter->second;
            }
            else{
                ma[n/2]+=iter->second;
                if((n/2-1) > 0) ma[n/2-1]+=iter->second;
            }
            ma.erase(iter->first);
        }
        cout<<"Case #"<<q<<": "<<ans1<<' '<<ans2<<endl;
    }
    return 0;
}
