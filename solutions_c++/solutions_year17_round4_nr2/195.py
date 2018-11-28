#include<bits/stdc++.h>
using namespace std;
const int MX = 1009;
string str;
int T , Tn , seats , people , orig[MX] , freq[MX];
int check(int mid){
    int extra = 0 , ret = 0;
    for(int j = seats ; j ; j--){
        if(orig[j] > mid){
            extra += orig[j] - mid;
            ret += orig[j] - mid;
        }
        else{
            extra -= (mid - orig[j]);
            extra = max(extra , 0);
        }
    }
    if(extra > 0) return -1;
    else return ret;
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    while(T--){
        printf("Case #%d: ",++Tn);
        int m , jd;
        cin>>seats>>people>>m;
        jd = m;
        memset(freq , 0 , sizeof(freq));
        memset(orig , 0 , sizeof(orig));
        while(m--){
            int x , y;
            cin>>y>>x;
            ++freq[x];
            ++orig[y];
        }
        int st = *max_element(freq , freq + MX);
        int en = jd , ans1 , ans2 , aa;
      //  cout<<"#"<<st<<' '<<en<<endl;
        while(st <= en){
            int mid = (st + en)/2;
            if(check(mid) != -1){
                ans1 = mid;
                ans2 = check(mid);
                en = mid-1;
            }
            else st = mid + 1;
        }
        cout<<ans1<<' '<<ans2<<endl;
    }
}

