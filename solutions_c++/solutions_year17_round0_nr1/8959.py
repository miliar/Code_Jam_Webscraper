#include<bits/stdc++.h>
using namespace std;

int main(){

    freopen("A-large.in","rt",stdin);
    freopen("outputf.txt","wt",stdout);

    int t,a,k;
    string s;
    cin>>t;

    getchar();

    for(int j=1;j<=t;j++){

        cin>>s>>a;

        bool f;

        getchar();
        k=0;
        int n = s.size();

        for(int mm = 0 ; mm<=20;mm++){

            for(int i=0;i<=n-a;i++){

                if(s[i]=='-'){
                    k++;

                    for(int jj=i;jj<i+a;jj++){
                        //cout<<jj<<"\n";
                        if(s[jj]=='-') s[jj] = '+';
                        else s[jj] = '-';
                    }


                    //cout<<s<<"\n";
                }
            }

            f = false;

            for(int i=0;i<n;i++){
                if(s[i]=='-'){
                    f = true;

                    break;
                }
            }
        }


        //cout<<s<<"\n";

        if(f==false){
            printf("Case #%d: %d\n",j,k);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",j);
        }


    }

    return 0;

}
