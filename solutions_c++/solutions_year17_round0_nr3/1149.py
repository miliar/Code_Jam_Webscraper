#include<bits/stdc++.h>
using namespace std;
long long n,k;
set<long long,greater<long long> >s;
set<long long>::iterator it;
map<long long ,long long>mp;
int main(){
    FILE *fp1=fopen("C:\\Users\\Administrator\\Downloads\\C-large.in","r+");
    FILE *fp2=fopen("C:\\Users\\Administrator\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int ansnum=0;
    while(t--){

        fscanf(fp1,"%lld%lld",&n,&k);cout<<n<<" "<<k<<endl;
        s.clear();
        mp.clear();
        s.insert(n);
        mp[n]=1;
        long long ansl,ansr;
        while(k>0){
            it=s.begin();
            if(mp[*it]>=k){
                if(*it%2==0){
                    ansl=*it/2;
                    ansr=*it/2-1;
                }
                else{
                    ansl=*it/2;
                    ansr=*it/2;
                }
                break;
            }
            else{
                if(*it%2==0){
                    k-=mp[*it];
                    if(mp[*it/2]==0){
                        s.insert(*it/2);
                    }
                    if(mp[*it/2-1]==0){
                        s.insert(*it/2-1);
                    }
                    mp[*it/2]+=mp[*it];
                    mp[*it/2-1]+=mp[*it];
                    s.erase(*it);
                }
                else{
                    if(mp[*it/2]==0){
                        s.insert(*it/2);
                    }
                    k-=mp[*it];
                    mp[*it/2]+=mp[*it]*2;
                    s.erase(*it);
                }
            }
        }
        cout<<ansl<<" "<<ansr<<endl;
        fprintf(fp2,"Case #%d: %lld %lld\n",++ansnum,ansl,ansr);
    }


}
