#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
using namespace std;
ifstream fin("in.in");
ofstream fo("out.out");
map < long long , long long > m;
priority_queue <long long> pro;
int test;
long long n,k,cnt=0,ans1,ans2,ck=0;
int main(){
    ios_base::sync_with_stdio(0);
    fin>>test;
    for(int t=1;t<=test;t++){
        if(t>1) fo<<"\n";
        fo<<"Case #"<<t<<": ";
        fin>>n>>k;
        cnt=0;
        ck=0;
        pro.push(n);
        m.clear();
        m[n]=1;
        while(!pro.empty()){
            if(ck==1){ pro.pop(); continue;}
            long long pr=pro.top();
            cnt+=m[pr];
            pro.pop();
            //fo<<pr;
            long long kq1,kq2;
            if(pr%2==0){
                kq1=pr/2;
                kq2=kq1-1;
            }
            else{
                kq1=pr/2;
                kq2=kq1;
            }
            //fo<<" "<<kq1<<" "<<kq2<<endl;
            if(cnt>=k){
                ans1=kq1;
                ans2=kq2;
                ck=1;
                continue;
            }
            if(pr==1) continue;
            if(m[kq1]==0){
                m[kq1]=m[pr];
                pro.push(kq1);
            }
            else{
                m[kq1]+=m[pr];
            }
            if(m[kq2]==0){
                m[kq2]=m[pr];
                pro.push(kq2);
            }
            else{
                m[kq2]+=m[pr];
            }
        }
        fo<<ans1<<" "<<ans2;
    }
}
