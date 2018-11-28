#include <iostream>
#include <algorithm>
using namespace std;
int tc;
int n,p;
int main(){
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>n>>p;
        int sum=0;
        switch(p){
        case 2:
            {
                int val[2];
                fill_n(val,2,0);
                for(int i=0;i<n;++i){
                    int x;
                    cin>>x;
                    ++val[x%2];
                }
                while(val[0]>0){
                    ++sum;
                    --val[0];
                }
                while(val[1]>0){
                    ++sum;
                    val[1]-=2;
                }
            }
            break;
        case 3:
            {
                int val[3];
                fill_n(val,3,0);
                for(int i=0;i<n;++i){
                    int x;
                    cin>>x;
                    ++val[x%3];
                }
                while(val[0]>0){
                    ++sum;
                    --val[0];
                }
                while(val[1]>0&&val[2]>0){
                    ++sum;
                    --val[1];
                    --val[2];
                }
                while(val[1]>0){
                    ++sum;
                    val[1]-=3;
                }
                while(val[2]>0){
                    ++sum;
                    val[2]-=3;
                }
            }
            break;
        case 4:
            {
                int val[4];
                fill_n(val,4,0);
                for(int i=0;i<n;++i){
                    int x;
                    cin>>x;
                    ++val[x%4];
                }
                while(val[0]>0){
                    ++sum;
                    --val[0];
                }
                while(val[1]>0&&val[3]>0){
                    ++sum;
                    --val[1];
                    --val[3];
                }
                while(val[2]>1){
                    ++sum;
                    val[2]-=2;
                }
                int rem=0;
                if(val[2]>0){
                    ++sum;
                    rem+=2;
                }
                while(val[1]>0){
                    if(rem%4==0)++sum;
                    rem+=1;
                    --val[1];
                }
                while(val[3]>0){
                    if(rem%4==0)++sum;
                    rem+=3;
                    --val[3];
                }
            }
            break;
        }
        cout<<"Case #"<<ct<<": "<<sum<<endl;
    }
}
