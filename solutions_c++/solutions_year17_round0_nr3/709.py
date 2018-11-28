#include<bits/stdc++.h>
using namespace std;
int main()
{

      freopen("C-large.in","r",stdin);
      freopen("C-large.out","w",stdout);
    int cases,caseno=0;
    cin>>cases;
    while(cases--)
    {
          long long K,N;
             cin>>N>>K;
            map<long long,long long>mymap;
            mymap[N]++;
            long long ans1=N,ans2=N;
            long long res1,res2;
            while(K>0)
            {
                long long trm;
                if(ans1==ans2){
                 trm = ans1;
                 if(ans1%2==0)
                 {
                     ans1 = ans1/2;
                     ans2 = ans1-1;
                 }
                 else
                 {
                     ans1 = ans2 = (ans1/2);
                 }
                }
                else{
                trm = ans1;
                ans1 = ans2;
                long long hh = trm/2;
                if(ans1 == hh)
                ans2 = hh-1;
                else
                ans2 = hh;
                }
                long long cnt =mymap[trm];
                    K = K-cnt;
                    if(trm%2==0)
                    {
                        res1 = trm/2;
                        res2 = res1-1;
                        mymap[trm/2]+=(cnt);
                        mymap[(trm/2)-1]+=(cnt);
                    }
                    else
                    {
                        res1 = res2= trm/2;
                        mymap[trm/2]+=(2*cnt);
                    }


            }


          cout<<"Case #"<<++caseno<<": "<<res1<<" "<<res2<<endl;
  }
    return 0;
}


