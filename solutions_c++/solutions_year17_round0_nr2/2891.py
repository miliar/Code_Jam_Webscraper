#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output4.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        string s;
        cin>>s;
        long long di[19];
        long long dt[19];
        int len=s.length();
        for(int j=0;j<len;j++){
            di[j]=((long long)(s[j]-'0'));
        }
        int filled=0;
        for(int j=0;j<len;j++){

            //cout<<"j "<<j<<endl;
            if(j==len-1){
                dt[j]=di[j];
                filled++;
            }else if(di[j]<di[j+1]){
                dt[j]=di[j];
                filled++;
            }else if(di[j]>di[j+1]){
                dt[j]=di[j]-1;
                filled++;
                break;
            }else{//di[j]==di[j+1]
                int k=j+1;
                while(di[k]==di[k+1]&&k+1<len)k++;
                //cout<<"j "<<j<<"k "<<k<<endl;
                if(k==len-1||di[k]<=di[k+1]){
                    for(int l=j;l<=k;l++){
                        dt[l]=di[l];
                        filled++;
                    }
                    j=k;
                }else{
                    dt[j]=di[j]-1;
                    filled++;
                    break;
                }
            }
        }
        long long lt=0;
        for(int j=0;j<len;j++){
            lt*=10l;
            if(j<filled)lt+=dt[j];
            else lt+=9l;
        }
        cout<<"Case #"<<i+1<<": "<<lt<<endl;
    }
    return 0;
}
