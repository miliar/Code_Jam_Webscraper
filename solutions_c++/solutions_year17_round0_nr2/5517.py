#include <bits/stdc++.h>
#define int long long
using namespace std;

string s;
int t,test,k,tt,ans,i,len,j,val,a[100],kol,n,m;

void f(){
     for(i=kol;i>0;--i)
                        for(j=i-1;j>0;--j)
                    if(a[i] < a[j]){
                        --a[i-1];
                        for(k=i;k<=kol;++k)
                        a[k] = 9;
                        for(k=i-1;k>0;--k)
                            if(a[k]<0) --a[k-1],a[k]+=10;
                        tt=1;
                        return;
                    }
}

//int
 main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> t;
    for(test = 1;test<=t;++test){

        cin >> n;
        cout << "Case #"<<test<<": ";
        {
            kol = 0;
            while(n){
                a[++kol] = n % 10;
                n/=10;
            }
            reverse(a+1,a+kol+1);
            while(1){
                    tt = 0;
                   f();
                   if(!tt)break;
            }

                val = 0;
            for(i = 1; i <= kol; ++i)
                val = val * 10 + a[i];

            cout << val << '\n';
        }
    }

}
